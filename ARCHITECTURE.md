# ECPEL Target Architecture

ECPEL's target architecture describes the intended shape of an Enterprise Cloud Platform. It is an architectural vision, not a statement of implemented capability.

> **Architecture status:** Target-state guidance only. No cloud account, workload platform, automation pipeline, security control, or operational process should be considered implemented unless supporting artifacts exist in this repository.

## Purpose

This document establishes the architectural direction for the Enterprise Cloud Platform Engineering Lab (ECPEL). It defines platform domains, boundaries, guiding principles, and an evolution path for future architecture work.

The architecture is intentionally evidence-first:

- It may describe target domains and desired interactions.
- It may define design constraints and decision areas.
- It must not claim working infrastructure or deployed services without repository evidence.
- It should guide future ADRs, diagrams, runbooks, playbooks, and implementation artifacts.

## Architectural Vision

The target ECPEL platform is a governed cloud platform that enables product teams to deliver software safely, repeatedly, and cost-consciously. It should provide paved roads for common engineering needs while preserving clear boundaries between platform responsibilities and workload responsibilities.

The long-term vision is a platform that provides:

- governed cloud account and environment foundations;
- identity and access patterns based on least privilege;
- network segmentation and connectivity standards;
- security guardrails and auditability;
- infrastructure delivery patterns with reviewable change control;
- runtime platforms for containerized and service workloads;
- observability and operational readiness patterns;
- cost visibility and financial accountability;
- documentation, runbooks, and decision records that explain how the platform works.

## Current Repository Evidence

The repository currently provides documentation, research, diagrams, ADRs, validated local tooling evidence, and two local-only **Simulated** labs. Planned `platform/**` paths represent target-domain documentation or future implementation locations; no `platform/` directory is currently versioned, and the existence of a planned path is not implementation evidence.

Current evidence supports only these architectural statements:

- ECPEL has a root project README that defines an evidence-first repository philosophy.
- ECPEL has documentation entry points under [docs](docs/README.md).
- ECPEL has substantive ADRs recorded under [docs/adr](docs/adr/README.md), including current deferral ADRs for cloud strategy, GitOps strategy, and primary IaC tool selection.
- ECPEL has version-controlled diagram documents under [docs/diagrams](docs/diagrams/README.md).
- ECPEL has completed market-analysis research artifacts under [docs/market-analysis](docs/market-analysis/README.md), including the 2026 Cloud Market Matrix and its derived roadmap.
- ECPEL has a local-only Terraform learning lab under [labs/terraform-local-foundation](labs/terraform-local-foundation/README.md), classified as **Simulated**.
- The simulated Terraform lab contains local Terraform configuration and a local naming module, but it provisions no cloud resources and does not adopt Terraform as the primary implemented IaC tool.
- ECPEL has a non-destructive GitHub Actions workflow that validates the simulated Terraform lab as a repository regression gate; it is not production deployment automation.
- ECPEL has a local-only static configuration-management lab under [labs/configuration-management/ansible-local-foundation](labs/configuration-management/ansible-local-foundation/README.md), classified as **Simulated** and governed by ADR-0008.
- The simulated Ansible lab has a non-destructive static validation workflow for artifact structure, guardrails, dependency installation, inventory parsing, playbook syntax checks, and linting; it is not production deployment automation and does not execute Ansible functionally.
- ECPEL has a **Validated** development container for GitHub Codespaces and VS Code Dev Containers.
- ECPEL does not currently contain implemented cloud infrastructure, deployed cloud resources, production deployment automation, GitOps automation, a functional Ansible target, or working platform services.

## Architecture Principles

### 1. Evidence before claims

A target architecture may describe intent, but an implemented capability requires repository evidence such as code, configuration, tests, diagrams, runbooks, and validation results.

### 2. Platform as a product

The platform should be designed as a product with clear users, capabilities, service boundaries, documentation, support expectations, and lifecycle management.

### 3. Guardrails over gates

The target platform should prefer reusable paved roads, automated validation, and policy guardrails over manual approval bottlenecks where possible.

### 4. Secure by design

Security controls should be part of the architecture from the start, including identity, least privilege, logging, audit trails, secrets handling, network boundaries, vulnerability management, and incident response.

### 5. Cost-aware by design

Cost visibility, tagging, budgeting, cleanup, forecasting, and ownership should be designed before cloud resources are created.

### 6. Operable by default

A capability is not architecturally complete until monitoring, logging, alerting, runbooks, failure modes, and ownership are understood.

### 7. Clear separation of responsibilities

The architecture should distinguish between platform team responsibilities, workload team responsibilities, security responsibilities, compliance responsibilities, and shared responsibilities.

### 8. Incremental evolution

Architecture should mature through explicit stages: concept, research, design, validation, implementation, and operation.

## Target Platform Domains

The target architecture is organized into platform domains. These domains are architectural boundaries, not implementation claims.

### Cloud foundation and organization

**Target purpose:** Provide the structure for accounts, environments, organizational units, policies, and baseline controls.

**Future architecture concerns:**

- account and environment model;
- separation between sandbox, development, staging, production, and shared services;
- organizational policies and guardrails;
- audit and logging foundations;
- region strategy;
- lifecycle of accounts and environments.

**Planned target locations:**

- `platform/aws-organizations/README.md`
- `platform/landing-zone/README.md`
- `platform/cloud-governance/README.md`
- `docs/diagrams/aws-organizations.mmd`

### Identity and access

**Target purpose:** Define how humans, workloads, automation, and emergency access interact with the platform.

**Future architecture concerns:**

- identity federation;
- role-based and attribute-based access models;
- least privilege boundaries;
- privileged access workflows;
- break-glass access;
- machine identity;
- auditability and access reviews.

**Planned target locations:**

- `platform/identity-center/README.md`
- `docs/runbooks/identity-center.md`

### Networking and connectivity

**Target purpose:** Define connectivity patterns, segmentation, ingress, egress, private access, and network security boundaries.

**Future architecture concerns:**

- VPC and subnet strategy;
- routing boundaries;
- ingress and egress controls;
- private connectivity;
- DNS strategy;
- service-to-service communication;
- network observability;
- shared versus workload-owned networking.

**Planned target locations:**

- `platform/networking/README.md`
- `docs/diagrams/network.mmd`

### Security and compliance

**Target purpose:** Define platform guardrails, security controls, compliance evidence, and risk management practices.

**Future architecture concerns:**

- baseline security controls;
- policy-as-code strategy;
- vulnerability management;
- secret management;
- logging and audit evidence;
- compliance mappings;
- threat modeling;
- incident response integration.

**Planned target locations:**

- `SECURITY.md`
- `platform/security/README.md`
- `platform/compliance/README.md`
- `docs/compliance/README.md`
- `.github/workflows/security.yml`

### Infrastructure as Code and provisioning

**Target purpose:** Define how infrastructure changes are modeled, reviewed, validated, applied, and rolled back.

**Future architecture concerns:**

- module boundaries;
- state management;
- environment promotion;
- plan and apply controls;
- policy checks;
- drift detection;
- rollback procedures;
- destructive action safeguards.

**Planned target locations:**

- `platform/terraform/README.md`
- `docs/runbooks/terraform.md`
- `.github/workflows/terraform.yml`
- `scripts/validate.sh`
- `scripts/destroy.sh`

### Delivery and GitOps

**Target purpose:** Define how application and platform changes move from source control to target environments.

**Future architecture concerns:**

- source-of-truth model;
- pull request validation;
- promotion strategy;
- deployment approvals;
- reconciliation model;
- environment drift;
- rollback and progressive delivery;
- ownership between platform and application teams.

**Planned target locations:**

- `platform/gitops/README.md`
- `platform/devsecops/README.md`
- `docs/adr/0003-defer-gitops-strategy-decision.md`
- `.github/workflows/ci.yml`
- `.github/workflows/release.yml`

### Runtime platforms

**Target purpose:** Define workload hosting patterns for containerized services and future application platforms.

**Future architecture concerns:**

- workload isolation;
- cluster or service boundaries;
- ingress patterns;
- scaling strategy;
- platform add-ons;
- deployment safety;
- runtime security;
- ownership and support model.

**Planned target locations:**

- `platform/eks/README.md`
- `platform/ecs/README.md`
- `docs/runbooks/eks.md`
- `docs/runbooks/ecs.md`

### Observability and operations

**Target purpose:** Define how the platform and workloads expose telemetry, detect failure, and support operations.

**Future architecture concerns:**

- logs, metrics, traces, and events;
- alert routing;
- service-level indicators;
- incident response;
- postmortems;
- game days;
- operational dashboards;
- runbook ownership.

**Planned target locations:**

- `platform/observability/README.md`
- `platform/incidents/README.md`
- `docs/runbooks/README.md`
- `docs/playbooks/incident-response.md`
- `docs/playbooks/postmortem-template.md`
- `docs/game-days/README.md`

### FinOps and cost management

**Target purpose:** Define how the platform makes cost visible, attributable, forecastable, and controllable.

**Future architecture concerns:**

- tagging and ownership model;
- budgets and alerts;
- showback or chargeback;
- cost anomaly detection;
- environment cleanup;
- unit economics;
- cost reporting automation.

**Planned target locations:**

- `platform/finops/README.md`
- `scripts/cost-report.sh`

### Developer experience and enterprise services

**Target purpose:** Define common services and workflows that make platform consumption easier and safer.

**Future architecture concerns:**

- repository standards;
- golden paths;
- templates;
- developer portals;
- quality gates;
- internal service catalog;
- support and escalation paths.

**Planned target locations:**

- `platform/github-enterprise/README.md`
- `platform/sonarqube-enterprise/README.md`
- `platform/enterprise-services/README.md`
- `platform/shared/README.md`

### Data, MLOps, and AI platform

**Target purpose:** Define future boundaries for data, machine learning, and AI platform capabilities without claiming they exist today.

**Future architecture concerns:**

- model development lifecycle;
- experiment tracking;
- model deployment patterns;
- data access boundaries;
- AI governance;
- agent safety and observability;
- cost and capacity management for AI workloads.

**Planned target locations:**

- `platform/mlops/README.md`
- `platform/ai-platform/README.md`
- `platform/ai-agents/README.md`

## Architecture Boundaries

### In scope for the target architecture

The target architecture may cover:

- platform domain definitions;
- cloud foundation models;
- security and compliance guardrails;
- infrastructure delivery patterns;
- runtime platform boundaries;
- operational readiness;
- cost management;
- documentation and decision practices.

### Out of scope until evidence exists

The following remain out of scope as implemented capabilities until the repository contains evidence beyond current documentation, research, local simulation, and regression validation:

- provisioned cloud accounts or resources;
- cloud provisioning modules;
- cloud deployment workflows;
- deployed ECS or EKS platforms;
- active GitOps controllers;
- production deployment, release, or GitOps automation;
- implemented security scanners;
- production incident response processes;
- operating FinOps reports;
- working MLOps or AI platform services.

## Target Interaction Model

The target platform should eventually support interactions among the following actors:

- **Platform team:** designs, operates, and evolves platform capabilities.
- **Application teams:** consume paved roads and deploy workloads within defined guardrails.
- **Security team:** defines security requirements, reviews controls, and consumes audit evidence.
- **Compliance and risk stakeholders:** map controls to requirements and validate evidence.
- **Finance and FinOps stakeholders:** review spend, ownership, forecasts, and optimization opportunities.
- **Operations stakeholders:** use runbooks, telemetry, incident processes, and postmortems.

No current file in the repository proves that these operating interactions are implemented. They are target architecture roles.

## Target Control Planes

Future architecture work should distinguish between several control planes:

1. **Source control plane** — repositories, pull requests, review policies, and change history.
2. **Delivery control plane** — CI/CD, GitOps, artifact promotion, and deployment approvals.
3. **Infrastructure control plane** — provisioning, state management, policy checks, and drift detection.
4. **Security control plane** — identity, policy, secrets, scanning, and audit evidence.
5. **Operations control plane** — telemetry, alerting, incident response, runbooks, and postmortems.
6. **Financial control plane** — budgets, tagging, cost allocation, reporting, and optimization.

These control planes are conceptual architecture boundaries. The repository has a non-destructive Terraform lab validation workflow, but no production delivery, GitOps, release, cloud provisioning, or cloud deployment control plane is currently implemented.

## Documentation Model

Architecture should be supported by a documentation set with clear responsibilities:

- [README](README.md) explains the project foundation and philosophy.
- [docs](docs/README.md) provides documentation navigation.
- [ADRs](docs/adr/README.md) record significant decisions.
- [diagrams](docs/diagrams/README.md) describe architecture visually.
- [runbooks](docs/runbooks/README.md) describe repeatable operational procedures.
- [playbooks](docs/playbooks/README.md) describe incident and disaster-response procedures.
- [market analysis](docs/market-analysis/README.md) records research context.

## Future Architecture Evolution

Architecture should evolve in deliberate stages.

### Stage 1 — Baseline documentation

- Define domain ownership and boundaries.
- Fill foundational architecture, blueprint, and roadmap documents.
- Convert empty placeholders into explicit draft documents or remove them.
- Record initial ADRs for major decisions.

### Stage 2 — Reference designs

- Create diagrams for context, containers, deployment, networking, and organization structure.
- Define environment and account models.
- Define identity, networking, security, and cost control patterns.
- Define runtime platform options and selection criteria.

### Stage 3 — Validation model

- Define how proposed architecture will be reviewed.
- Establish link checks, documentation checks, and future infrastructure validation checks; preserve the existing non-destructive Terraform lab regression workflow as local simulation validation only.
- Define acceptance criteria for moving from target design to implementation.

### Stage 4 — Evidence-backed implementation

- Add implementation artifacts only after the corresponding architecture is documented.
- Pair each implementation with validation, runbooks, cost considerations, and rollback guidance.
- Update this architecture document when evidence changes.

### Stage 5 — Operated platform maturity

- Track operational metrics, incidents, and postmortems.
- Improve guardrails based on evidence.
- Evolve golden paths and platform services based on user feedback.
- Keep architecture synchronized with actual implementation.

## Decision Areas Requiring ADRs

Future ADRs should be used for decisions such as:

- cloud provider and multi-account strategy;
- identity and federation model;
- GitOps and delivery strategy;
- infrastructure state and promotion model;
- network segmentation and connectivity model;
- runtime platform selection;
- observability stack selection;
- security scanning and policy-as-code approach;
- FinOps tagging and reporting model;
- AI and MLOps governance boundaries.

Existing ADR references include:

- `docs/adr/0001-record-architecture-decisions.md`
- `docs/adr/0002-defer-primary-implementation-cloud-decision.md`
- `docs/adr/0003-defer-gitops-strategy-decision.md`
- `docs/adr/0006-defer-primary-infrastructure-as-code-tool-decision.md`

## Risks and Open Questions

Known architecture risks at this foundation stage:

- The repository contains many named domains with limited content, which can create a false impression of maturity.
- Security, compliance, and cost controls are not yet defined.
- Planned workflow and script paths should not be read as current production automation; the existing Terraform lab workflow is only a non-destructive repository regression-validation gate.
- Platform boundaries are conceptual and need continued validation through ADRs and diagrams.
- The repository uses Apache License 2.0; [LICENSE](LICENSE) contains the license terms and [NOTICE](NOTICE) contains project attribution.

Open questions for future architecture work:

- Which cloud provider strategy should ECPEL document first?
- What is the target account and environment model?
- Which capabilities belong to the platform team versus workload teams?
- What level of automation is appropriate before security and cost guardrails exist?
- What evidence is required before a capability can be marked implemented?

## Architecture Review Checklist

Before any future platform capability is described as implemented, reviewers should verify:

- The relevant domain documentation exists.
- An ADR exists for major design decisions.
- Architecture diagrams are updated where appropriate.
- Security and compliance implications are documented.
- Cost impact and cleanup strategy are documented.
- Validation steps are automated or clearly documented.
- Runbooks or playbooks exist for operational use.
- README and documentation links remain accurate.

## Summary

This architecture document defines ECPEL's target platform direction without claiming current implementation. It should be used as a guide for future research, decisions, diagrams, and implementation work. The core rule remains unchanged: **No evidence, no implementation.**
