# Postmortems

Postmortems are blameless, evidence-based learning documents for incidents, significant operational events, or exercises.

They explain what happened, why it happened, what evidence supports the analysis, and which corrective or preventive actions will reduce future risk.

> **Principle:** No evidence, no implementation.

## Blameless principles

Postmortems should:

- focus on systems, processes, signals, and decisions;
- avoid blaming individuals;
- use evidence instead of assumptions;
- identify actionable improvements;
- document unknowns honestly;
- protect sensitive information.

## When a postmortem is required

Create a postmortem after:

- a major incident;
- a significant reliability or security event;
- a failed change or recovery attempt;
- a game day that produces important findings;
- a near miss with meaningful risk;
- any event where learning should be preserved.

## Expected participants

Participants may include role types such as incident commander, technical lead, service owner, communications lead, security reviewer, SRE reviewer, or compliance reviewer. Do not include private personal data unless appropriate for the repository context.

## Evidence requirements

Postmortems should reference evidence such as:

- timeline entries;
- logs, metrics, traces, alerts, or dashboards;
- related runbooks and playbooks;
- incident tickets or change records;
- validation records;
- screenshots only when permitted and sanitized.

Do not fabricate incident timestamps, customer impact, financial impact, monitoring data, or outcomes.

## Handling sensitive information

Do not commit credentials, account IDs, customer data, personal data, secrets, private incident data, or confidential enterprise details.

## Action-item ownership

Every corrective or preventive action should have:

- owner;
- priority;
- due date;
- status;
- evidence or closure link.

## Closure criteria

A postmortem is ready for closure when:

- evidence has been reviewed;
- root cause and contributing factors are documented or explicitly unknown;
- action items have owners;
- sensitive data has been removed;
- reviewers have signed off.

## Review process

Postmortems should be reviewed by relevant technical, operational, security, and business stakeholders. Closure should not imply production maturity unless supporting evidence exists.

## Index

| Document | Purpose | Status |
| --- | --- | --- |
| [0000-template.md](0000-template.md) | Reusable postmortem template | Template |
