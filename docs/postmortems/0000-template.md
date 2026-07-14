# Postmortem: <Incident Title>

> **Template instructions:** This is a reusable template. Replace placeholders and remove instructional text when writing a real postmortem. Do not fabricate incident details, timestamps, metrics, customer impact, or financial impact.

> **Blameless and evidence-based:** This postmortem must focus on systems, processes, decisions, and evidence. It must not blame individuals. No evidence, no implementation.

## Metadata

| Field | Value |
| --- | --- |
| Incident ID | <incident-id> |
| Date | <YYYY-MM-DD> |
| Severity | <severity> |
| Status | <Draft/In Review/Closed> |
| Authors | <author-list> |
| Reviewers | <reviewer-list> |
| Affected capability | <service-name> |
| Start time | <YYYY-MM-DDThh:mm:ssZ> |
| Detection time | <YYYY-MM-DDThh:mm:ssZ> |
| Mitigation time | <YYYY-MM-DDThh:mm:ssZ-or-not-applicable> |
| Recovery time | <YYYY-MM-DDThh:mm:ssZ-or-not-applicable> |

## Executive Summary

Summarize what happened using evidence. Do not include unsupported conclusions.

## Impact

Describe validated impact only. Do not request or invent fabricated customer impact, financial impact, or production impact.

## Detection

Describe how the event was detected and which evidence supports detection.

## Timeline

Use UTC or explicitly identify the timezone.

| Time | Event | Evidence |
| --- | --- | --- |
| <YYYY-MM-DDThh:mm:ssZ> | <event-description> | <repository-relative-link-or-reference> |

## Technical Context

Describe relevant architecture, services, dependencies, and constraints.

## Root Cause

Describe the root cause supported by evidence. If unknown, state what is unknown and why.

## Contributing Factors

List contributing factors supported by evidence.

## What Went Well

List positive response factors supported by evidence.

## What Did Not Go Well

List gaps, delays, missing signals, unclear ownership, or process issues.

## Where We Got Lucky

Describe favorable conditions that reduced impact or risk.

## Resolution

Describe how the event was mitigated or resolved.

## Recovery Validation

Describe how recovery was validated.

## Corrective and Preventive Actions

| Action | Owner | Priority | Due Date | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| <action> | <owner> | <priority> | <YYYY-MM-DD> | <status> | <repository-relative-link-or-none> |

## Lessons Learned

Summarize learnings that should influence future architecture, runbooks, playbooks, monitoring, or training.

## SLO or Monitoring Impact

Describe any validated SLO, alerting, or telemetry impact. Do not fabricate metrics.

## Security Impact

Describe validated security impact or explicitly state when none is known.

## Cost Impact

Describe validated cost impact or explicitly state when none is known. Do not fabricate financial values.

## Related Documents

- <repository-relative-link>

## Approval and Closure

| Reviewer | Role | Decision | Date |
| --- | --- | --- | --- |
| <reviewer> | <role> | <Approved/Changes Requested> | <YYYY-MM-DD> |
