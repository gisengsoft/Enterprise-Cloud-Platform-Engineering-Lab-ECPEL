# Ansible Local Foundation Lab

## Status

- Lab status: **Simulated**
- Artifact validation: **Pending** until real Pull Request checks complete
- Functional execution: **Not Run**
- Local functional evidence: **Not Available**

Static artifacts in this directory do not prove implementation. No WSL target was created, no functional Ansible execution or check mode was run, and no runtime evidence exists.

## Purpose and ADR

This lab is the PR 1 static foundation for ADR-0008, [Adopt Ansible for Initial Linux Configuration Management](../../../docs/adr/0008-adopt-ansible-for-initial-linux-configuration-management.md). It prepares repository structure, dependency locking, static tests, and CI validation only.

## Future Target Model

Future work may use a dedicated WSL2 distribution named `ecpel-ansible-local-foundation`. The future control node and managed node are the same dedicated target using `ansible_connection: local`. The sole future fallback is a Linux VM through VirtualBox. Existing `Ubuntu-22.04` remains untouched.

## PR 1 Scope and Exclusions

PR 1 includes static Ansible playbooks, role files, inventory, dependency locks, guardrail tests, documentation, and a static CI workflow. PR 1 excludes WSL lifecycle automation, VirtualBox lifecycle automation, functional playbook execution, check mode execution, jq installation on a real target, systemd service validation on a real target, idempotence proof, cleanup proof, cloud, IaC, Kubernetes, GitOps, ADR-0009, and TaskGuard.

## Directory Structure

| Path | Purpose |
| --- | --- |
| `ansible.cfg` | Repository-local Ansible configuration. |
| `.ansible-lint` | Strict lint configuration. |
| `requirements.in` | Direct Python tool requirements. |
| `requirements.lock` | Hash-checked transitive dependency lock. |
| `inventory/local.yml` | One-host local inventory. |
| `playbooks/apply.yml` | Static future apply playbook. |
| `playbooks/cleanup.yml` | Static future cleanup playbook. |
| `roles/local_foundation/` | Static role defaults, tasks, handlers, and templates. |
| `scripts/preflight-target.sh` | Read-only future target preflight. |
| `tests/` | Static structure and guardrail tests. |
| `evidence/README.md` | Explicit pending and Not Run evidence status. |

## Dependencies

Install with hash checking from the lock file only:

```bash
python -m pip install --require-hashes -r requirements.lock
python -m pip check
```

The direct requirements are `ansible-core==2.21.2` and `ansible-lint==26.6.0`. The full `ansible` package and external collections are not used.

## Static Validation

Future validation commands must name the inventory, playbook, and target limit explicitly:

```bash
ansible-inventory -i inventory/local.yml --list
ansible-playbook -i inventory/local.yml playbooks/apply.yml --limit ecpel_local_target --syntax-check
ansible-playbook -i inventory/local.yml playbooks/cleanup.yml --limit ecpel_local_target --syntax-check
ansible-lint playbooks/apply.yml playbooks/cleanup.yml roles/local_foundation
python tests/validate_structure.py
python tests/validate_guardrails.py
bash -n scripts/preflight-target.sh
```

These commands are static checks only. Functional action remains Not Run.

## Security Boundaries

The lab uses one local inventory host, no SSH, no remote destination, no IP address, no network hostname, no cloud authentication, no credentials, no external workload, and no production target. The generated JSON is fictional and deterministic.

## PR 2 Storage and RAM Gates

PR 2 remains future work. Its gates are 20 GB free on one drive minimum, 30 GB preferred, 6 GB available RAM minimum, and 8 GB preferred. Passing future gates never authorizes action automatically.

## Evidence

See [evidence/README.md](evidence/README.md). Artifact validation, functional validation, idempotence, cleanup, and target destruction are Pending or Not Run as documented there.

## Limitations

Expected systemd `active/exited/0` status is unobserved. This scaffold does not validate a real target, modify Ubuntu-22.04, create WSL, run Ansible functionally, or prove cleanup.
