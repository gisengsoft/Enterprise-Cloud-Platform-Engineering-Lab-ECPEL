# Compliance Documentation

Compliance documentation in ECPEL is educational and evidence-oriented. ECPEL does not claim formal certification.

> **Principle:** No evidence, no implementation.

## Certification disclaimer

ECPEL does not claim PCI, SOX, SOC 2, ISO 27001, LGPD, GDPR, HIPAA, FedRAMP, or any other formal certification or regulatory attestation.

Compliance documents in this repository may describe educational, planned, or simulated control scenarios. They are not audit reports, certification evidence, or proof of operating effectiveness unless explicitly supported by validated evidence.

## Control design vs. operating effectiveness

| Concept | Meaning |
| --- | --- |
| Control design | How a control is intended to work. |
| Control operating effectiveness | Evidence that a control operated as intended over a defined period. |

A designed control is not the same as a validated control. Simulated evidence must be labeled as simulated.

## Evidence handling

Compliance evidence should:

- use repository-relative links when possible;
- identify evidence owner and reviewer;
- identify evidence period and collection date;
- distinguish planned, documented, simulated, implemented, and validated states;
- avoid unsupported compliance claims;
- expire or require review after a defined date.

## Sensitive-data restrictions

Do not commit:

- credentials or secrets;
- account IDs;
- customer data;
- personal data;
- private enterprise evidence;
- confidential audit findings;
- screenshots containing sensitive information.

## Ownership and review expectations

Each evidence record should include an owner, reviewer, evidence period, classification, and review date. Reviewers should verify that evidence is sanitized, scoped, and accurately labeled.

## Status labels

Allowed compliance evidence statuses:

- **Planned** — control or evidence is expected but not documented;
- **Documented** — control design is described;
- **Simulated** — evidence is produced by a clearly labeled simulation;
- **Implemented** — implementation artifacts exist;
- **Validated** — evidence supports operation over the stated period;
- **Not Applicable** — control does not apply to the stated scope.

## Simulation requirements

Simulated compliance evidence must:

- be labeled **Simulated**;
- avoid claiming certification or operating effectiveness;
- explain simulation scope and limitations;
- avoid real sensitive data;
- link to related runbooks, playbooks, ADRs, RFCs, or architecture documents where applicable.

## Index

| Document | Purpose | Status |
| --- | --- | --- |
| [evidence-template.md](evidence-template.md) | Reusable compliance evidence record template | Template |
