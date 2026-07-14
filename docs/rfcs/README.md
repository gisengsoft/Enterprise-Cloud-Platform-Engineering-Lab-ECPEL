# Requests for Comments

Requests for Comments (RFCs) are structured proposals for design, process, operational, or implementation changes that need review before a decision is made.

An RFC proposes and evaluates options. An ADR records a decision after review.

> **Principle:** No evidence, no implementation.

## When an RFC is required

Create an RFC for proposals that:

- affect multiple platform domains;
- introduce new tools or workflows;
- change architecture, roadmap, governance, or operating model assumptions;
- require security, cost, reliability, or compliance review;
- need stakeholder feedback before an ADR or implementation.

## RFC vs. ADR

| Document type | Purpose |
| --- | --- |
| RFC | Explores a proposal, alternatives, tradeoffs, risks, and open questions. |
| ADR | Records an accepted, rejected, superseded, deprecated, or deferred decision. |

An accepted RFC may lead to an ADR. An RFC does not by itself implement anything.

## RFC lifecycle

Allowed RFC statuses:

- **Draft** — proposal is being written;
- **In Review** — proposal is ready for feedback;
- **Accepted** — proposal is approved to proceed or produce ADRs;
- **Rejected** — proposal will not proceed;
- **Withdrawn** — proposal was removed by authors;
- **Superseded** — replaced by a newer RFC.

## Review expectations

RFCs should identify authors, reviewers, review date, open questions, risks, validation plan, and related documents. Security, operations, cost, and reliability impacts should be addressed before acceptance.

## Acceptance and rejection process

Acceptance means the proposal is approved as a direction or input to an ADR. Rejection means the proposal should not proceed as written. Neither status proves implementation.

## Relationship with implementation work

Implementation work should not begin from an RFC alone when an ADR, roadmap update, runbook, playbook, or validation plan is required. Implementation claims still require repository evidence.

## Relationship with ADRs

Major accepted RFCs should link to resulting ADRs. ADRs should link back to relevant RFCs when an RFC informed the decision.

## Index

| RFC | Purpose | Status |
| --- | --- | --- |
| [0000-template.md](0000-template.md) | Reusable RFC template | Template |
