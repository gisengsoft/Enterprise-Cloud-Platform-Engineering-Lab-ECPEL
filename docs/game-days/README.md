# Game Days

Game days are controlled resilience exercises designed to test assumptions, operational readiness, observability, response coordination, and recovery procedures.

Game days must be planned, authorized, bounded, and evidence-based. No game day may be described as executed without real evidence.

> **Principle:** No evidence, no implementation.

## Purpose

Game days help ECPEL evaluate future reliability and operational practices through safe, controlled exercises. They should reveal gaps in runbooks, playbooks, observability, ownership, and recovery procedures.

## Prerequisites

Before a game day is executed, define:

- objective and hypothesis;
- affected systems or capabilities;
- required approvals;
- participants and roles;
- safety controls;
- blast radius;
- stop conditions;
- rollback or recovery procedures;
- telemetry and evidence requirements.

## Safety and authorization requirements

Game days must not be run without authorization from the appropriate owners. Exercises that could affect real systems, costs, users, data, or security require explicit approval and documented stop conditions.

## Blast-radius control

Every game day should limit scope by environment, service, account, region, traffic, data classification, or simulation boundary. Simulated exercises must be labeled as simulated.

## Stop conditions

Stop conditions should define when the exercise must pause or end, including unexpected impact, cost risk, security risk, missing telemetry, unclear ownership, or failed recovery.

## Evidence collection

Game days should capture planned and observed behavior, telemetry, decisions, timelines, recovery evidence, findings, and improvement actions. Do not fabricate outcomes.

## Relationship with SRE and incident management

Game days support SRE, incident response, postmortems, and operational excellence. Findings may lead to runbook updates, playbook updates, monitoring improvements, ADRs, RFCs, or roadmap changes.

## Review and follow-up process

After a real or simulated game day, complete a review, document findings, assign improvement actions, and link related evidence.

## Index

| Game Day | Purpose | Status |
| --- | --- | --- |
| [0000-template.md](0000-template.md) | Reusable game-day template | Template |
| [game-day-001.md](game-day-001.md) | Game-day placeholder | Placeholder |
| [game-day-002.md](game-day-002.md) | Game-day placeholder | Placeholder |
| [game-day-003.md](game-day-003.md) | Game-day placeholder | Placeholder |
