# Architecture Decision Records

Architecture Decision Records (ADRs) document significant technical, architectural, operational, and governance decisions for ECPEL.

ADRs support the repository philosophy: **No evidence, no implementation.** An ADR can record an accepted direction, a rejected option, or a deferral, but it does not prove that a capability is implemented.

## Purpose

The purpose of ADRs is to make important decisions explicit, reviewable, traceable, and revisitable. ADRs should explain the context, decision, drivers, options, consequences, risks, validation approach, and evidence behind a decision.

ADRs are especially important when a decision affects multiple platform domains, changes the roadmap, establishes a long-term constraint, or influences security, cost, operations, reliability, compliance, or implementation sequencing.

## When an ADR is required

Create or update an ADR for decisions such as:

- cloud provider or account strategy;
- identity and access model;
- infrastructure-as-code strategy;
- runtime platform selection or sequencing;
- GitOps and delivery strategy;
- security and compliance control strategy;
- observability and reliability strategy;
- FinOps and governance model;
- AI platform or MLOps governance boundaries;
- decisions that supersede an earlier ADR;
- decisions that change repository maturity or roadmap assumptions.

## When an ADR is not required

An ADR is usually not required for:

- typo fixes;
- formatting-only documentation changes;
- minor wording improvements that do not change meaning;
- adding links to existing documents;
- routine maintenance that does not affect architecture or governance;
- implementation details already governed by an accepted ADR and documented elsewhere.

## Numbering convention

ADRs use a four-digit sequence:

```text
ADR-0000
ADR-0001
ADR-0002
```

`ADR-0000` is reserved for the template. Decision records start at `ADR-0001` and must be sequential. Do not reuse numbers after an ADR is superseded or rejected.

## File naming convention

ADR filenames use lowercase kebab-case:

```text
NNNN-short-decision-title.md
```

Examples:

```text
0000-template.md
0001-record-architecture-decisions.md
0002-defer-primary-implementation-cloud-decision.md
```

The filename should match the ADR title as closely as practical.

## Lifecycle and status model

Allowed ADR status values are:

- **Proposed** — under discussion and not yet accepted;
- **Accepted** — approved as the current decision or current intentional deferral;
- **Rejected** — evaluated and intentionally not adopted;
- **Superseded** — replaced by a newer ADR;
- **Deprecated** — no longer recommended, but not directly replaced.

A status of **Accepted** does not imply that a platform capability is implemented. Implementation requires repository evidence such as code, configuration, validation, tests, diagrams, runbooks, and operational documentation.

## Review process

1. Identify the decision and confirm that an ADR is needed.
2. Check this index to avoid duplicate ADRs.
3. Copy the [ADR template](0000-template.md) into the next sequential ADR file.
4. Document context, decision, drivers, options, consequences, risks, validation, evidence, revisit conditions, and related documents.
5. Link supporting evidence from [README.md](../../README.md), [ARCHITECTURE.md](../../ARCHITECTURE.md), [BLUEPRINT.md](../../BLUEPRINT.md), [ROADMAP.md](../../ROADMAP.md), RFCs, diagrams, runbooks, playbooks, or market analysis where applicable.
6. Review the ADR for consistency with the governing principle: **No evidence, no implementation.**
7. Update the ADR index after the ADR is accepted, rejected, deprecated, or superseded.

## Superseding process

When a decision changes:

1. Create a new ADR with the next sequential number.
2. Set the old ADR status to **Superseded**.
3. Add the new ADR number to the old ADR's `Superseded By` section.
4. Add the old ADR number to the new ADR's `Supersedes` section.
5. Update the ADR index table.

Do not delete superseded ADRs. Historical decisions are part of the project record.

## Relationship with RFCs

RFCs are used to discuss proposals before a decision is accepted. ADRs record the decision after review. A major proposal may begin as an RFC and later become an ADR.

RFCs should answer: “What should we consider?”

ADRs should answer: “What did we decide, why, and with what consequences?”

## Relationship with architecture, blueprint, and roadmap

- [ARCHITECTURE.md](../../ARCHITECTURE.md) describes the target architecture vision and identifies decision areas that may require ADRs.
- [BLUEPRINT.md](../../BLUEPRINT.md) describes the domain-oriented target platform blueprint and intentionally leaves major choices to ADRs.
- [ROADMAP.md](../../ROADMAP.md) defines phase sequencing, dependency rules, status terminology, and exit criteria.
- ADRs record specific decisions that support or refine those documents.

If an ADR changes the architecture, blueprint, or roadmap, update the affected document in the same change or explicitly document why the update is deferred.

## ADR index

| ADR | Title | Status | Date | Supersedes |
| --- | --- | --- | --- | --- |
| [ADR-0001](0001-record-architecture-decisions.md) | Record Architecture Decisions | Accepted | 2026-07-14 | None |
| [ADR-0002](0002-defer-primary-implementation-cloud-decision.md) | Defer Primary Implementation Cloud Decision | Accepted | 2026-07-14 | None |
| [ADR-0003](0003-defer-gitops-strategy-decision.md) | Defer GitOps Strategy Decision | Accepted | 2026-07-14 | None |
| [ADR-0004](0004-adopt-evidence-driven-implementation-rule.md) | Adopt Evidence-Driven Implementation Rule | Accepted | 2026-07-14 | None |
| [ADR-0005](0005-sequence-ecs-before-eks-in-roadmap-planning.md) | Sequence ECS Before EKS in Roadmap Planning | Accepted | 2026-07-14 | None |
| [ADR-0006](0006-defer-primary-infrastructure-as-code-tool-decision.md) | Defer Primary Infrastructure as Code Tool Decision | Accepted | 2026-07-14 | None |
| [ADR-0007](0007-adopt-ecpel-as-platform-hub-with-independent-project-repositories.md) | Adopt ECPEL as Platform Hub with Independent Project Repositories | Accepted | 2026-07-18 | None |
| [ADR-0008](0008-adopt-ansible-for-initial-linux-configuration-management.md) | Adopt Ansible for Initial Linux Configuration Management | Accepted | 2026-07-18 | None |
