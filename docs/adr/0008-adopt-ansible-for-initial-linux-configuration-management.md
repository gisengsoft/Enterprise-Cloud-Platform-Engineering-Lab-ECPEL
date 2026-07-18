# ADR-0008: Adopt Ansible for Initial Linux Configuration Management

## Status

Accepted

## Date

2026-07-18

## Deciders

- ECPEL maintainer

## Consulted

- None at proposal time

## Informed

- ECPEL contributors

## Context

ECPEL does not currently have an adopted configuration-management
strategy.

Future platform work may require repeatable management of Linux packages,
files, templates, permissions, services, and other post-provisioning
system state. These concerns are separate from the creation and lifecycle
of infrastructure resources.

The initial use case is deliberately limited to a local, isolated, and
disposable Linux target owned by ECPEL, without cloud access, an external
workload, a production server, or permanent effects on the primary host.

The decision must support reproducible execution, state verification,
idempotence evidence, and cleanup while preserving:

"No evidence, no implementation."

## Decision Drivers

- Enable a low-risk executable laboratory without cloud resources.
- Support repeatable Linux configuration and state verification.
- Produce evidence through real and repeated execution.
- Keep configuration management separate from Infrastructure as Code.
- Remain independent of a cloud provider.
- Avoid using procedural shell scripts as the primary state-management
  mechanism.
- Defer remote operation until local evidence exists.

## Considered Options

### Ansible

Selected as the initial configuration-management tool because it supports
local Linux targets, inventories, playbooks, state-oriented modules,
templates, handlers, check mode, diff mode, and repeated execution.

The selection is limited to the initial ECPEL use case and does not make
Ansible a universal platform standard.

### Versioned shell scripts as the primary mechanism

Not selected as the primary mechanism because ECPEL would need to create
its own conventions for convergence, idempotence, dry-run, diff, and
change reporting.

Shell scripts may still support preparation, validation, evidence
collection, cleanup, and target lifecycle operations.

### Cloud-init as the primary mechanism

Not selected.

Cloud-init remains a possible future bootstrap mechanism for newly
created machines, but it is not the initial mechanism for repeatable
post-bootstrap configuration.

### Cloud-init combined with Ansible

Deferred.

A future design may use cloud-init for minimum bootstrap and Ansible for
subsequent configuration, but the first laboratory does not require both.

### Continue deferring configuration management

Not selected because continued deferral would prevent the next
low-cost and evidence-producing ECPEL laboratory.

## Decision

ECPEL will adopt Ansible as its initial and limited
configuration-management tool for local, isolated, and disposable Linux
targets.

The first use will be an ECPEL-owned laboratory with:

- no cloud account or cloud resource;
- no external workload;
- no production or persistent server;
- no real secrets;
- no permanent effect on the primary host.

Shell scripts may be used only to support preparation, validation,
evidence collection, cleanup, and creation or destruction of the
disposable target.

Cloud-init remains deferred as a possible future bootstrap mechanism.

Infrastructure as Code remains a separate decision. A future IaC tool
will manage infrastructure resources and their lifecycle, while
configuration management will manage post-provisioning system state.

GitHub Actions may validate configuration-management artifacts, but this
decision does not classify it as deployment automation.

The future laboratory must include, at minimum:

- versioned dependencies;
- preference for state-oriented modules;
- inventory and playbook-based execution;
- syntax and lint validation;
- check mode where supported;
- diff mode where safe;
- a real first execution;
- verification of the resulting state;
- a repeated execution;
- idempotence evidence;
- cleanup and cleanup verification.

Expansion to remote Linux hosts requires successful local evidence and a
separate future scope.

This ADR does not select the disposable-target technology, Linux image,
container, virtual machine, or virtualization backend.

## Consequences

### Positive consequences

- ECPEL gains a path to executable evidence without cloud cost.
- Linux configuration practices become reproducible and testable.
- Idempotence can be evaluated through repeated execution.
- Configuration management remains separate from Infrastructure as Code.
- The decision creates a controlled path toward future remote Linux
  targets.

### Negative consequences

- Python, Ansible, and lint dependencies must be maintained.
- Contributors must learn Ansible concepts and module behavior.
- Check-mode and diff support may vary between modules.
- The laboratory requires a sufficiently isolated Linux target.
- Remote use will require additional identity, connectivity, and security
  decisions.

### Neutral consequences

- No cloud provider is adopted.
- No Infrastructure as Code tool is selected.
- Cloud-init is not adopted.
- GitHub Actions remains a validation gate.
- No external workload or project is integrated.
- Accepting this ADR does not itself implement Ansible.

## Risks

- Tasks may not be idempotent.
- Excessive use of `shell` or `command` may bypass state-oriented
  behavior.
- Check mode may create false confidence.
- Diff output may expose sensitive content.
- Incorrect targeting may modify the primary host.
- Scope may expand prematurely into remote operations, hardening, or
  production.
- Cleanup may be incomplete.

Controls include preference for state-oriented built-in modules, real
execution and state tests, repeated execution with no unexpected changes,
absence of real secrets, disabling diff for sensitive content, an
isolated disposable target, and mandatory cleanup verification.

## Validation

Acceptance of this ADR does not prove that Ansible is implemented in
ECPEL.

The future laboratory must demonstrate:

- identifiable and versioned dependencies;
- a local, isolated, and disposable Linux target;
- successful syntax and lint validation;
- check mode where supported;
- diff mode only where safe;
- a successful real first execution;
- verification of the resulting state;
- a successful repeated execution with no unexpected changes;
- successful cleanup and cleanup verification;
- no permanent modification of the primary host;
- no cloud credentials or real secrets.

Check mode is preventive simulation and does not replace real execution.

A second execution with `changed=0` is required evidence of idempotent
behavior, but it does not alone prove that the resulting configuration is
correct. State verification is also required.

The laboratory will remain classified as **Simulated** because it is
local, disposable, does not configure cloud infrastructure, and does not
operate a real workload.

Successful local execution may be documented as local validation
evidence. CI lint, syntax, or check-mode results are CI validation
evidence only. Neither implies Cloud Validated, Operated, Production
Ready, or Reference Ready.

## Related Documents

- [ADR-0001: Record Architecture Decisions](0001-record-architecture-decisions.md)
- [ADR-0004: Adopt Evidence-Driven Implementation Rule](0004-adopt-evidence-driven-implementation-rule.md)
- [ADR-0006: Defer Primary Infrastructure as Code Tool Decision](0006-defer-primary-infrastructure-as-code-tool-decision.md)
- [ADR-0007: Adopt ECPEL as Platform Hub with Independent Project Repositories](0007-adopt-ecpel-as-platform-hub-with-independent-project-repositories.md)

This ADR complements ADR-0001.

It respects the evidence requirements established by ADR-0004.

It complements ADR-0006 by separating configuration management from the
future Infrastructure as Code decision.

It respects ADR-0007 because the future laboratory will be an ECPEL-owned
artifact and will not import an external project.

It does not modify ADR-0002, ADR-0003, or ADR-0005.

## Supersedes

None.

## Superseded By

None.
