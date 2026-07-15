# ADR-0004: Adopt Evidence-Driven Implementation Rule

## Status

Accepted

## Date

2026-07-14

## Context

The repository repeatedly states the governing principle: **No evidence, no implementation.** Current documentation intentionally distinguishes target architecture, roadmap phases, reference technologies, placeholders, planned work, simulated work, and implemented capabilities.

ECPEL needs this rule recorded as a formal architectural decision so future changes cannot treat aspirational documentation as proof of implementation.

## Decision

ECPEL adopts the evidence-driven implementation rule:

> No evidence, no implementation.

A capability must not be described as implemented unless supporting repository artifacts exist. Acceptable evidence may include implementation files, configuration, validation output, tests, diagrams, runbooks, playbooks, ADRs, and operational documentation appropriate to the capability.

Design documents, roadmap entries, placeholders, representative technology lists, and target-state statements are not implementation evidence by themselves.

## Decision Drivers

- The repository currently contains many planned platform domains but little implementation evidence.
- The README, architecture, roadmap, and blueprint all require clear separation between current state and future intent.
- Future contributors need a consistent standard for status claims.
- The rule reduces the risk of fake labs, fake infrastructure claims, and misleading maturity statements.

## Considered Options

- **Adopt an explicit evidence-driven rule:** Accepted because it matches the current repository philosophy.
- **Allow documentation to imply implementation:** Rejected because it would contradict current repository guidance.
- **Use informal reviewer judgment only:** Rejected because it would be inconsistent and hard to audit.

## Consequences

### Positive consequences

- Prevents unsupported implementation claims.
- Improves trust in repository documentation.
- Creates a clear review standard for future PRs.
- Aligns README, architecture, roadmap, blueprint, and ADR process.

### Negative consequences

- Contributors must provide more evidence before marking work implemented.
- Some roadmap phases may remain planned longer while evidence is produced.

### Neutral consequences

- A future direction can still be planned, researched, or designed without being implemented.
- ADRs can record accepted decisions without claiming deployment.

## Risks

- **Technical risk:** Overly strict interpretation may slow prototyping if simulation status is not used clearly.
- **Security risk:** If evidence quality is weak, unsafe capabilities could still be overstated.
- **Operational risk:** A capability might be implemented technically but not operationally ready without runbooks or ownership.
- **Financial risk:** Cost-impacting resources could be created before FinOps evidence exists if the rule is ignored.
- **Maintenance risk:** Evidence requirements must stay consistent across documents.

## Validation

This decision will be validated by:

- reviewing future PRs for unsupported implementation claims;
- validating status terminology against [ROADMAP.md](../../ROADMAP.md) and [BLUEPRINT.md](../../BLUEPRINT.md);
- checking that implemented claims link to supporting artifacts;
- keeping ADRs, README, architecture, and roadmap consistent.

## Evidence

- [README.md](../../README.md) states the repository philosophy as “No evidence, no implementation.”
- [ARCHITECTURE.md](../../ARCHITECTURE.md) states that target architecture is not implementation evidence.
- [ROADMAP.md](../../ROADMAP.md) defines implementation status and states that no phase is currently implemented.
- [BLUEPRINT.md](../../BLUEPRINT.md) states that the blueprint never serves as implementation evidence.

## Revisit Conditions

Revisit this decision if:

- the repository adopts a different maturity model;
- evidence requirements need formal expansion;
- automated validation is added and changes the review process;
- the project begins supporting real deployed environments.

## Related Documents

- [README.md](../../README.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [BLUEPRINT.md](../../BLUEPRINT.md)
- [ROADMAP.md](../../ROADMAP.md)

## Supersedes

None

## Superseded By

None
