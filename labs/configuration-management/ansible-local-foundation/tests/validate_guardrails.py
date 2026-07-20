#!/usr/bin/env python3
from pathlib import Path
import ipaddress, re, yaml
ROOT=Path(__file__).resolve().parents[4]
LAB=ROOT/'labs/configuration-management/ansible-local-foundation'
for p in [LAB/'inventory/local.yml', LAB/'playbooks/apply.yml', LAB/'playbooks/cleanup.yml', LAB/'roles/local_foundation/tasks/main.yml', LAB/'roles/local_foundation/handlers/main.yml']:
    txt=p.read_text()
    assert 'delegate_to' not in txt and 'local_action' not in txt, p
    assert not re.search(r'ansible\.builtin\.(shell|command|raw|script)\b', txt), p
    assert not re.search(r'https?://(?!github\.com/gisengsoft/Enterprise-Cloud-Platform-Engineering-Lab-ECPEL)', txt), p
    assert '/mnt/' not in txt, p
    for m in re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', txt):
        ipaddress.ip_address(m); raise AssertionError((p,m))
inv=yaml.safe_load((LAB/'inventory/local.yml').read_text())
h=inv['ecpel_local_lab']['hosts']['ecpel_local_target']
assert h['ansible_connection']=='local'
for k in ['ansible_host','ansible_port','ansible_user','ansible_ssh_private_key_file','password','private_key']:
    assert k not in h
for p in [LAB/'roles/local_foundation/defaults/main.yml', LAB/'roles/local_foundation/templates/config.json.j2', LAB/'roles/local_foundation/templates/ecpel-ansible-local-foundation.service.j2']:
    txt=p.read_text()
    for bad in ['token','secret','credential','private key','Terraform','Kubernetes','GitOps','TaskGuard','aws_','azure','gcp']:
        assert bad.lower() not in txt.lower(), (p,bad)
assert 'ansible.builtin.apt' in (LAB/'roles/local_foundation/tasks/main.yml').read_text()
assert '/opt/ecpel/ansible-local-foundation' in (LAB/'roles/local_foundation/defaults/main.yml').read_text()
assert 'ecpel-ansible-local-foundation.service' in (LAB/'roles/local_foundation/defaults/main.yml').read_text()
print('guardrail validation passed')
