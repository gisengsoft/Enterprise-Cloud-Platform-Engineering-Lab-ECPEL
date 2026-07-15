# Runbooks

Runbooks define repeatable operational procedures for known services, capabilities, alerts, or maintenance activities.

A runbook is procedural: it tells an operator exactly what to check, what commands or consoles may be used, what evidence to capture, how to validate success, and when to escalate. A runbook does not prove that a capability is implemented.

> **Principle:** No evidence, no implementation.

## When a runbook is required

Create a runbook when a future ECPEL capability has or expects:

- repeatable operational tasks;
- alerts requiring a documented response;
- routine maintenance or validation procedures;
- recovery, rollback, or escalation procedures;
- access-sensitive operational steps;
- cost, security, or reliability implications.

## Runbook vs. playbook

| Document type | Purpose |
| --- | --- |
| Runbook | Step-by-step procedure for a known operational task or alert. |
| Playbook | Coordinated response plan for a broader scenario, incident class, or event. |

Runbooks are usually executed by operators. Playbooks coordinate people, roles, communication, containment, investigation, and recovery.

## Naming convention

Use lowercase kebab-case filenames:

```text
<service-or-capability>.md
```

Use `0000-template.md` only as the reusable template. Do not create real runbooks in this PR.

## Ownership expectations

Every runbook should identify:

- owner;
- reviewers;
- service or capability;
- environment;
- review dates;
- related alerts, SLOs, architecture documents, or ADRs.

## Review frequency

Runbooks should be reviewed:

- at least quarterly for operationally critical capabilities;
- after incidents or postmortems that reveal procedure gaps;
- after architecture, ownership, alerting, or access changes;
- before claiming a capability is operated.

## Validation expectations

A runbook must define how the operator confirms success. Validation should distinguish:

- planned procedure steps;
- simulated validation;
- evidence captured from real operation;
- unresolved assumptions.

## Status model

Allowed runbook statuses:

- **Template** — reusable format only;
- **Draft** — incomplete and not validated;
- **Planned** — expected future procedure, not executable yet;
- **Simulated** — exercised only in a labeled simulation;
- **Validated** — tested against supporting evidence;
- **Deprecated** — no longer recommended.

## Required evidence

A runbook should reference evidence such as:

- related ADRs;
- architecture or blueprint documents;
- alert definitions;
- logs, metrics, traces, dashboards, or alarms;
- validation output;
- postmortems or playbooks;
- repository-relative links to implementation artifacts when they exist.

Do not include real credentials, account IDs, customer data, or sensitive information.

## Indexing approach

Add future runbooks to this index only when they exist as files.

| Runbook | Purpose | Status |
| --- | --- | --- |
| [0000-template.md](0000-template.md) | Reusable runbook template | Template |
