# ADR-0006: Defer Primary Infrastructure as Code Tool Decision

## Status

Accepted

## Date

2026-07-14

## Context

The repository contains Terraform-oriented roadmap language for a future Terraform Foundation phase and a local-only simulated Terraform learning lab. The blueprint describes Terraform as a representative Infrastructure as Code technology and also uses broader language such as “Terraform or another IaC approach.”

The repository does not currently contain Terraform provider configuration, remote state configuration, cloud infrastructure modules, validation workflows, or cloud infrastructure implementation artifacts. The local lab is a simulation and does not establish Terraform as the primary implemented Infrastructure as Code tool.

## Decision

ECPEL will defer the primary Infrastructure as Code tool decision.

Terraform remains a reference, planning, and local-learning context because current repository documents include Terraform-oriented phases and a simulated lab. This ADR does not adopt Terraform as the primary implemented tool and does not claim that Terraform cloud infrastructure exists.

A future ADR must accept or supersede this decision before ECPEL claims a primary IaC implementation tool.

## Decision Drivers

- Terraform is repeatedly referenced as a future or representative IaC area.
- Current documentation and the simulated local lab do not provide enough evidence to accept Terraform as the primary implementation tool.
- IaC tool selection affects state management, workflow automation, security controls, cost controls, and provider strategy.
- The evidence-driven rule prevents representative technologies from being treated as implemented capabilities.

## Considered Options

- **Accept Terraform as the primary IaC tool now:** Not accepted because current evidence is insufficient and the local Terraform lab is simulated, not cloud infrastructure implementation.
- **Choose another IaC tool now:** Not accepted because no requirements or analysis support another choice.
- **Defer the primary IaC tool decision while retaining Terraform as a planning reference:** Accepted because it matches the current repository state.

## Consequences

### Positive consequences

- Avoids overstating Terraform adoption.
- Preserves future flexibility for IaC tool selection.
- Keeps Terraform references and the local lab useful for planning and learning without implying cloud implementation.
- Requires a future explicit decision before IaC implementation claims are made.

### Negative consequences

- Terraform Foundation cloud implementation work remains blocked until a future decision is accepted.
- Some documentation must continue to use careful status language.

### Neutral consequences

- Existing Terraform-oriented documentation and the simulated local lab remain in place.
- This ADR does not prevent future Terraform adoption.

## Risks

- **Technical risk:** Future documents may assume Terraform-specific workflows before the tool decision is accepted.
- **Security risk:** State and secret handling decisions may be deferred too long.
- **Operational risk:** Validation and drift management remain undefined until IaC strategy matures.
- **Financial risk:** Provider and cost-control assumptions may be inaccurate before IaC design exists.
- **Maintenance risk:** Terraform references may need revision if another tool is selected.

## Validation

This decision will be validated by:

- keeping Terraform language in planned, reference, or target-state terms;
- requiring a future ADR before Terraform is claimed as the primary implemented IaC tool;
- checking that no Terraform implementation claims are made without files, validation, and documentation evidence.

## Evidence

- [README.md](../../README.md) identifies the Terraform lab as local-only and simulated, and states that Terraform has not been adopted as the primary implemented Infrastructure as Code tool.
- [ROADMAP.md](../../ROADMAP.md) defines a planned Terraform Foundation phase and requires Terraform design and validation before implementation.
- [BLUEPRINT.md](../../BLUEPRINT.md) lists Terraform as a representative IaC tool and states that representative technologies are not implementation commitments.
- [ARCHITECTURE.md](../../ARCHITECTURE.md) states that cloud infrastructure and working platform automation remain out of scope until evidence exists.

## Revisit Conditions

Revisit this decision when:

- ECPEL is ready to choose an IaC tool;
- state management and provider strategy are documented;
- validation and workflow requirements are defined;
- Terraform or another IaC tool has supporting design evidence.

## Related Documents

- [README.md](../../README.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [BLUEPRINT.md](../../BLUEPRINT.md)
- [ROADMAP.md](../../ROADMAP.md)
- [Runbook documentation foundation](../runbooks/README.md)
- [Terraform Local Foundation Lab](../../labs/terraform-local-foundation/README.md)

## Supersedes

None

## Superseded By

None
