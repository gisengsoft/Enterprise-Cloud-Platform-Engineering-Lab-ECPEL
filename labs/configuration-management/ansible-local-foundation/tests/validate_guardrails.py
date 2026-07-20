#!/usr/bin/env python3
from pathlib import Path
import ipaddress
import re
import yaml

ROOT = Path(__file__).resolve().parents[4]
LAB = ROOT / "labs/configuration-management/ansible-local-foundation"
APPROVED = {
    "package": "jq",
    "alias": "ecpel_local_target",
    "connection": "local",
    "classification": "Simulated",
    "root": "/opt/ecpel/ansible-local-foundation",
    "config": "/opt/ecpel/ansible-local-foundation/config.json",
    "marker": "/opt/ecpel/ansible-local-foundation/.jq-installed-by-lab",
    "unit": "ecpel-ansible-local-foundation.service",
    "unit_path": "/etc/systemd/system/ecpel-ansible-local-foundation.service",
}
EXECUTABLE_CONFIGS = [
    LAB / "ansible.cfg",
    LAB / ".ansible-lint",
    ROOT / ".github/workflows/ansible-local-foundation.yml",
    LAB / "scripts/preflight-target.sh",
    LAB / "roles/local_foundation/templates/config.json.j2",
    LAB / "roles/local_foundation/templates/ecpel-ansible-local-foundation.service.j2",
]
YAML_FILES = list((LAB / "inventory").glob("**/*.yml")) + list((LAB / "playbooks").glob("**/*.yml")) + list((LAB / "roles").glob("**/*.yml"))
PROHIBITED_MODULES = {"shell", "command", "raw", "script", "ansible.builtin.shell", "ansible.builtin.command", "ansible.builtin.raw", "ansible.builtin.script"}
REMOTE_FIELDS = {"ansible_host", "ansible_port", "ansible_user"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def text(path: Path) -> str:
    return path.read_text()


def walk_yaml(node, path, ancestors=()):
    if isinstance(node, dict):
        for key, value in node.items():
            yield key, value, ancestors
            yield from walk_yaml(value, path, ancestors + (key,))
    elif isinstance(node, list):
        for item in node:
            yield from walk_yaml(item, path, ancestors)


def check_common_text(path: Path, content: str) -> None:
    require(not re.search(r'(?<![A-Za-z])(?:dest|path|root):\s*[\'"]?/mnt/', content), f"/mnt destination is not allowed in {path}")
    for match in re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content):
        ipaddress.ip_address(match)
        raise AssertionError(f"IP address is not allowed in {path}: {match}")
    require(not re.search(r"https?://(?!github\.com/gisengsoft/Enterprise-Cloud-Platform-Engineering-Lab-ECPEL\b)", content), f"external URL is not allowed in {path}")
    sensitive_patterns = ["lookup('env', '" + "TOKEN", 'lookup("env", "' + "TOKEN", "id-token: write", "oidc", "BEGIN " + "PRIVATE" + " KEY", "BEGIN RSA " + "PRIVATE" + " KEY"]
    for bad in sensitive_patterns:
        require(bad.lower() not in content.lower(), f"sensitive pattern is not allowed in {path}: {bad}")
    require(not re.search(r"\b(kubernetes|gitops|taskguard)\b.*\b(run|apply|deploy|execute|start)\b", content, re.I), f"out-of-scope execution term in {path}")
    require(not re.search(r"\b(terraform)\b.*\b(init|plan|apply|destroy|validate|test|fmt)\b", content, re.I), f"Terraform execution is not allowed in {path}")


for path in YAML_FILES + EXECUTABLE_CONFIGS:
    check_common_text(path, text(path))

inventory = yaml.safe_load(text(LAB / "inventory/local.yml"))
host = inventory["ecpel_local_lab"]["hosts"][APPROVED["alias"]]
require(host.get("ansible_connection") == APPROVED["connection"], "inventory must use local connection")
for key in host:
    require(key not in REMOTE_FIELDS and not key.startswith("ansible_ssh_"), f"remote inventory field is not allowed: {key}")
require("plugin:" not in text(LAB / "inventory/local.yml"), "dynamic inventory plugin is not allowed")

for path in YAML_FILES:
    data = yaml.safe_load(text(path))
    for key, value, ancestors in walk_yaml(data, path):
        if key in {"delegate_to", "local_action"}:
            raise AssertionError(f"delegation is not allowed in {path}")
        if isinstance(key, str) and key in PROHIBITED_MODULES:
            raise AssertionError(f"prohibited module {key} in {path}")
        if isinstance(key, str) and (key.startswith("amazon.aws.") or key.startswith("community.aws.") or key.startswith("azure.") or key.startswith("google.cloud.")):
            raise AssertionError(f"cloud/external collection module is not allowed in {path}: {key}")
        if isinstance(key, str) and key.startswith("ansible_ssh_"):
            raise AssertionError(f"ansible_ssh field is not allowed in {path}: {key}")
        if isinstance(value, str) and re.search(r"\b(password|credential|private[_ -]?key|secret)\b", value, re.I):
            raise AssertionError(f"sensitive value text is not allowed in {path}: {value}")

defaults = yaml.safe_load(text(LAB / "roles/local_foundation/defaults/main.yml"))
expected = {
    "local_foundation_package_name": APPROVED["package"],
    "local_foundation_target_alias": APPROVED["alias"],
    "local_foundation_lab_classification": APPROVED["classification"],
    "local_foundation_lab_root": APPROVED["root"],
    "local_foundation_config_path": APPROVED["config"],
    "local_foundation_marker_path": APPROVED["marker"],
    "local_foundation_unit_name": APPROVED["unit"],
    "local_foundation_unit_path": APPROVED["unit_path"],
}
for key, value in expected.items():
    require(defaults.get(key) == value, f"unapproved default value for {key}")

preflight = text(LAB / "scripts/preflight-target.sh")
for mutation in ["apt ", "apt-get", "dnf ", "yum ", "ansible-playbook", "ansible ", "systemctl start", "systemctl stop", "systemctl enable", "systemctl disable", "mkdir ", "rm ", "curl ", "wget ", "wsl.exe"]:
    require(mutation not in preflight, f"preflight mutation or Ansible execution is not allowed: {mutation}")
for required in ["uname -s", "/proc/version", "/run/WSL", "WSL_DISTRO_NAME", "24.04", "systemd", "python3.12"]:
    require(required in preflight, f"preflight missing guard: {required}")

workflow = yaml.safe_load(text(ROOT / ".github/workflows/ansible-local-foundation.yml"))
require(workflow.get("permissions") == {"contents": "read"}, "workflow permissions must be contents: read only")
require("id-token" not in text(ROOT / ".github/workflows/ansible-local-foundation.yml"), "OIDC id-token permission is not allowed")

print("guardrail validation passed")
