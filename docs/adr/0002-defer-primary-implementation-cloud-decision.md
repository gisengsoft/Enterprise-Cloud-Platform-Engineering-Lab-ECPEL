# ADR-0002: Defer Primary Implementation Cloud Decision

## Status

Accepted

## Date

2026-07-14

## Context

The repository contains AWS-oriented roadmap language and reference documentation for future AWS networking and identity work. It also describes AWS as a representative or reference technology in the blueprint. However, the repository does not contain implemented cloud infrastructure, deployed AWS resources, cloud account evidence, or an accepted cloud provider implementation decision.

The governing principle requires that the repository must not claim implementation without evidence.

## Decision

ECPEL will defer the primary implementation cloud decision.

AWS may remain a reference and planning context where existing repository documents mention AWS-oriented domains, but this ADR does not adopt AWS as an implemented cloud platform and does not imply access to AWS accounts, deployed resources, or commercial product usage.

A future ADR must be created or this ADR must be superseded before ECPEL claims a primary implementation cloud provider.

## Decision Drivers

- The repository has AWS-oriented roadmap and reference documentation.
- The blueprint identifies AWS as a reference cloud provider family, not an implementation commitment.
- No cloud resources or provider configuration exist in the repository.
- Cloud provider selection affects identity, networking, security, compliance, cost, IaC, runtime, and operations.
- Provider selection requires more evidence than current repository documentation provides.

## Considered Options

- **Accept AWS as the primary implementation cloud now:** Not accepted because current evidence is insufficient and would overstate implementation direction.
- **Remain cloud-agnostic with no reference provider:** Not selected because existing repository structure already includes AWS-oriented planning areas.
- **Defer the primary implementation cloud decision while retaining AWS as a reference planning context:** Accepted because it aligns with the current evidence.

## Consequences

### Positive consequences

- Avoids claiming cloud implementation or commercial access that does not exist.
- Keeps current AWS-oriented planning documents usable as future design inputs.
- Preserves flexibility for future provider strategy decisions.
- Forces a future explicit ADR before provider implementation claims are made.

### Negative consequences

- Some future roadmap items remain blocked until provider strategy is decided.
- Documentation must be careful to distinguish AWS references from AWS implementation.

### Neutral consequences

- AWS-oriented roadmap and reference language remains in the repository.
- This ADR does not prevent future AWS implementation if later evidence supports it.

## Risks

- **Technical risk:** Future designs may assume AWS details before the provider decision is accepted.
- **Security risk:** Identity and access designs may become provider-specific too early.
- **Operational risk:** Runbooks may be written around unimplemented provider services.
- **Financial risk:** Cost assumptions may be inaccurate without real provider usage data.
- **Maintenance risk:** AWS references may need revision if a future decision changes provider direction.

## Validation

This decision will be validated by:

- ensuring documentation describes AWS as planned, reference, or target context rather than implemented infrastructure;
- rejecting claims that AWS resources exist unless repository evidence is added;
- creating or superseding this ADR before any provider implementation phase is marked implemented.

## Evidence

- [README.md](../../README.md) lists AWS Organizations as mentioned in documentation only and not implemented.
- [ROADMAP.md](../../ROADMAP.md) includes a planned AWS Networking and Identity phase and states that no AWS implementation is claimed without supporting artifacts.
- [BLUEPRINT.md](../../BLUEPRINT.md) lists AWS as a representative reference technology and states that reference technologies are not implementation commitments.
- [ARCHITECTURE.md](../../ARCHITECTURE.md) states that no cloud account or cloud resource should be considered implemented without supporting artifacts.

## Revisit Conditions

Revisit this decision when:

- ECPEL is ready to make a cloud provider implementation decision;
- market analysis or requirements justify a provider choice;
- Terraform, identity, networking, or runtime platform implementation work requires a provider commitment;
- a future ADR proposes AWS or another cloud provider as the primary implementation cloud.

## Related Documents

- [README.md](../../README.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [BLUEPRINT.md](../../BLUEPRINT.md)
- [ROADMAP.md](../../ROADMAP.md)
- [Market analysis](../market-analysis/README.md)

## Supersedes

None

## Superseded By

None
