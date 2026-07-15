# ECPEL Diagrams

## Purpose

ECPEL stores diagram sources in the repository so architecture, process, lifecycle, and dependency views can be reviewed through normal documentation changes. Diagrams must support understanding of documented repository intent without implying that infrastructure is deployed.

## Diagram Principles

- Diagrams are documentation, not implementation evidence.
- Diagram sources must be version controlled.
- Diagrams must link to supporting documentation.
- Current-state and target-state diagrams must be clearly distinguished.
- Unsupported implementation details must not be invented.
- Sensitive information must not be committed.
- Diagrams must be updated when their supporting architecture changes.
- The governing principle still applies: **No evidence, no implementation.**

## Diagram Format

The initial ECPEL diagram standard is Mermaid embedded in Markdown.

Mermaid is selected because it is:

- text based;
- version controlled;
- reviewable in Git diffs;
- maintainable as documentation as code;
- renderable by GitHub when supported by the platform and syntax used.

This repository does not claim that every Mermaid feature is supported. Prefer simple `flowchart`, `graph`, and `stateDiagram-v2` syntax.

## Naming Convention

Diagram documents use lowercase kebab-case filenames:

```text
<diagram-topic>.md
```

Empty diagram placeholders are not retained. Add a new diagram file only when it contains supported source content and links to evidence or source documents.

## Status Convention

Each diagram document must identify one of the following representation types:

- **Current repository state** — documents files, relationships, or statuses that exist in the repository.
- **Target conceptual state** — documents intended future architecture or domain organization.
- **Process or lifecycle** — documents status transitions, review flow, or evidence lifecycle.
- **Planned relationship** — documents dependency or sequencing relationships from the roadmap, blueprint, architecture, or ADRs.
- **Deprecated or superseded content** — documents content retained for history but replaced by newer documentation.

A diagram can use established repository statuses such as Planned, In Progress, Designed, Simulated, Validated, Implemented, Operated, Deferred, Deprecated, Proposed, Accepted, Rejected, or Superseded when supported by source documents.

## Diagram Index

| Diagram | Type | Status | Primary Source |
| --- | --- | --- | --- |
| [Repository Document Relationships](repository-document-relationships.md) | Current repository state and documentation relationship | In Progress | [README.md](../../README.md) |
| [Platform Domain Map](platform-domain-map.md) | Target conceptual state | Designed | [BLUEPRINT.md](../../BLUEPRINT.md) |
| [Capability Dependency Map](capability-dependency-map.md) | Planned relationship | Planned | [ROADMAP.md](../../ROADMAP.md) |
| [Evidence and Status Lifecycle](evidence-and-status-lifecycle.md) | Process or lifecycle | Designed | [ROADMAP.md](../../ROADMAP.md) |

## Deferred Diagrams

| Diagram | Status | Reason |
| --- | --- | --- |
| `system-context.md` | Deferred | Current documentation defines target actors and conceptual platform boundaries, but it does not yet define enough external systems and interaction responsibilities for a C4-style context diagram without inventing integrations. |

## Validation

Diagram updates should be reviewed for:

- valid Markdown links;
- properly opened and closed Mermaid code fences;
- simple Mermaid syntax;
- consistency with supporting documents;
- no unsupported implementation claims;
- no sensitive information;
- index entries matching actual diagram files.

Automated Mermaid rendering validation is not currently configured in this repository. Reviewers should perform careful syntax review until validation tooling is introduced.

## Security Restrictions

Do not include:

- credentials;
- secrets;
- tokens;
- private endpoints;
- account IDs;
- personal data;
- customer data;
- sensitive network ranges;
- unapproved internal architecture;
- cloud resource identifiers;
- production topology not supported by repository evidence.
