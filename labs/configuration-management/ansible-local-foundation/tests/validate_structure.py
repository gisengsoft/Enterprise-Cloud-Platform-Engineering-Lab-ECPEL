#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[4]
LAB=ROOT/'labs/configuration-management/ansible-local-foundation'
REQ=[LAB/p for p in ['README.md','ansible.cfg','.ansible-lint','requirements.in','requirements.lock','inventory/local.yml','playbooks/apply.yml','playbooks/cleanup.yml','roles/local_foundation/defaults/main.yml','roles/local_foundation/tasks/main.yml','roles/local_foundation/handlers/main.yml','roles/local_foundation/templates/config.json.j2','roles/local_foundation/templates/ecpel-ansible-local-foundation.service.j2','scripts/preflight-target.sh','tests/validate_structure.py','tests/validate_guardrails.py','evidence/README.md']]+[ROOT/'.github/workflows/ansible-local-foundation.yml',ROOT/'labs/README.md']
missing=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
assert not missing, missing
readme=(LAB/'README.md').read_text()
for text in ['Lab status: **Simulated**','Artifact validation: **Pending**','Functional execution: **Not Run**','ADR-0008','evidence/README.md','ansible_connection: local']:
    assert text in readme, text
inv=yaml.safe_load((LAB/'inventory/local.yml').read_text())
assert list(inv)==['ecpel_local_lab']
hosts=inv['ecpel_local_lab']['hosts']
assert list(hosts)==['ecpel_local_target']
assert hosts['ecpel_local_target']['ansible_connection']=='local'
assert 'ansible_host' not in hosts['ecpel_local_target']
for pb in ['apply.yml','cleanup.yml']:
    docs=yaml.safe_load((LAB/'playbooks'/pb).read_text())
    assert docs[0]['hosts']=='ecpel_local_target'
assert 'local_foundation' in (LAB/'playbooks/apply.yml').read_text()
defaults=(LAB/'roles/local_foundation/defaults/main.yml').read_text()
for v in ['ecpel-ansible-local-foundation','24.04','ecpel_local_target','jq','/opt/ecpel/ansible-local-foundation','Simulated']:
    assert v in defaults
wf=(ROOT/'.github/workflows/ansible-local-foundation.yml').read_text()
assert 'name: Ansible Local Foundation Validation' in wf
assert 'name: Ansible local foundation static validation' in wf
assert 'ubuntu-24.04' in wf and 'python-version: \'3.12\'' in wf
terr=(ROOT/'.github/workflows/terraform-local-foundation.yml').read_text()
assert 'name: Terraform ${{ matrix.terraform-version }} local validation' in terr
assert '- 1.6.0' in terr and '- 1.15.8' in terr
ev=(LAB/'evidence/README.md').read_text()
for text in ['Lab classification | Simulated','Artifact validation | Pending','Functional execution | Not Run','WSL target created | No']:
    assert text in ev, text
reserved={'tests/verify_state.py','tests/verify_cleanup.py','scripts/preflight-windows.ps1','scripts/create-target.ps1','scripts/run-local-validation.sh','scripts/destroy-target.ps1','evidence/manifest.md','evidence/validation-summary.md'}
allowed={str(p.relative_to(LAB)) for p in REQ if str(p).startswith(str(LAB))}|reserved
extra=[str(p.relative_to(LAB)) for p in LAB.rglob('*') if p.is_file() and str(p.relative_to(LAB)) not in allowed]
assert not extra, extra
print('structure validation passed')
