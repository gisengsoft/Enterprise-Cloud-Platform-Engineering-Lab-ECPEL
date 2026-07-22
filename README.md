# Enterprise Cloud Platform Engineering Lab (ECPEL)

ECPEL is a learning and portfolio repository for designing an enterprise-grade cloud platform engineering foundation. Its purpose is to document architecture, operating models, decision records, and future implementation boundaries for cloud platform work without claiming capabilities that are not present in the repository.

> **Repository philosophy:** No evidence, no implementation.

## Project Overview

This repository is the project foundation for an enterprise cloud platform engineering lab. It is organized around the disciplines commonly required to design, govern, operate, and evolve a cloud platform, including architecture, market analysis, platform domains, runbooks, playbooks, security, compliance, FinOps, and delivery workflows.

At the current stage, ECPEL is documentation-first. It does not include implemented cloud infrastructure, deployed services, production automation, or completed labs. The repository includes two local-only **Simulated** labs: Terraform Local Foundation and Ansible Local Foundation. Both labs have GitHub-hosted static artifact validation, and neither lab provisions cloud resources. The Ansible lab has not been executed functionally and remains static configuration-management scaffolding only. Any future capability must be backed by files, decisions, tests, and documentation in this repository before it is described as implemented.

## Vision

ECPEL aims to become a transparent, evidence-driven reference for enterprise cloud platform engineering. The long-term vision is to show how a platform team can move from research and architectural intent to governed, secure, cost-aware, and operable cloud capabilities.

The repository should help answer practical engineering questions such as:

- What problem is the platform solving?
- Which capabilities are planned, researched, designed, or implemented?
- What decisions have been made, and why?
- What operational procedures exist?
- What security, compliance, and cost controls are documented?
- What evidence proves that a capability exists?

## Philosophy

ECPEL follows a strict evidence-based philosophy:

- **No evidence, no implementation.** A capability is not considered implemented unless supporting artifacts exist in the repository.
- **Documentation before claims.** The repository may describe intent, scope, and planned work, but it must not present unbuilt systems as working systems.
- **Architecture must be traceable.** Design decisions should be captured in ADRs, diagrams, blueprints, and implementation artifacts when they exist.
- **Operations are part of the product.** Runbooks, playbooks, validation, incident response, cost controls, and rollback procedures are first-class concerns.
- **Security and cost are design constraints.** Security, compliance, and FinOps should be considered before infrastructure is created.
- **Prefer clarity over breadth.** A small amount of accurate documentation is more valuable than a large structure that overstates maturity.

## Engineering Principles

ECPEL should evolve according to the following engineering principles:

1. **Evidence-driven delivery** — every implemented claim must be backed by repository artifacts.
2. **Incremental maturity** — work should move through clear stages: proposed, researched, designed, validated, implemented, operated.
3. **Secure by design** — identity, access, secrets, auditability, and least privilege should be defined before deployment.
4. **Cost-aware by design** — budgets, tagging, cleanup, and cost reporting should be planned before resources are created.
5. **Operational readiness** — capabilities should include runbooks, failure modes, validation, and ownership before being treated as usable.
6. **Automation with guardrails** — automation should include validation, approvals, and safeguards appropriate to its blast radius.
7. **Reproducibility** — future labs and platform components should be repeatable from documented source artifacts.
8. **Separation of concerns** — research, architecture, operations, workflows, and platform implementation should remain clearly separated.

## Design Principles

Future ECPEL designs should follow these principles:

- **Explicit status labels** for planned, draft, validated, and implemented work.
- **Decision records for major choices** such as cloud provider strategy, GitOps strategy, identity model, and platform boundaries.
- **Clear platform domains** such as identity, networking, security, compliance, observability, FinOps, and workload orchestration.
- **Documented interfaces** between platform teams, application teams, security teams, and operations teams.
- **Fail-safe operational procedures** for destructive actions, incident response, disaster recovery, and rollback.
- **Minimal claims** until implementation artifacts exist.

## Repository Structure

```text
.
├── docs/                    # Documentation, research, ADRs, templates, diagrams, and compliance guidance
│   ├── adr/                 # Architecture Decision Records
│   ├── compliance/          # Compliance documentation and evidence template
│   ├── diagrams/            # Version-controlled diagram documents
│   ├── game-days/           # Game-day guidance and template
│   ├── market-analysis/     # Completed 2026 Cloud Market Matrix, derived roadmap, and market-analysis index
│   ├── playbooks/           # Operational playbook guidance and template
│   ├── postmortems/         # Postmortem guidance and template
│   ├── rfcs/                # Request-for-comments guidance and template
│   └── runbooks/            # Operational runbook guidance and template
├── labs/                    # Evidence-scoped local-only Simulated labs for Terraform and Ansible
├── ARCHITECTURE.md          # Root architecture entry point
├── BLUEPRINT.md             # Root blueprint entry point
├── ROADMAP.md               # Root roadmap entry point
└── README.md                # Project foundation and navigation
```

## Documentation

Primary documentation entry points:

- [Documentation index](docs/README.md)
- [Market analysis](docs/market-analysis/README.md)
- [2026 Cloud Market Matrix research artifact](docs/market-analysis/2026-cloud-market-matrix.md)
- [Roadmap from market analysis](docs/market-analysis/roadmap-from-market.md)
- [Architecture Decision Records](docs/adr/README.md)
- [Runbooks](docs/runbooks/README.md)
- [Playbooks](docs/playbooks/README.md)
- [Compliance](docs/compliance/README.md)
- [Diagrams](docs/diagrams/README.md)
- [Labs](labs/README.md)

Supporting project files:

- [Architecture overview](ARCHITECTURE.md)
- [Blueprint](BLUEPRINT.md)
- [Roadmap](ROADMAP.md)

Governance documents now provide repository contribution and review expectations:

- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Changelog](CHANGELOG.md)

The repository uses the Apache License 2.0; [LICENSE](LICENSE) contains the license terms and [NOTICE](NOTICE) contains project attribution.

## Roadmap

The roadmap is intentionally conservative. Items below describe intended maturity stages, not implemented capabilities.

### Stage 0 — Foundation

- Establish repository philosophy and documentation standards.
- Create a clear README and documentation navigation.
- Identify empty placeholders and avoid claiming implementation.
- Maintain the completed market-analysis research artifacts and derived roadmap without treating research as implementation evidence.

### Stage 1 — Research and discovery

- Capture market analysis and enterprise requirements.
- Document target users and stakeholder needs.
- Record architectural assumptions and constraints.
- Draft ADRs for major decisions.

### Stage 2 — Architecture and operating model

- Define platform domain boundaries.
- Document identity, networking, security, compliance, FinOps, and observability models.
- Create diagrams and runbook/playbook templates.
- Define validation and acceptance criteria.

### Stage 3 — Evidence-backed implementation

- Add infrastructure or automation only when it is intentionally designed, reviewed, and validated.
- Pair each implementation with documentation, tests, validation, cost considerations, and rollback guidance.
- Mark capabilities as implemented only after evidence exists in the repository.

## Technology Scope

The repository currently names several technology and practice areas as future or research domains. These names do not indicate implementation.

| Area | Current repository status |
| --- | --- |
| AWS Organizations | Mentioned in documentation only; not implemented |
| Identity Center | Mentioned in documentation only; not implemented |
| Landing zone | Mentioned in documentation only; not implemented |
| Terraform | A local-only learning lab exists and is classified as **Simulated**; Terraform has not been adopted as the repository's primary implemented Infrastructure as Code tool, and no cloud infrastructure is provisioned |
| Ansible | A local-only static configuration-management foundation lab exists and is classified as **Simulated** under ADR-0008; GitHub-hosted static artifact validation has passed, but Ansible has not been executed functionally or in check mode |
| EKS | Mentioned in documentation only; not implemented |
| ECS | Mentioned in documentation only; not implemented |
| GitOps | Mentioned in documentation only; not implemented |
| DevSecOps | Mentioned in documentation only; not implemented |
| Observability | Mentioned in documentation only; not implemented |
| FinOps | Mentioned in documentation only; not implemented |
| MLOps and AI platform | Mentioned in documentation only; not implemented |
| GitHub Enterprise | Mentioned in documentation only; not implemented |
| SonarQube Enterprise | Mentioned in documentation only; not implemented |

## Current Status

ECPEL is in the **initial foundation** stage.

Current evidence in the repository supports the following statements:

- The repository structure exists.
- Documentation entry points exist for architecture, roadmap, blueprint, ADRs, diagrams, operational templates, compliance, market analysis, and labs.
- Completed market-analysis research artifacts exist, including the 2026 Cloud Market Matrix and the derived market-analysis roadmap.
- Two local-only **Simulated** labs exist: Terraform Local Foundation and Ansible Local Foundation.
- GitHub-hosted static artifact validation exists for both local-only Simulated labs.
- The Terraform workflow is a repository regression gate and is not production deployment automation.
- The Ansible workflow is non-destructive static artifact validation and is not production deployment automation.
- A validated development container exists for GitHub Codespaces and VS Code Dev Containers.
- `labs/configuration-management/ansible-local-foundation/scripts/preflight-target.sh` is a read-only future-target preflight utility; it checks target prerequisites only and does not implement WSL lifecycle automation or functional Ansible execution.
- No cloud or platform infrastructure is implemented.
- No cloud resources are provisioned by this repository.
- No production capability should be considered implemented yet.

## Project Goals

ECPEL's goals are to:

- Build an honest, evidence-backed cloud platform engineering reference.
- Document research, decisions, architecture, and operating models before implementation.
- Make capability maturity visible and auditable.
- Provide a safe place to develop enterprise platform patterns without overstating readiness.
- Treat security, compliance, operations, and cost management as core design requirements.

## Contributing

Contributions should preserve the repository philosophy: **No evidence, no implementation.**

Before adding or changing content:

1. Be explicit about whether the work is proposed, researched, designed, validated, or implemented.
2. Do not describe a capability as implemented unless supporting artifacts exist.
3. Keep documentation links valid.
4. Include operational, security, and cost considerations when proposing platform capabilities.
5. Prefer small, reviewable changes with clear evidence.

See the [Contributing guide](CONTRIBUTING.md) for contribution workflow, Pull Request expectations, validation guidance, status terminology, security requirements, cost awareness, and documentation standards.

## License

Unless otherwise noted, the contents of this repository are licensed under the Apache License, Version 2.0.

See [LICENSE](LICENSE) for the complete license terms and [NOTICE](NOTICE) for copyright attribution.

Copyright 2026 Gilson Inácio da Silva (gisengsoft).
