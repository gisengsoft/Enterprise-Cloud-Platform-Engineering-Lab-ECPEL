# ECPEL Roadmap

This roadmap defines the long-term evolution of the Enterprise Cloud Platform Engineering Lab (ECPEL). It is a planning document, not an implementation report.

> **Governing principle:** No evidence, no implementation.

A phase, capability, lab, workflow, control, or platform domain must not be described as implemented unless supporting evidence exists in this repository.

## 1. Purpose

The purpose of this roadmap is to provide a disciplined path for evolving ECPEL from a documentation-first foundation into an evidence-backed enterprise cloud platform engineering project.

This roadmap is intended to:

- align future work with the repository philosophy in [README.md](README.md);
- support the target architecture described in [ARCHITECTURE.md](ARCHITECTURE.md);
- define maturity stages before implementation claims are made;
- establish dependencies between documentation, validation, infrastructure, operations, security, and cost controls;
- make it clear which capabilities are planned, in progress, implemented, simulated, or deferred.

## 2. Guiding Principles

### Evidence before implementation claims

Implementation status requires repository evidence. Examples of evidence include code, configuration, validation output, tests, diagrams, runbooks, ADRs, and documented operating procedures.

### Documentation before automation

Architecture, scope, assumptions, risks, and exit criteria should be documented before automation or infrastructure is added.

### Security and cost before scale

Identity, least privilege, auditability, tagging, budgets, cleanup, and cost visibility should be considered before creating cloud resources or long-running services.

### Operations before production language

A capability should not be described with production-ready language unless runbooks, ownership, observability, failure modes, and recovery procedures exist.

### Incremental maturity

Each phase should move ECPEL through a clear maturity progression rather than jumping directly to complex platform claims.

### Explicit non-implementation

If a domain exists only as a directory, README, placeholder, or target architecture statement, it remains unimplemented.

## 3. Repository Maturity Model

Repository maturity describes the quality and completeness of repository evidence, not the maturity of any external cloud environment.

| Level | Name | Meaning | Evidence examples |
| --- | --- | --- | --- |
| 0 | Placeholder | A file or directory exists but contains no substantive content. | Empty README, empty workflow, empty script |
| 1 | Described | Purpose, scope, and constraints are documented. | README, roadmap, architecture overview |
| 2 | Designed | Architecture and decisions are documented with boundaries and tradeoffs. | ADRs, diagrams, design docs |
| 3 | Validated | Static checks, tests, or review criteria exist and can be run. | Link checks, linting, validation scripts, policy checks |
| 4 | Implemented | Working artifacts exist and are supported by validation evidence. | IaC modules, workflows, scripts, manifests, tests |
| 5 | Operated | Operational procedures and feedback loops exist. | Runbooks, playbooks, SLOs, postmortems, cost reports |
| 6 | Optimized | Evidence is used to improve reliability, cost, security, and developer experience. | Trend analysis, improvements, governance metrics |

Current repository maturity is primarily between **Level 1 — Described** and early **Level 2 — Designed** for project-level documentation. Platform capabilities remain below implementation maturity unless future evidence is added.

## 4. Implementation Status Model

Every future roadmap item should use one of the following statuses.

| Status | Definition | Required evidence |
| --- | --- | --- |
| Planned | Intended future work with no active implementation evidence. | Roadmap entry or issue reference |
| In Progress | Work has started but is not complete or validated. | Draft documentation, partial artifacts, open PRs |
| Implemented | Working artifacts exist and satisfy documented exit criteria. | Code/configuration, validation, docs, runbooks as applicable |
| Simulated | The repository contains a safe mock, local-only exercise, or non-production demonstration. | Clearly labeled simulation artifacts and instructions |
| Deferred | Work is intentionally postponed or blocked. | Roadmap note explaining why and what must change |

### Current implementation status

At the time this roadmap is introduced:

- Project documentation foundation: **In Progress**
- Target architecture documentation: **In Progress**
- Roadmap documentation: **In Progress**
- Infrastructure implementation: **Planned**
- CI/CD implementation: **Planned**
- Runtime platforms: **Planned**
- Security automation: **Planned**
- Cost automation: **Planned**
- AI and MLOps platform capabilities: **Planned**

No roadmap phase is currently marked **Implemented**. Current provider and tooling boundaries are unchanged: Microsoft Azure is not adopted, AWS is not adopted, Google Cloud is not adopted, no cloud provider is adopted, no primary IaC tool is adopted, the Terraform local lab remains **Simulated**, Terraform validation is not deployment automation, and no cloud infrastructure is implemented.

## 5. Dependency Rules

These dependency rules govern phase progression.

1. **Architecture before infrastructure:** Infrastructure work should depend on documented architecture, assumptions, and boundaries.
2. **ADRs before major platform choices:** Cloud provider strategy, GitOps strategy, runtime selection, identity model, and state strategy should be captured in ADRs.
3. **Validation before automation scale:** Validation should exist before automation is trusted for broad use.
4. **Security before exposure:** Public endpoints, production-like environments, privileged automation, and secrets handling require documented security controls.
5. **Cost controls before persistent resources:** Long-running or potentially expensive cloud resources require tagging, budgets, cleanup, and ownership guidance.
6. **Runbooks before operational claims:** A capability cannot be considered operated without documented procedures.
7. **Simulation labels are mandatory:** Any mock or local-only lab must be labeled **Simulated** and must not be described as deployed infrastructure.
8. **Implementation requires exit criteria:** A phase cannot be marked **Implemented** until its exit criteria are satisfied with repository evidence.
9. **No phase bypassing for dependent work:** Later phases may be researched, but implementation should not depend on missing earlier controls.

## 6. Phase Overview

| Phase | Name | Current status | Primary outcome |
| --- | --- | --- | --- |
| 0 | Foundation | In Progress | Evidence-first repository foundation and documentation baseline |
| 1 | Operational Fundamentals | Planned | Operating model, ownership, runbooks, playbooks, and governance basics |
| 2 | Local Tooling and Validation | Planned | Local checks, Markdown validation, script standards, and safe validation workflows |
| 3 | Terraform Foundation | Planned | IaC design, state strategy, module conventions, and validation path |
| 4 | AWS Networking and Identity | Planned | Target account, identity, and networking architecture with ADR-backed decisions |
| 5 | Security, Cost and Operations Baseline | Planned | Baseline controls for security, FinOps, observability, and operations |
| 6 | ECS Application Platform | Planned | Target ECS platform design and eventual evidence-backed implementation path |
| 7 | CI/CD and DevSecOps | Planned | Delivery workflows, security checks, and change-control model |
| 8 | Kubernetes and EKS | Planned | Target Kubernetes/EKS design and operational model |
| 9 | GitOps and Platform Engineering | Planned | GitOps operating model and platform product practices |
| 10 | SRE and Reliability Engineering | Planned | SLOs, incident practices, reliability reviews, and resilience exercises |
| 11 | Advanced FinOps and Governance | Planned | Cost governance, policy maturity, reporting, and optimization loops |
| 12 | Enterprise Platform Administration | Planned | Enterprise services, administration model, and platform support processes |
| 13 | AI Platform | Planned | Target AI platform boundaries, governance, and architecture |
| 14 | MLOps and AI Reliability | Planned | ML lifecycle, AI reliability, and operational controls |
| 15 | Specialization Labs | Planned | Focused advanced labs clearly labeled by evidence status |

## 7. Detailed Roadmap Phases

### Phase 0 — Foundation

**Status:** In Progress

#### Objective

Establish ECPEL as an evidence-first repository with clear project purpose, architecture direction, documentation navigation, and roadmap discipline.

#### Scope

- Root project documentation.
- Target architecture documentation.
- Roadmap documentation.
- Documentation index structure.
- Market analysis location.
- Explicit warnings against unbacked implementation claims.

#### Expected evidence

- [README.md](README.md) defines the project foundation and repository philosophy.
- [ARCHITECTURE.md](ARCHITECTURE.md) defines target architecture direction and boundaries.
- [ROADMAP.md](ROADMAP.md) defines maturity, dependencies, and phase progression.
- [docs/README.md](docs/README.md) provides documentation navigation.
- [docs/market-analysis/README.md](docs/market-analysis/README.md) provides market-analysis navigation.
- [docs/market-analysis/2026-cloud-market-matrix.md](docs/market-analysis/2026-cloud-market-matrix.md) exists as a completed research artifact.
- [docs/market-analysis/roadmap-from-market.md](docs/market-analysis/roadmap-from-market.md) exists as a roadmap derived from the market analysis.

#### Dependencies

- None. This is the baseline phase.

#### Exit criteria

- README, architecture, and roadmap are internally consistent.
- Internal Markdown links validate successfully.
- Empty or placeholder files are either documented as placeholders or prioritized for future completion.
- The repository does not claim implemented infrastructure or platform capabilities.

#### Deliverables

- Project README.
- Target architecture document.
- Roadmap document.
- Documentation index.
- Completed market-analysis research artifact and derived roadmap location.

### Phase 1 — Operational Fundamentals

**Status:** Planned

#### Objective

Define the operating model required before platform implementation begins.

#### Scope

- Ownership model.
- Support expectations.
- Incident response structure.
- Postmortem approach.
- Runbook and playbook standards.
- Contribution and change-management guidance.

#### Expected evidence

- Completed `CONTRIBUTING.md`.
- Completed `CODE_OF_CONDUCT.md` if community participation is expected.
- Completed `SECURITY.md` with vulnerability reporting process.
- Initial runbook standards in `docs/runbooks/README.md`.
- Initial playbook standards in `docs/playbooks/README.md`.
- Incident response draft in `docs/playbooks/incident-response.md`.
- Postmortem template in `docs/playbooks/postmortem-template.md`.

#### Dependencies

- Phase 0 foundation.

#### Exit criteria

- Operational documents describe ownership, escalation, incident handling, and review practices.
- Security reporting process is documented.
- Runbook and playbook templates are usable for future phases.
- Documentation is linked from the repository navigation.

#### Deliverables

- Operating model documentation.
- Incident response playbook.
- Postmortem template.
- Runbook template or standard.
- Security reporting guidance.

### Phase 2 — Local Tooling and Validation

**Status:** Planned

#### Objective

Create safe local validation tooling before infrastructure or deployment automation is introduced.

#### Scope

- Markdown link validation.
- Documentation consistency checks.
- Shell script standards.
- Local validation entry point.
- Non-destructive validation workflow design.

#### Expected evidence

- Create and validate `scripts/validate.sh` with non-destructive checks before completing the phase.
- Documented validation usage in README or docs.
- Validation rules for Markdown links and formatting.
- Optional local-only helper scripts clearly labeled as local validation.
- CI design documented before workflow execution is claimed.

#### Dependencies

- Phase 0 foundation.
- Phase 1 operational documentation should be started for ownership of checks.

#### Exit criteria

- Validation can be run locally without cloud credentials.
- Validation does not provision or destroy infrastructure.
- Documentation describes exactly what validation checks do.
- All internal Markdown links pass validation.

#### Deliverables

- Local validation script.
- Validation documentation.
- Markdown consistency rules.
- Safe script execution conventions.

### Phase 3 — Terraform Foundation

**Status:** Planned

#### Objective

Design and eventually introduce Terraform foundations for infrastructure-as-code without creating unmanaged or unexplained cloud resources.

#### Scope

- Terraform project conventions.
- Backend and state strategy.
- Module boundaries.
- Environment layout.
- Plan/apply workflow design.
- Destructive-action safeguards.
- Drift detection approach.

#### Expected evidence

- ADR for Terraform state and environment strategy.
- Expected exit artifact: `platform/terraform/README.md`.
- Expected exit artifact: `docs/runbooks/terraform.md`.
- Terraform validation documented before apply automation exists.
- Future Terraform files only after design and validation standards are documented.

#### Dependencies

- Phase 0 foundation.
- Phase 2 local validation.
- Relevant ADR process from `docs/adr/README.md`.

#### Exit criteria

- Terraform design is documented.
- State and environment strategy is recorded.
- Validation path exists for format, lint, plan safety, and policy checks.
- No apply workflow is introduced without approval and cost controls.

#### Deliverables

- Terraform foundation design.
- Terraform ADRs.
- Terraform runbook.
- Validation approach for future IaC.

### Phase 4 — AWS Networking and Identity

**Status:** Planned

#### Objective

Maintain this AWS reference-planning track for target account, identity, and networking architecture before any cloud resources are claimed as implemented; the track remains conditional on a future accepted cloud-strategy ADR and does not adopt AWS.

#### Scope

- Account and environment model.
- AWS Organizations target structure.
- Identity Center target model.
- Network segmentation.
- Routing and DNS assumptions.
- Ingress and egress strategy.
- Audit and access-review expectations.

#### Expected evidence

- ADR for cloud provider and account strategy.
- Expected exit artifact: `platform/aws-organizations/README.md`.
- Expected exit artifact: `platform/landing-zone/README.md`.
- Expected exit artifact: `platform/identity-center/README.md`.
- Expected exit artifact: `platform/networking/README.md`.
- Expected future diagrams: `docs/diagrams/aws-organizations.mmd` and `docs/diagrams/network.mmd` if diagrams are used.
- Expected exit artifact: `docs/runbooks/identity-center.md`.

#### Dependencies

- Phase 0 foundation.
- Phase 1 operational fundamentals.
- Phase 3 Terraform foundation before infrastructure implementation.

#### Exit criteria

- Identity and networking boundaries are documented.
- Account/environment model is documented.
- Security and cost implications are identified.
- No AWS networking or identity implementation is claimed without supporting artifacts.

#### Deliverables

- AWS organization target design.
- Identity target design.
- Network target design.
- Architecture diagrams.
- Identity runbook draft.

### Phase 5 — Security, Cost and Operations Baseline

**Status:** Planned

#### Objective

Establish baseline controls for security, cost, observability, and operations before runtime platforms are introduced.

#### Scope

- Security baseline.
- Compliance evidence model.
- Cost tagging and budget strategy.
- Observability baseline.
- Logging and audit expectations.
- Incident and operational ownership.

#### Expected evidence

- Completed `SECURITY.md`.
- Expected exit artifact: `platform/security/README.md`.
- Expected exit artifact: `platform/compliance/README.md`.
- Completed `docs/compliance/README.md`.
- Expected exit artifact: `platform/finops/README.md`.
- Expected exit artifact: `platform/observability/README.md`.
- Initial cost-reporting design for `scripts/cost-report.sh` before implementation.

#### Dependencies

- Phase 1 operational fundamentals.
- Phase 2 local validation.
- Phase 4 target identity and networking decisions, conditional on a future accepted cloud-strategy ADR.

#### Exit criteria

- Security baseline is documented.
- Cost ownership and tagging model are documented.
- Observability expectations are documented.
- Operational responsibilities are documented.
- No scanner, cost report, or telemetry pipeline is marked implemented unless working artifacts exist.

#### Deliverables

- Security baseline documentation.
- Compliance evidence model.
- FinOps baseline documentation.
- Observability baseline documentation.
- Operations baseline documentation.

### Phase 6 — ECS Application Platform

**Status:** Planned

#### Objective

Preserve this ECS reference-planning track for workloads where Kubernetes is not required; the track remains conditional on a future accepted cloud-strategy ADR and does not adopt AWS or ECS.

#### Scope

- ECS platform architecture.
- Service deployment model.
- Task execution and runtime identity.
- Load balancing and service exposure.
- Logging and monitoring requirements.
- Cost and scaling considerations.
- Operational runbooks.

#### Expected evidence

- Expected exit artifact: `platform/ecs/README.md`.
- Expected exit artifact: `docs/runbooks/ecs.md`.
- Future ECS architecture diagrams if applicable.
- ADR describing when ECS is preferred over other runtime options.
- Future implementation artifacts only after Terraform, identity, networking, security, and cost baselines are ready.

#### Dependencies

- Phase 3 Terraform foundation.
- Phase 4 AWS networking and identity reference-planning track, conditional on a future accepted cloud-strategy ADR.
- Phase 5 security, cost, and operations baseline.

#### Exit criteria

- ECS architecture is documented.
- Operational model and runbook are documented.
- Cost and security implications are documented.
- ECS is not marked implemented until repository artifacts prove it.

#### Deliverables

- ECS target architecture.
- ECS runbook.
- Runtime selection ADR.
- Future implementation checklist.

### Phase 7 — CI/CD and DevSecOps

**Status:** Planned

#### Objective

Define and later implement safe delivery workflows for documentation, infrastructure, and application changes.

#### Scope

- CI workflow design.
- Release workflow design.
- Terraform workflow design.
- Security scanning workflow design.
- Pull request validation.
- Approval and promotion model.
- Supply-chain and dependency considerations.

#### Expected evidence

- Expected future workflow: `.github/workflows/ci.yml` when CI is implemented.
- Expected future workflow: `.github/workflows/release.yml` when release automation is implemented.
- Expected future workflow: `.github/workflows/security.yml` when security automation is implemented.
- Expected future workflow: `.github/workflows/terraform.yml` when Terraform automation is implemented.
- Expected exit artifact: `platform/devsecops/README.md`.
- Documentation of workflow permissions and secrets handling.

#### Dependencies

- Phase 2 local tooling and validation.
- Phase 3 Terraform foundation for Terraform workflows.
- Phase 5 security baseline for DevSecOps controls.

#### Exit criteria

- Workflow purpose and permissions are documented.
- Workflows are non-destructive unless explicitly approved and guarded.
- Security and validation checks are documented.
- CI/CD is not claimed implemented until workflows contain working jobs and validation evidence.

#### Deliverables

- CI/CD design documentation.
- DevSecOps documentation.
- Workflow files when ready.
- Validation and permissions documentation.

### Phase 8 — Kubernetes and EKS

**Status:** Planned

#### Objective

Preserve this Kubernetes/EKS reference-planning track for workloads requiring Kubernetes capabilities; the track remains conditional on a future accepted cloud-strategy ADR and does not adopt AWS, EKS, or Kubernetes.

#### Scope

- EKS target architecture.
- Cluster boundary model.
- Add-on strategy.
- Workload identity.
- Ingress and networking.
- Runtime security.
- Observability and operations.
- Upgrade and lifecycle strategy.

#### Expected evidence

- Expected exit artifact: `platform/eks/README.md`.
- Expected exit artifact: `docs/runbooks/eks.md`.
- Future EKS architecture diagrams if applicable.
- ADR for Kubernetes/EKS selection and cluster strategy.
- Future manifests, Helm charts, or Terraform artifacts only after earlier dependencies are met.

#### Dependencies

- Phase 3 Terraform foundation.
- Phase 4 AWS networking and identity reference-planning track, conditional on a future accepted cloud-strategy ADR.
- Phase 5 security, cost, and operations baseline.
- Phase 7 CI/CD and DevSecOps for safe delivery path.

#### Exit criteria

- EKS architecture is documented.
- Cluster lifecycle and ownership are documented.
- Security, cost, and operational implications are documented.
- EKS is not marked implemented without working artifacts and validation.

#### Deliverables

- EKS target architecture.
- EKS runbook.
- Cluster strategy ADR.
- Future implementation checklist.

### Phase 9 — GitOps and Platform Engineering

**Status:** Planned

#### Objective

Define the GitOps operating model and platform product practices that govern how platform capabilities are consumed and evolved.

#### Scope

- GitOps source-of-truth model.
- Reconciliation and drift strategy.
- Environment promotion.
- Platform product ownership.
- Golden paths and templates.
- Service catalog concepts.
- Consumer onboarding model.

#### Expected evidence

- Expected exit artifact: `platform/gitops/README.md`.
- Required future ADR resolution: an accepted GitOps decision must supersede or otherwise resolve `docs/adr/0003-defer-gitops-strategy-decision.md`.
- Expected exit artifact: `platform/shared/README.md` if shared platform patterns are introduced.
- GitOps workflow documentation.
- Any GitOps tooling must be clearly documented and validated before implementation claims.

#### Dependencies

- Phase 7 CI/CD and DevSecOps.
- Phase 8 Kubernetes and EKS if GitOps is applied to Kubernetes.
- Phase 1 operational fundamentals for ownership and support model.

#### Exit criteria

- GitOps strategy is documented in an ADR.
- Platform product boundaries are documented.
- Consumer onboarding assumptions are documented.
- No GitOps controller or reconciliation loop is claimed without implementation evidence.

#### Deliverables

- GitOps ADR.
- Platform engineering operating model.
- Golden path design.
- Consumer onboarding documentation.

### Phase 10 — SRE and Reliability Engineering

**Status:** Planned

#### Objective

Develop reliability engineering practices for platform and workload operations.

#### Scope

- Service-level indicators and objectives.
- Error budgets.
- Incident response maturity.
- Postmortem process.
- Game day planning.
- Resilience testing approach.
- Reliability reviews.

#### Expected evidence

- Completed `docs/game-days/README.md`.
- Expected exit artifact: `docs/game-days/game-day-001.md` and later game-day documents as exercises are designed.
- Expected exit artifact: `docs/playbooks/disaster-recovery.md`.
- Completed `docs/playbooks/incident-response.md`.
- Completed `docs/postmortems/README.md`.
- Reliability model documented in `platform/observability/README.md` or related docs.

#### Dependencies

- Phase 1 operational fundamentals.
- Phase 5 security, cost, and operations baseline.
- At least one runtime platform design from Phase 6 or Phase 8 before platform-specific reliability claims.

#### Exit criteria

- Reliability practices are documented.
- Incident and postmortem workflows are documented.
- Game day scenarios are labeled as planned, simulated, or executed based on evidence.
- No SLO or reliability claim is made without measurement evidence.

#### Deliverables

- Reliability engineering documentation.
- Incident response playbook.
- Disaster recovery playbook.
- Game day plans.
- Postmortem process.

### Phase 11 — Advanced FinOps and Governance

**Status:** Planned

#### Objective

Advance cost management and governance beyond baseline documentation into measurable practices when evidence exists.

#### Scope

- Cost allocation and tagging enforcement design.
- Budget and anomaly response process.
- Showback or chargeback model.
- Governance policy model.
- Cost optimization review process.
- Compliance and risk reporting.

#### Expected evidence

- Expected exit artifact: `platform/finops/README.md` with advanced practices.
- Create `scripts/cost-report.sh` only when it has real, documented behavior and validation evidence.
- Expected exit artifact: `platform/cloud-governance/README.md`.
- Governance metrics and reports when evidence exists.
- Compliance mappings in `docs/compliance/README.md` or related documents.

#### Dependencies

- Phase 5 security, cost, and operations baseline.
- Phase 7 CI/CD and DevSecOps if governance checks are automated.
- Runtime phases only if cost reporting depends on actual workloads.

#### Exit criteria

- Advanced cost practices are documented.
- Governance process is documented.
- Any cost reporting automation is validated and non-misleading.
- Optimization recommendations are based on evidence, not assumptions.

#### Deliverables

- Advanced FinOps documentation.
- Governance model.
- Cost reporting implementation if evidence exists.
- Optimization review process.

### Phase 12 — Enterprise Platform Administration

**Status:** Planned

#### Objective

Define enterprise administration practices for platform services, repositories, quality systems, and shared services.

#### Scope

- GitHub Enterprise administration model.
- SonarQube Enterprise administration model.
- Shared services ownership.
- Repository standards.
- Enterprise service lifecycle.
- Access review and audit practices.
- Support and escalation model.

#### Expected evidence

- Expected exit artifact: `platform/github-enterprise/README.md`.
- Expected exit artifact: `platform/sonarqube-enterprise/README.md`.
- Expected exit artifact: `platform/enterprise-services/README.md`.
- Expected exit artifact: `platform/shared/README.md`.
- Runbooks for enterprise services when services are actually implemented.

#### Dependencies

- Phase 1 operational fundamentals.
- Phase 5 security, cost, and operations baseline.
- Phase 7 CI/CD and DevSecOps for repository and quality workflows.

#### Exit criteria

- Enterprise administration model is documented.
- Access and ownership boundaries are documented.
- No enterprise service is marked operational without implementation and runbook evidence.

#### Deliverables

- Enterprise administration documentation.
- Shared services model.
- Repository standards.
- Enterprise service runbook plan.

### Phase 13 — AI Platform

**Status:** Planned

#### Objective

Define target architecture and governance boundaries for future AI platform capabilities.

#### Scope

- AI platform use cases.
- Model and agent governance.
- Data access boundaries.
- Security and privacy requirements.
- Cost and capacity considerations.
- Developer experience for AI workloads.
- Responsible AI review model.

#### Expected evidence

- Expected exit artifact: `platform/ai-platform/README.md`.
- Expected exit artifact: `platform/ai-agents/README.md` if agent patterns are documented.
- ADRs for AI platform boundaries and governance.
- Cost and safety considerations documented before any AI service implementation.

#### Dependencies

- Phase 5 security, cost, and operations baseline.
- Phase 11 advanced FinOps and governance for cost-heavy AI workloads.
- Phase 12 enterprise platform administration if AI services depend on enterprise administration.

#### Exit criteria

- AI platform boundaries are documented.
- AI governance and safety requirements are documented.
- Cost risks are documented.
- No AI platform capability is marked implemented without artifacts and validation.

#### Deliverables

- AI platform target architecture.
- AI governance documentation.
- AI agent boundary documentation.
- AI cost and safety checklist.

### Phase 14 — MLOps and AI Reliability

**Status:** Planned

#### Objective

Define lifecycle, reliability, and operational practices for ML and AI systems.

#### Scope

- ML lifecycle management.
- Experiment tracking target model.
- Model deployment boundaries.
- Model monitoring and drift concepts.
- AI reliability and evaluation.
- Incident response for AI systems.
- Governance and audit evidence.

#### Expected evidence

- Expected exit artifact: `platform/mlops/README.md`.
- AI reliability documentation.
- ADRs for MLOps lifecycle choices.
- Runbooks or playbooks for AI/ML operations if implemented.
- Evaluation artifacts only when actual simulations or implementations exist.

#### Dependencies

- Phase 13 AI Platform.
- Phase 10 SRE and Reliability Engineering.
- Phase 11 Advanced FinOps and Governance.

#### Exit criteria

- MLOps architecture and lifecycle are documented.
- AI reliability practices are documented.
- Evaluation and monitoring claims are backed by evidence.
- No model platform, evaluation system, or reliability system is marked implemented without repository artifacts.

#### Deliverables

- MLOps target architecture.
- AI reliability model.
- AI/ML operations checklist.
- Future evaluation evidence structure.

### Phase 15 — Specialization Labs

**Status:** Planned

#### Objective

Create focused specialization labs only after the repository has enough foundation, validation, and safety guidance to prevent misleading or unsafe claims.

#### Scope

- Advanced cloud platform scenarios.
- Security exercises.
- FinOps exercises.
- Reliability game days.
- Platform administration exercises.
- AI and MLOps exercises.
- Portfolio-ready demonstrations clearly labeled by evidence status.

#### Expected evidence

- Lab README files with explicit status labels.
- Prerequisites and cleanup instructions.
- Validation steps.
- Cost warnings where applicable.
- Security warnings where applicable.
- Clear distinction between simulated and implemented labs.

#### Dependencies

- Relevant earlier phases depending on lab topic.
- Phase 2 local validation for any runnable local lab.
- Phase 5 security, cost, and operations baseline for cloud-related labs.
- Phase 10 reliability practices for game-day labs.

#### Exit criteria

- Each lab has a status: Planned, In Progress, Implemented, Simulated, or Deferred.
- Each lab includes evidence requirements and validation instructions.
- No lab is described as real infrastructure unless repository artifacts prove it.
- Cleanup and cost guidance exist for any lab that could create resources.

#### Deliverables

- Specialization lab index.
- Individual lab documents.
- Validation and cleanup instructions.
- Evidence records for completed or simulated labs.

## Roadmap Governance

This roadmap should be updated whenever repository evidence changes. Updates should include:

- status changes with supporting evidence;
- new dependencies or risks;
- added or removed phases;
- changes to exit criteria;
- links to ADRs, diagrams, runbooks, workflows, scripts, or implementation artifacts.

A phase should not move to **Implemented** unless all exit criteria are satisfied and the relevant evidence is present in the repository.

## Summary

ECPEL is currently a foundation-stage repository. This roadmap provides a long-term path toward enterprise cloud platform engineering maturity while preserving the repository's governing principle: **No evidence, no implementation.**
