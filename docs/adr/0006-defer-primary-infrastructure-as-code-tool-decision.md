# ADR-0006: Defer Primary Infrastructure as Code Tool Decision

## Status

Accepted

## Date

2026-07-14

## Context

The repository contains Terraform-oriented placeholders and roadmap language for a future Terraform Foundation phase. The blueprint describes Terraform as a representative Infrastructure as Code technology and also uses broader language such as “Terraform or another IaC approach.”

The repository does not currently contain Terraform modules, state configuration, provider configuration, validation workflows, or infrastructure implementation artifacts.

## Decision

ECPEL will defer the primary Infrastructure as Code tool decision.

Terraform remains a reference and planning context because current repository documents include Terraform-oriented placeholders and phases. This ADR does not adopt Terraform as an implemented tool and does not claim that Terraform infrastructure exists.

A future ADR must accept or supersede this decision before ECPEL claims a primary IaC implementation tool.

## Decision Drivers

- Terraform is repeatedly referenced as a future or representative IaC area.
- Current documentation does not provide enough evidence to accept Terraform as the primary implementation tool.
- IaC tool selection affects state management, workflow automation, security controls, cost controls, and provider strategy.
- The evidence-driven rule prevents representative technologies from being treated as implemented capabilities.

## Considered Options

- **Accept Terraform as the primary IaC tool now:** Not accepted because current evidence is insufficient and no Terraform implementation exists.
- **Choose another IaC tool now:** Not accepted because no requirements or analysis support another choice.
- **Defer the primary IaC tool decision while retaining Terraform as a planning reference:** Accepted because it matches the current repository state.

## Consequences

### Positive consequences

- Avoids overstating Terraform adoption.
- Preserves future flexibility for IaC tool selection.
- Keeps Terraform placeholders useful for planning without implying implementation.
- Requires a future explicit decision before IaC implementation claims are made.

### Negative consequences

- Terraform Foundation work remains blocked from implementation until a future decision is accepted.
- Some documentation must continue to use careful status language.

### Neutral consequences

- Existing Terraform-oriented files remain in place.
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

- [README.md](../../README.md) lists Terraform as mentioned by directory or file names only and not implemented.
- [ROADMAP.md](../../ROADMAP.md) defines a planned Terraform Foundation phase and requires Terraform design and validation before implementation.
- [BLUEPRINT.md](../../BLUEPRINT.md) lists Terraform as a representative IaC tool and states that representative technologies are not implementation commitments.
- [ARCHITECTURE.md](../../ARCHITECTURE.md) states that working Terraform modules are out of scope until evidence exists.

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
- [Terraform runbook placeholder](../runbooks/terraform.md)

## Supersedes

None

## Superseded By

None
