#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[4]
LAB = ROOT / "labs/configuration-management/ansible-local-foundation"
MANDATORY = [
    ".github/workflows/ansible-local-foundation.yml",
    "labs/README.md",
    "labs/configuration-management/ansible-local-foundation/README.md",
    "labs/configuration-management/ansible-local-foundation/ansible.cfg",
    "labs/configuration-management/ansible-local-foundation/.ansible-lint",
    "labs/configuration-management/ansible-local-foundation/requirements.in",
    "labs/configuration-management/ansible-local-foundation/requirements.lock",
    "labs/configuration-management/ansible-local-foundation/inventory/local.yml",
    "labs/configuration-management/ansible-local-foundation/playbooks/apply.yml",
    "labs/configuration-management/ansible-local-foundation/playbooks/cleanup.yml",
    "labs/configuration-management/ansible-local-foundation/roles/local_foundation/defaults/main.yml",
    "labs/configuration-management/ansible-local-foundation/roles/local_foundation/tasks/main.yml",
    "labs/configuration-management/ansible-local-foundation/roles/local_foundation/handlers/main.yml",
    "labs/configuration-management/ansible-local-foundation/roles/local_foundation/templates/config.json.j2",
    "labs/configuration-management/ansible-local-foundation/roles/local_foundation/templates/ecpel-ansible-local-foundation.service.j2",
    "labs/configuration-management/ansible-local-foundation/scripts/preflight-target.sh",
    "labs/configuration-management/ansible-local-foundation/tests/validate_structure.py",
    "labs/configuration-management/ansible-local-foundation/tests/validate_guardrails.py",
    "labs/configuration-management/ansible-local-foundation/evidence/README.md",
]
RESERVED = {
    "tests/verify_state.py",
    "tests/verify_cleanup.py",
    "scripts/preflight-windows.ps1",
    "scripts/create-target.ps1",
    "scripts/run-local-validation.sh",
    "scripts/destroy-target.ps1",
    "evidence/manifest.md",
    "evidence/validation-summary.md",
}


def read(path: str) -> str:
    return (ROOT / path).read_text()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


for rel in MANDATORY:
    require((ROOT / rel).is_file(), f"mandatory path is not a regular file: {rel}")

for rel in RESERVED:
    p = LAB / rel
    if p.exists():
        require(p.is_file(), f"reserved PR 2 path is not a regular file: {rel}")

allowed_lab_files = {str(Path(rel).relative_to("labs/configuration-management/ansible-local-foundation")) for rel in MANDATORY if rel.startswith("labs/configuration-management/ansible-local-foundation/")} | RESERVED
extra = [str(p.relative_to(LAB)) for p in LAB.rglob("*") if p.is_file() and str(p.relative_to(LAB)) not in allowed_lab_files]
require(not extra, f"unapproved lab files present: {extra}")

for rel in ["labs/README.md", "labs/configuration-management/ansible-local-foundation/README.md", "labs/configuration-management/ansible-local-foundation/evidence/README.md"]:
    text = read(rel)
    require(text.startswith("# "), f"missing top-level heading: {rel}")
    require(text.count("```") % 2 == 0, f"unbalanced fenced code blocks: {rel}")
    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in link or link.startswith("#"):
            continue
        target = ((ROOT / rel).parent / link).resolve()
        require(str(target).startswith(str(ROOT.resolve())), f"link escapes repository: {rel} -> {link}")
        require(target.exists(), f"broken relative link: {rel} -> {link}")

readme = read("labs/configuration-management/ansible-local-foundation/README.md")
for section in ["Status", "Purpose and ADR", "Future Target Model", "PR 1 Scope and Exclusions", "Directory Structure", "Dependencies", "Static Validation", "Security Boundaries", "PR 2 Storage and RAM Gates", "Evidence", "Limitations"]:
    require(f"## {section}" in readme, f"missing README section: {section}")
for value in ["Lab status: **Simulated**", "Artifact validation: **Passed**", "Functional execution: **Not Run**", "Local functional evidence: **Not Available**"]:
    require(value in readme, f"missing approved README status: {value}")

labs_index = read("labs/README.md")
require("| [Ansible Local Foundation](configuration-management/ansible-local-foundation/README.md) | Static local Ansible configuration-management foundation governed by ADR-0008; functional execution remains Not Run | Simulated |" in labs_index, "missing labs index entry")

inv = yaml.safe_load(read("labs/configuration-management/ansible-local-foundation/inventory/local.yml"))
require(list(inv) == ["ecpel_local_lab"], "inventory must contain exactly one group")
hosts = inv["ecpel_local_lab"].get("hosts", {})
require(list(hosts) == ["ecpel_local_target"], "inventory must contain exactly one host")
host = hosts["ecpel_local_target"]
require(host.get("ansible_connection") == "local", "inventory must use local connection")
require("ansible_host" not in host and "ansible_port" not in host and "ansible_user" not in host, "remote inventory fields are not allowed")

apply_doc = yaml.safe_load(read("labs/configuration-management/ansible-local-foundation/playbooks/apply.yml"))
cleanup_doc = yaml.safe_load(read("labs/configuration-management/ansible-local-foundation/playbooks/cleanup.yml"))
require(apply_doc[0]["hosts"] == "ecpel_local_target", "apply playbook must target approved host")
require(cleanup_doc[0]["hosts"] == "ecpel_local_target", "cleanup playbook must target approved host")
require(apply_doc[0]["roles"] == [{"role": "local_foundation"}], "apply playbook must reference approved role")

defaults = yaml.safe_load(read("labs/configuration-management/ansible-local-foundation/roles/local_foundation/defaults/main.yml"))
expected_defaults = {
    "local_foundation_wsl_distribution": "ecpel-ansible-local-foundation",
    "local_foundation_ubuntu_version": "24.04",
    "local_foundation_target_alias": "ecpel_local_target",
    "local_foundation_package_name": "jq",
    "local_foundation_lab_root": "/opt/ecpel/ansible-local-foundation",
    "local_foundation_config_path": "/opt/ecpel/ansible-local-foundation/config.json",
    "local_foundation_marker_path": "/opt/ecpel/ansible-local-foundation/.jq-installed-by-lab",
    "local_foundation_unit_name": "ecpel-ansible-local-foundation.service",
    "local_foundation_unit_path": "/etc/systemd/system/ecpel-ansible-local-foundation.service",
    "local_foundation_lab_classification": "Simulated",
}
for key, value in expected_defaults.items():
    require(defaults.get(key) == value, f"unexpected default {key}")

workflow_text = read(".github/workflows/ansible-local-foundation.yml")
workflow = yaml.safe_load(workflow_text)
require(workflow.get("name") == "Ansible Local Foundation Validation", "unexpected workflow display name")
require(workflow.get("permissions") == {"contents": "read"}, "unexpected workflow permissions")
job = workflow["jobs"]["ansible-local-foundation"]
require(job.get("name") == "Ansible local foundation static validation", "unexpected job/check name")
require(job.get("runs-on") == "ubuntu-24.04", "unexpected runner")
require("actions/setup-python@v6.0.0" in workflow_text and "python-version: '3.12'" in workflow_text, "Python 3.12 setup is required")
require(re.search(r"pull_request:\n\s+branches:\n\s+- main\n\s+push:", workflow_text), "pull_request trigger must target main without path filter")
require("workflow_dispatch:" in workflow_text and "base_sha:" in workflow_text and "required: true" in workflow_text, "workflow_dispatch base_sha must be required")
for path in ["labs/configuration-management/ansible-local-foundation/**", "labs/README.md", ".github/workflows/ansible-local-foundation.yml"]:
    require(path in workflow_text, f"missing push path filter: {path}")

terr = read(".github/workflows/terraform-local-foundation.yml")
require("name: Terraform ${{ matrix.terraform-version }} local validation" in terr, "Terraform job name expression changed")
require("- 1.6.0" in terr and "- 1.15.8" in terr, "Terraform matrix values changed")

evidence = read("labs/configuration-management/ansible-local-foundation/evidence/README.md")
for value in ["Lab classification | Simulated", "Artifact validation | Passed", "Functional validation | Pending", "Functional execution | Not Run", "Check mode | Not Run", "Idempotence | Not Run", "Cleanup | Not Run", "WSL target created | No", "Local functional evidence | No"]:
    require(value in evidence, f"missing evidence value: {value}")

print("structure validation passed")
