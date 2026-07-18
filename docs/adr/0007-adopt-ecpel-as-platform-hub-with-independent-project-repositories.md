# ADR-0007: Adopt ECPEL as Platform Hub with Independent Project Repositories

## Status

Proposed

## Date

YYYY-MM-DD

## Deciders

- ECPEL maintainer

## Consulted

- None at proposal time

## Informed

- ECPEL contributors

## Context

ECPEL is the repository responsible for platform architecture, standards,
controlled environments, platform automation, operational practices, and
evidence requirements.

The broader portfolio also contains independent reference-workload
candidates, blueprints, prototypes, specialized laboratories, and Data
and AI projects. These repositories have their own source code, tests,
release cycles, internal decisions, evidence, and limitations.

Without an explicit repository-topology decision, future work could create
duplicated sources of truth, import project-specific ADRs into the wrong
scope, or present external evidence as proof of ECPEL implementation.

Current examples include TaskGuard as a reference-workload candidate,
Aurora as a blueprint and prototype family, SRE Platform Lab as a source
of operational practices, and Enterprise Cloud Governance Lab as a
specialized laboratory. These examples are not an exhaustive project
catalog.

## Decision Drivers

- Preserve clear ownership and sources of truth.
- Keep platform concerns separate from application concerns.
- Prevent external evidence from being inherited without ECPEL validation.
- Avoid premature monorepository consolidation.
- Allow independent project releases and lifecycles.
- Avoid choosing an integration mechanism before a concrete requirement
  exists.
- Remain consistent with the evidence rule established by ADR-0004.

## Considered Options

### Monorepository containing all projects

Not selected because the projects have different scopes, technology
stacks, release cycles, internal ADRs, and evidence levels. There is no
current requirement for frequent atomic changes across all projects.

### ECPEL as hub with independent project repositories

Selected because it preserves project autonomy while establishing clear
platform, integration, and evidence boundaries.

### Manual copying between repositories

Not selected as the default because it creates duplicated sources of
truth and loses provenance. Selective adaptation remains possible when
ownership, origin, review, and ECPEL validation are explicit.

### Git submodules

Deferred because no current integration requires nested repository
checkouts and the contributor and CI complexity is not yet justified.

### Git subtree

Deferred because no current requirement justifies duplicating and
synchronizing external project content inside ECPEL.

### Informal links without an architectural decision

Not selected because links alone do not define ownership, integration
responsibility, or evidence boundaries.

## Decision

ECPEL will act as the platform hub and source of truth for:

- platform standards and reusable patterns;
- environments controlled by ECPEL;
- platform automation and integration;
- integration of approved reference workloads;
- shared observability and operational practices when implemented;
- platform runbooks;
- minimum integration contracts;
- ECPEL evidence criteria and indexes.

Independent project repositories will remain the source of truth for
their own:

- source code;
- tests;
- dependencies and build definitions;
- functional documentation;
- internal ADRs;
- releases and versions;
- project-specific evidence and limitations.

Project-specific ADRs do not automatically govern ECPEL.

Evidence from another repository does not automatically prove that a
project is integrated, implemented, cloud validated, or operated by
ECPEL.

A future ECPEL integration must identify at minimum:

- the referenced project and version;
- project and platform ownership;
- the integration boundary;
- reviewed ECPEL-side integration artifacts;
- ECPEL-side validation evidence.

Reuse may occur through references, identifiable versions, selective
adaptation, or separately reviewed ECPEL implementations.

No project will be imported in full as a consequence of this ADR.

This ADR does not select Git submodules, Git subtree, synchronization,
catalog tooling, registries, contract formats, deployment manifests, or
cross-repository automation.

## Consequences

### Positive consequences

- Platform and application responsibilities remain separate.
- Independent projects retain their own histories and release cycles.
- External ADRs cannot silently become ECPEL decisions.
- External evidence cannot silently become ECPEL implementation evidence.
- Workloads and patterns can be evaluated without moving their complete
  repositories.
- Future integration mechanisms can evolve without changing the logical
  repository ownership model.

### Negative consequences

- Cross-repository changes may require coordinated Pull Requests.
- References to external versions can become outdated.
- Integration evidence may be distributed across repositories.
- Contributors must understand both project-owned and ECPEL-owned
  responsibilities.

### Neutral consequences

- Existing repositories and files are not moved or renamed.
- No project becomes integrated or reference ready through this decision.
- The number and location of current repositories remain unchanged.

## Risks

- ECPEL could become only a documentation aggregator without executable
  integrations.
- Application and platform repositories could create conflicting
  deployment artifacts.
- External validation could be overstated as ECPEL validation.
- ECPEL could gradually accumulate application-specific code and become
  an unplanned monorepository.

These risks must be controlled through explicit ownership, reviewed
integration boundaries, immutable references where practical, and
ECPEL-side validation under ADR-0004.

## Validation

Future integrations governed by this ADR must demonstrate that:

- the external project and version are identifiable;
- project and ECPEL ownership are documented;
- the integration boundary is explicit;
- ECPEL-owned integration artifacts are reviewed;
- ECPEL-side validation exists;
- external evidence is not presented as stronger ECPEL evidence;
- no complete project import occurs without a separate architectural
  decision.

This ADR itself creates no integration or implementation.

## Related Documents

- [ADR-0001: Record Architecture Decisions](0001-record-architecture-decisions.md)
- [ADR-0004: Adopt Evidence-Driven Implementation Rule](0004-adopt-evidence-driven-implementation-rule.md)

This ADR complements ADR-0001 and ADR-0004.

It does not modify ADR-0002, ADR-0003, ADR-0005, or ADR-0006.

## Supersedes

None.

## Superseded By

None.
