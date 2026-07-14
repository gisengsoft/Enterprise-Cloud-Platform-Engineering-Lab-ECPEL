# ADR-0003: Defer GitOps Strategy Decision

## Status

Accepted

## Date

2026-07-14

## Context

ECPEL documentation identifies GitOps as a future delivery and platform engineering concern. The roadmap places GitOps after CI/CD, DevSecOps, and Kubernetes/EKS planning. The blueprint describes Argo CD only as a representative technology, not an implementation commitment.

The repository does not currently include GitOps controllers, manifests, reconciliation configuration, deployment environments, or workflow automation.

## Decision

ECPEL will defer the GitOps implementation strategy decision until prerequisite platform, CI/CD, security, and runtime decisions have sufficient evidence.

GitOps remains a planned future domain, but no GitOps tool, controller, reconciliation model, or deployment process is accepted as implemented by this ADR.

## Decision Drivers

- GitOps depends on source control validation, delivery workflows, runtime platform decisions, and operational ownership.
- The repository does not contain implemented CI/CD, Kubernetes, ECS, or deployment environments.
- The roadmap identifies GitOps as a later planned phase.
- The blueprint states that representative technologies are not implementation commitments.

## Considered Options

- **Adopt a GitOps tool now:** Not accepted because no runtime platform or delivery workflow evidence exists.
- **Remove GitOps from the roadmap:** Not selected because GitOps remains a relevant future platform engineering domain.
- **Defer the GitOps strategy decision:** Accepted because it preserves future direction without inventing implementation.

## Consequences

### Positive consequences

- Avoids premature tool selection.
- Keeps GitOps aligned with future CI/CD, Kubernetes, security, and operations decisions.
- Prevents claims that a reconciliation loop exists when no such artifacts are present.

### Negative consequences

- GitOps implementation details remain undefined.
- Future platform delivery design requires another ADR or a superseding ADR.

### Neutral consequences

- GitOps remains part of the target architecture and roadmap.
- Reference technologies may still be discussed without being adopted.

## Risks

- **Technical risk:** Future platform documents may assume a GitOps model before it is accepted.
- **Security risk:** Controller permissions may be underestimated if tool selection is rushed later.
- **Operational risk:** Reconciliation behavior and rollback procedures may be unclear until a strategy is accepted.
- **Financial risk:** Future tooling choices may introduce costs not yet analyzed.
- **Maintenance risk:** GitOps documentation may need updates once runtime platforms are decided.

## Validation

This decision will be validated by:

- keeping GitOps language in planned or target-state terms;
- requiring a future ADR before a GitOps tool or reconciliation strategy is accepted;
- validating that documentation does not claim active GitOps controllers or deployments without evidence.

## Evidence

- [ROADMAP.md](../../ROADMAP.md) places GitOps in a planned later phase and states that no GitOps controller or reconciliation loop is claimed without implementation evidence.
- [ARCHITECTURE.md](../../ARCHITECTURE.md) identifies GitOps and delivery strategy as a future ADR decision area.
- [BLUEPRINT.md](../../BLUEPRINT.md) lists Argo CD as a representative GitOps technology, not an implementation commitment.
- [README.md](../../README.md) lists GitOps as mentioned by directory or file names only and not implemented.

## Revisit Conditions

Revisit this decision when:

- CI/CD and DevSecOps foundations exist;
- a runtime platform strategy has been accepted;
- Kubernetes or another reconciliation target is designed;
- repository evidence supports selecting a GitOps tool or strategy.

## Related Documents

- [README.md](../../README.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [BLUEPRINT.md](../../BLUEPRINT.md)
- [ROADMAP.md](../../ROADMAP.md)

## Supersedes

None

## Superseded By

None
