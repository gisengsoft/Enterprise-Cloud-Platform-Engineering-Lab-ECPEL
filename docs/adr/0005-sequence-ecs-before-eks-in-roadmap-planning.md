# ADR-0005: Sequence ECS Before EKS in Roadmap Planning

## Status

Accepted

## Date

2026-07-14

## Context

The roadmap defines Phase 6 as ECS Application Platform and Phase 8 as Kubernetes and EKS. The repository does not currently implement ECS, EKS, containers, Kubernetes, or runtime platform automation. The blueprint states that Amazon ECS and Amazon EKS are representative AWS container platforms and not implementation commitments.

The repository needs to clarify whether the phase order is an intentional planning decision or an implementation claim.

## Decision

ECPEL accepts the roadmap planning sequence that evaluates and designs an ECS application platform before Kubernetes/EKS.

This is a planning and dependency decision only. It does not implement ECS, does not implement EKS, does not select ECS as the only runtime platform, and does not claim that either runtime exists in the repository.

## Decision Drivers

- The roadmap already places ECS before EKS.
- ECS can represent a simpler container platform path before Kubernetes complexity is introduced.
- EKS has additional dependencies on Kubernetes operations, cluster lifecycle, add-ons, GitOps, and SRE maturity.
- The repository needs runtime sequencing clarity without claiming implementation.

## Considered Options

- **Design EKS before ECS:** Not selected because the current roadmap sequences ECS first.
- **Design ECS before EKS:** Accepted as the current roadmap planning sequence.
- **Design both runtime paths in parallel:** Not selected for the initial roadmap because it increases documentation and dependency complexity.
- **Defer all runtime sequencing:** Not selected because the roadmap already establishes phase ordering.

## Consequences

### Positive consequences

- Clarifies that Phase 6 precedes Phase 8 intentionally.
- Allows runtime platform learning to progress from a simpler container platform path to Kubernetes planning.
- Keeps EKS dependent on stronger networking, identity, security, observability, CI/CD, and operational foundations.

### Negative consequences

- EKS design work is intentionally later in the roadmap.
- Future requirements may show that Kubernetes should be prioritized earlier, requiring this ADR to be revisited.

### Neutral consequences

- ECS and EKS remain unimplemented.
- This decision does not prevent future EKS adoption.
- This decision does not require AWS resources or commercial cloud access.

## Risks

- **Technical risk:** ECS-first planning may not fit all future workload requirements.
- **Security risk:** Runtime security requirements still need separate design work.
- **Operational risk:** ECS documentation might be mistaken for implemented runtime capability if status language is unclear.
- **Financial risk:** Future ECS or EKS experimentation could create costs if cost controls are not in place.
- **Maintenance risk:** Runtime sequencing may need revision as platform requirements mature.

## Validation

This decision will be validated by:

- keeping ECS and EKS documentation in planned or designed status until implementation evidence exists;
- preserving roadmap ordering unless superseded by a future ADR;
- requiring runtime implementation evidence before either platform is marked implemented;
- reviewing future runtime ADRs for consistency with this sequencing decision.

## Evidence

- [ROADMAP.md](../../ROADMAP.md) defines Phase 6 as ECS Application Platform and Phase 8 as Kubernetes and EKS.
- [ROADMAP.md](../../ROADMAP.md) states that ECS and EKS must not be marked implemented without repository artifacts and validation.
- [BLUEPRINT.md](../../BLUEPRINT.md) lists Amazon ECS and Amazon EKS as representative technologies, not implementation commitments.
- [README.md](../../README.md) lists ECS and EKS as mentioned by directory or file names only and not implemented.

## Revisit Conditions

Revisit this decision if:

- workload requirements require Kubernetes before ECS;
- runtime platform selection criteria change;
- AWS provider strategy changes;
- evidence emerges that ECS should be skipped or EKS should be prioritized;
- platform phases are reorganized in the roadmap.

## Related Documents

- [README.md](../../README.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [BLUEPRINT.md](../../BLUEPRINT.md)
- [ROADMAP.md](../../ROADMAP.md)
- [ECS runbook placeholder](../runbooks/ecs.md)
- [EKS runbook placeholder](../runbooks/eks.md)

## Supersedes

None

## Superseded By

None
