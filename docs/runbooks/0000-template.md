# Runbook: <Procedure Name>

> **Template instructions:** This is a reusable template. Replace placeholders such as `<service-name>`, `<owner>`, `<YYYY-MM-DD>`, and `<repository-relative-link>`. Remove instructional text when creating a real runbook. Do not claim a procedure is validated without evidence.

> **Principle:** No evidence, no implementation.

## Metadata

| Field | Value |
| --- | --- |
| Status | <Template/Draft/Planned/Simulated/Validated/Deprecated> |
| Owner | <owner> |
| Reviewers | <reviewer-list> |
| Service or capability | <service-name> |
| Environment | <environment> |
| Severity applicability | <severity-or-alert-scope> |
| Last reviewed | <YYYY-MM-DD> |
| Next review | <YYYY-MM-DD> |
| Related SLO or alert | <repository-relative-link-or-none> |
| Related architecture or ADR | <repository-relative-link-or-none> |

## Purpose

Describe the operational task or alert this runbook supports.

## Scope

Define what this runbook covers and what it does not cover.

## Preconditions

List conditions that must be true before the procedure begins.

## Required Access

Describe the minimum access required. Do not include credentials, account IDs, tokens, customer data, or secrets.

## Safety Warnings

List destructive actions, production-impacting steps, cost risks, privacy risks, and stop conditions.

## Inputs

List required inputs such as alert name, service name, environment, ticket, change request, or time range.

## Procedure

Use numbered, verifiable steps.

1. Confirm the affected service or capability: `<service-name>`.
2. Confirm the environment: `<environment>`.
3. Record the start time in ISO 8601 format: `<YYYY-MM-DDThh:mm:ssZ>`.
4. Execute the next diagnostic step and record evidence: `<evidence-location>`.
5. Continue only if safety warnings and access requirements are satisfied.

## Validation

Define how the operator confirms success. Separate planned validation from evidence captured during execution.

## Rollback

Describe how to reverse the change or stop the procedure safely.

## Recovery

Describe how to restore the service or capability after failure.

## Escalation

Describe when and how to escalate without assigning fictional people.

## Observability

Document relevant logs, metrics, traces, dashboards, and alarms.

| Signal Type | Location | Expected Evidence |
| --- | --- | --- |
| Logs | <repository-relative-link-or-system-reference> | <expected-log-evidence> |
| Metrics | <repository-relative-link-or-system-reference> | <expected-metric-evidence> |
| Traces | <repository-relative-link-or-system-reference> | <expected-trace-evidence> |
| Dashboards | <repository-relative-link-or-system-reference> | <expected-dashboard-evidence> |
| Alarms | <repository-relative-link-or-system-reference> | <expected-alarm-evidence> |

## Security Considerations

Document access, data handling, least privilege, audit, and privacy considerations.

## Cost Considerations

Document cost risks, resource creation risks, cleanup needs, and cost evidence to capture.

## Troubleshooting

| Symptom | Possible Cause | Diagnostic Step | Corrective Action |
| --- | --- | --- | --- |
| <symptom> | <possible-cause> | <diagnostic-step> | <corrective-action> |

## Evidence to Capture

List evidence that should be attached to a ticket, postmortem, change request, or repository artifact.

## Related Documents

- <repository-relative-link>

## Revision History

| Date | Author | Change | Evidence |
| --- | --- | --- | --- |
| <YYYY-MM-DD> | <owner> | Initial draft | <repository-relative-link-or-none> |
