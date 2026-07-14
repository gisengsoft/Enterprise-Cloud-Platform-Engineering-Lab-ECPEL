# Playbooks

Playbooks define coordinated response plans for operational scenarios, incident classes, exercises, or multi-step recovery events.

A playbook coordinates roles, communication, containment, investigation, mitigation, recovery, validation, and follow-up. It is scenario-oriented rather than task-oriented.

> **Principle:** No evidence, no implementation.

## When playbooks are used

Use playbooks for:

- incident response scenarios;
- disaster recovery scenarios;
- security events;
- major operational degradation;
- coordinated recovery activities;
- game-day preparation;
- communication-heavy events.

## Playbook vs. runbook

| Document type | Purpose |
| --- | --- |
| Playbook | Coordinates people, roles, decisions, communications, and scenario flow. |
| Runbook | Provides exact procedural steps for a known task, alert, or capability. |

A playbook may link to one or more runbooks.

## Relationship with incident response

Incident response playbooks should define how an event is assessed, contained, investigated, mitigated, recovered, communicated, and reviewed. They do not replace postmortems or evidence collection.

## Ownership

Every playbook should identify an owner, reviewers, role expectations, review cadence, and related runbooks or architecture documents.

## Review and exercise expectations

Playbooks should be reviewed:

- after incidents or exercises;
- before planned game days;
- after ownership, architecture, or severity model changes;
- at least semi-annually for critical scenarios.

Exercise results must not be fabricated. Simulated exercises must be clearly labeled as simulated.

## Status and lifecycle

Allowed playbook statuses:

- **Template** — reusable format only;
- **Draft** — incomplete and not exercised;
- **Planned** — expected scenario response, not validated;
- **Simulated** — exercised in a controlled simulation;
- **Validated** — supported by evidence from review or exercise;
- **Deprecated** — no longer recommended.

## Index

| Playbook | Purpose | Status |
| --- | --- | --- |
| [0000-template.md](0000-template.md) | Reusable playbook template | Template |
| [disaster-recovery.md](disaster-recovery.md) | Disaster recovery playbook placeholder | Placeholder |
| [incident-response.md](incident-response.md) | Incident response playbook placeholder | Placeholder |
| [postmortem-template.md](postmortem-template.md) | Legacy postmortem template placeholder | Placeholder |
