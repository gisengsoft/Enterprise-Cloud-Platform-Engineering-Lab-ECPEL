# 2026 Cloud Market Matrix

## Status

**Research complete for Pull Request #7 — not an implementation decision**

- Research date: 2026-07-16
- Repository maturity: Initial Foundation
- Evidence classes: Fact, Analysis, Recommendation, Not assessed
- Primary cloud adopted: None
- Primary Infrastructure as Code tool adopted: None
- Cloud resources created by this research: None

This document records evidence and ECPEL-specific analysis. It does not authorize implementation, approve expenditure, establish production architecture, or change a capability to Implemented.

> No evidence, no implementation.

## Purpose

The matrix:

- compares enterprise cloud-foundation capabilities across AWS, Microsoft Azure, and Google Cloud;
- compares cross-cloud technologies relevant to platform engineering, DevOps, SRE, security, and FinOps;
- identifies dependencies, operational burden, cost risks, and safe sequencing;
- provides evidence for future ADRs;
- distinguishes provider facts from ECPEL analysis and recommendations.

## Scope

### Primary provider comparison

- Amazon Web Services
- Microsoft Azure
- Google Cloud

### Cross-cloud toolchain domains

- Infrastructure as Code
- Configuration management
- CI/CD
- GitOps
- Kubernetes control planes
- Internal developer platforms
- Observability
- Policy as Code
- Secrets management
- Software supply-chain security
- Kubernetes networking
- Kubernetes cost allocation
- FinOps

### Out of scope

This research explicitly excludes:

- provider adoption;
- account, subscription, or project creation;
- cloud deployment;
- credential or federation configuration;
- production architecture approval;
- definitive tool adoption;
- compliance certification claims;
- promotional-credit-driven architecture;
- unsupported market-share claims;
- employment-market and salary conclusions.

OCI is not scored in this version.

OCI may later be documented as an auxiliary authorized environment without implying strategic adoption or technical rejection.

## Evidence Policy

| Classification | Meaning |
| --- | --- |
| Fact | Directly supported by first-party documentation listed in the source register. |
| Analysis | ECPEL-specific interpretation derived from documented capabilities and project constraints. |
| Recommendation | Proposed direction that requires review and, when architectural, an accepted ADR. |
| Not assessed | Evidence is incomplete or the subject is deliberately deferred. |

1. Product documentation proves documented capability, not objective superiority.
2. Analysis and recommendations must not be presented as provider facts.
3. No capability is Adopted without an accepted ADR.
4. No capability is Implemented without repository and runtime evidence.
5. Pricing, quotas, availability, free tiers, and product limits must be reverified immediately before a lab.
6. Promotional credits are not a durable architectural criterion.
7. Provider certifications do not certify an ECPEL implementation.

## Evaluation Method

### Score scale

| Score | ECPEL-specific meaning |
| ---: | --- |
| 0 | Does not satisfy the evaluated requirement |
| 1 | Very limited fit or major blocker |
| 2 | Partial fit with significant constraints |
| 3 | Meets the core need with material complexity or risk |
| 4 | Strong fit with manageable constraints |
| 5 | Excellent fit for the defined ECPEL requirement |

### Approved weights

| Dimension | Weight |
| --- | ---: |
| Enterprise governance and landing zones | 12% |
| Identity and workload identity | 10% |
| Networking and connectivity | 10% |
| Security and compliance controls | 10% |
| Managed Kubernetes | 8% |
| Managed containers without Kubernetes | 6% |
| Observability and operations | 8% |
| FinOps and cost guardrails | 10% |
| Infrastructure as Code and automation | 8% |
| Developer and platform experience | 6% |
| Portfolio laboratory feasibility | 8% |
| Complexity and operational risk | 4% |
| Total | 100% |

Weighted result = sum(score / 5 * dimension weight)

This is an ECPEL research model and not an industry-standard benchmark.

## Provider Capability Summary

Documented capabilities in this table are classified as Fact.

| Capability | AWS | Microsoft Azure | Google Cloud |
| --- | --- | --- | --- |
| Resource hierarchy | Organizations, OUs, accounts | Entra tenant, management groups, subscriptions, resource groups | Organization, folders, projects, resources |
| Enterprise foundation | AWS Control Tower | Azure Landing Zones | Google Cloud landing-zone guidance |
| Workforce identity | IAM Identity Center | Microsoft Entra ID | Cloud Identity and IAM |
| GitHub workload federation | IAM OIDC provider and role | Entra federated identity credential | Workload Identity Federation |
| Managed Kubernetes | Amazon EKS | Azure Kubernetes Service | Google Kubernetes Engine |
| Managed containers without direct Kubernetes administration | Amazon ECS with Fargate | Azure Container Apps | Cloud Run |
| Native observability | CloudWatch | Azure Monitor | Google Cloud Observability |
| Native cost controls | AWS cost tools and AWS Budgets | Microsoft Cost Management and budgets | Cloud Billing budgets and alerts |
| Native IaC | CloudFormation and AWS CDK | ARM and Bicep | Infrastructure Manager with Terraform |
| Adoption status | None | None | None |

## Enterprise Governance and Landing Zones

Facts:

- AWS Control Tower orchestrates services including AWS Organizations and IAM Identity Center to establish and govern a multi-account landing zone.
- Azure Landing Zones use management groups, subscriptions, and policy-driven governance.
- Google Cloud landing-zone guidance covers resource hierarchy, identity, networking, and security with organizations, folders, and projects.

Analysis: all three providers support enterprise governance patterns, and product existence alone cannot decide the provider.

Evaluation considers individual portfolio prerequisites, hierarchy and identity complexity, isolated laboratories, audit defaults, policy inheritance, cleanup, cost visibility, and evidence collection.

Recommendation: do not deploy a complete landing zone as the first cloud laboratory.

## Identity and Workload Federation

| Requirement | AWS | Microsoft Azure | Google Cloud |
| --- | --- | --- | --- |
| GitHub Actions OIDC | Supported | Supported | Supported |
| Long-lived cloud key required | No | No | No |
| Short-lived token exchange | Yes | Yes | Yes |
| Trust restriction | IAM role trust-policy conditions | Federated credential subject and audience | Attribute mapping, conditions, and IAM |
| ECPEL target | Required | Required | Required |

GitHub Actions OIDC allows workflows to exchange identity tokens for short-lived credentials instead of storing long-lived cloud credentials.

Future cloud workflows must require:

1. GitHub environment protection;
2. OIDC federation;
3. repository, branch, tag, or environment restrictions;
4. least privilege;
5. short sessions;
6. no static administrator key in GitHub Secrets;
7. separate plan and apply permissions;
8. human approval before apply;
9. audit evidence;
10. revocation and recovery guidance.

This research creates no credentials.

## Networking and Connectivity

| Area | AWS | Microsoft Azure | Google Cloud |
| --- | --- | --- | --- |
| Workload network | VPC | Virtual Network | VPC network |
| Enterprise hub pattern | Transit Gateway | Hub-and-spoke or Virtual WAN | Shared VPC |
| Organizational separation | Accounts | Subscriptions | Host and service projects |
| Hybrid connectivity | VPN and Direct Connect | VPN Gateway and ExpressRoute | Cloud VPN and Cloud Interconnect |

Analysis: enterprise topologies add routing, policy, ownership, and recurring-cost considerations.

First-lab recommendation:

- one isolated account, subscription, or project scope;
- one network;
- no enterprise transit service;
- no public administrative port;
- minimal egress;
- explicit deletion verification.

## Security, Audit, and Compliance Boundaries

| Function | AWS | Microsoft Azure | Google Cloud |
| --- | --- | --- | --- |
| Security posture | Security Hub capabilities | Defender for Cloud capabilities | Security Command Center capabilities |
| Threat detection | GuardDuty ecosystem | Defender workload protection | Security Command Center threat detection |
| Administrative audit | CloudTrail | Azure Activity Log and resource logs | Cloud Audit Logs |
| Governance integration | Organizations, controls, Config, security services | Azure Policy and Defender recommendations | Organization Policy and SCC findings |

This research does not prove equal coverage, pricing, retention, or operational effectiveness.

Foundational lab evidence must include:

- audit logging reviewed;
- least privilege;
- no public administrative exposure;
- encryption defaults documented;
- security posture or finding view reviewed;
- retention and logging cost documented;
- no intentionally unresolved critical exposure.

Provider reports do not prove ECPEL compliance with ISO, SOC, PCI DSS, LGPD, HIPAA, or any other framework.

## Container Platforms

### Managed Kubernetes

- AWS: Amazon EKS
- Azure: Azure Kubernetes Service
- Google Cloud: Google Kubernetes Engine

All are research candidates and no Kubernetes provider is selected.

### Managed containers without direct cluster administration

- AWS: Amazon ECS with Fargate
- Azure: Azure Container Apps
- Google Cloud: Cloud Run

Recommended sequence:

1. reproducible local container build;
2. dependency and image scan;
3. SBOM;
4. immutable digest;
5. signing and attestation evaluation;
6. registry lifecycle;
7. managed container runtime;
8. Kubernetes only after identity, networking, cost, secrets, registry, observability, and recovery prerequisites exist.

## Observability and Operations

Compare:

- AWS CloudWatch;
- Azure Monitor;
- Google Cloud Monitoring and Logging.

Evaluation must include metrics, logs, tracing, alerting, and OpenTelemetry integration.

A dashboard alone is not operational evidence.

Future evidence must include:

- signal and purpose;
- data source;
- retention;
- estimated cost;
- threshold or SLO;
- alert delivery;
- linked runbook;
- simulated failure;
- recovery verification.

## FinOps and Cost Guardrails

All three providers offer cost analysis, budgets, and alerts.

Budgets must not be presented as guaranteed hard spending caps.

Before any paid lab require:

- maximum expected cost;
- budget or spending protection;
- tags or labels;
- approved region;
- cleanup deadline;
- destroy procedure;
- post-destroy verification;
- final cost review;
- user confirmation before apply.

## Infrastructure as Code

| Tool | Authoring model | State model | ECPEL position |
| --- | --- | --- | --- |
| Terraform | HCL, declarative | State | Existing simulated lab; adoption ADR pending |
| OpenTofu | HCL-compatible, declarative | State | Compare in IaC ADR |
| Pulumi | General-purpose languages or YAML | State | Compare language and backend complexity |
| Crossplane | Kubernetes APIs and reconciliation | Kubernetes control plane | Advanced platform-control-plane candidate |

| Provider | Option | Boundary |
| --- | --- | --- |
| AWS | CloudFormation and AWS CDK | AWS-specific |
| Microsoft Azure | ARM and Bicep | Azure-specific |
| Google Cloud | Infrastructure Manager using Terraform | Google Cloud managed execution |
| Google Cloud legacy | Deployment Manager | Support ended; exclude from new designs |

The IaC ADR must compare Terraform, OpenTofu, and Pulumi.

Crossplane is a later control-plane decision and not the first ECPEL provisioning tool.

## Configuration Management: Ansible

- Ansible uses playbooks;
- Ansible commonly manages targets without an Ansible agent;
- check mode and diff mode support validation where modules support them;
- idempotence must be tested and is not guaranteed for every playbook or module.

IaC and Ansible are complementary:

- IaC manages infrastructure resources and lifecycle;
- Ansible manages operating systems, applications, network devices, and post-provisioning state.

Recommendation: a future local disposable Ansible lab should include inventory, playbook, role, handlers, templates, variables, linting, syntax check, check mode, diff mode, repeated-run idempotence evidence, no cloud credentials, and no production target.

## CI/CD and GitOps

| Technology | Role | ECPEL position |
| --- | --- | --- |
| GitHub Actions | Repository automation and CI/CD | Current validated baseline |
| Jenkins | Self-hosted automation server and Pipeline as Code | Enterprise and brownfield comparator |
| Tekton | Kubernetes-native Tasks, Pipelines, and Runs | Later, after Kubernetes |
| Argo CD | Declarative GitOps CD for Kubernetes | Later |
| Flux | Declarative reconciliation from Git or OCI sources | Later |

Jenkins evaluation must include:

- controller;
- agents;
- authentication;
- credential storage;
- plugin inventory;
- upgrades;
- vulnerability management;
- persistence;
- backup and restore;
- network exposure;
- resource consumption;
- operational ownership.

Jenkins is not selected as a replacement for GitHub Actions.

Argo CD and Flux are not general replacements for all CI build, test, and scanning functions.

## Platform Engineering

| Technology | Role | Timing |
| --- | --- | --- |
| Backstage | Developer portal, software catalog, templates, documentation | After ownership and catalog models |
| Crossplane | Custom platform APIs and infrastructure compositions | After Kubernetes and IaC decisions |

Installing Backstage without ownership, catalog metadata, templates, and operational responsibility would be tool installation, not defensible platform engineering evidence.

## Observability Toolchain

- OpenTelemetry;
- Prometheus;
- Grafana.

OpenTelemetry generates, collects, and exports telemetry. OpenTelemetry is not a storage or visualization backend. Prometheus focuses on time-series metrics and alerting. Grafana queries and visualizes supported data sources.

Recommended sequence:

1. observability concepts and service indicators;
2. instrumentation;
3. metrics collection;
4. dashboards;
5. alerts;
6. runbooks;
7. controlled failure testing.

## Policy as Code

- Open Policy Agent as a general-purpose policy engine;
- Kyverno as a cloud-native policy engine with Kubernetes and JSON policy capabilities.

Neither tool is selected by this research.

## Secrets Management

Initial labs should prefer:

- workload identity;
- short-lived credentials;
- native secret managers where sufficient;
- no committed credentials.

Vault is a centralized secrets and privileged-access option with static and dynamic secret capabilities, authorization, and audit.

Self-managed Vault adds significant operational responsibility and should only be evaluated for a concrete requirement.

## Software Supply-Chain Security

Include these capabilities in future evaluations:

- dependency scanning;
- image scanning;
- SBOM;
- provenance;
- signing;
- signature verification;
- attestation verification;
- protected environments;
- trusted publishing;
- least-privilege workflow permissions;
- pinned actions and dependencies;
- Sigstore/Cosign;
- SLSA.

No SLSA level may be claimed without satisfying and proving every applicable requirement.

## Kubernetes Networking and FinOps Watchlist

- Cilium and eBPF are advanced networking, policy, and observability research after a stable cluster exists;
- OpenCost is Kubernetes cost measurement and allocation research after a cluster and metrics foundation exist.

This watchlist does not recommend immediate implementation.

## Weighted Provider Assessment

| Dimension | Weight | AWS | Azure | Google Cloud |
| --- | ---: | ---: | ---: | ---: |
| Enterprise governance and landing zones | 12% | 5 | 5 | 4 |
| Identity and workload identity | 10% | 4 | 5 | 5 |
| Networking and connectivity | 10% | 5 | 5 | 4 |
| Security and compliance controls | 10% | 5 | 5 | 5 |
| Managed Kubernetes | 8% | 4 | 4 | 5 |
| Managed containers without Kubernetes | 6% | 4 | 5 | 5 |
| Observability and operations | 8% | 4 | 5 | 5 |
| FinOps and cost guardrails | 10% | 5 | 5 | 5 |
| Infrastructure as Code and automation | 8% | 5 | 5 | 4 |
| Developer and platform experience | 6% | 4 | 5 | 4 |
| Portfolio laboratory feasibility | 8% | 5 | 4 | 5 |
| Complexity and operational risk | 4% | 3 | 3 | 4 |
| Weighted result | 100% | 90.8 | 95.2 | 92.0 |

Interpretation:

1. Microsoft Azure: 95.2
2. Google Cloud: 92.0
3. AWS: 90.8

All three providers are viable. Score differences are small. The ranking is ECPEL-specific. It is not an objective or universal market ranking. Temporary credits are excluded from durable scoring.

## ECPEL Recommendations

1. Microsoft Azure is the leading candidate for the future cloud strategy ADR, but is not adopted.
2. GitHub Actions remains the current validated CI baseline.
3. Jenkins remains an enterprise and brownfield comparator.
4. A local Ansible foundation lab is the next local implementation candidate after the ADR phase.
5. The first cloud lab must use OIDC, least privilege, human approval, one low-cost ephemeral resource, destroy, post-destroy verification, and final cost review.
6. Kubernetes must be deferred until identity, networking, registry, secrets, security, observability, cost, and recovery prerequisites exist.

Target cloud-lab sequence:

GitHub Actions → protected environment → OIDC federation → least-privilege identity → plan → human approval → one low-cost ephemeral resource → validation evidence → destroy → provider-side post-destroy verification → final cost review

## Risks and Limitations

- first-party documentation is provider-authored;
- no equivalent hands-on provider benchmark was executed;
- scores include ECPEL analysis;
- product features, quotas, limits, prices, and availability change;
- managed services do not eliminate operational ownership;
- open-source tools still require operation and security;
- portfolio suitability does not prove production suitability;
- no performance, availability, security, compliance, or support guarantee is established;
- employment-market demand was not assessed.

## Implementation Boundary

This research does not:

- adopt AWS, Azure, or Google Cloud;
- adopt any evaluated tool;
- create credentials;
- create or modify cloud resources;
- authorize expenditure;
- execute an apply;
- modify an ADR;
- classify a cloud or platform capability as Implemented.

## Official Source Register

Use only first-party sources.

### GitHub and identity

- https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers
- https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html
- https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect
- https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines

### Cloud foundations

- https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups
- https://docs.cloud.google.com/architecture/landing-zones
- https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy
- https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html
- https://learn.microsoft.com/en-us/azure/networking/design-guide/hub-spoke
- https://docs.cloud.google.com/vpc/docs/shared-vpc

### Security, audit, and compliance boundaries

- https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html
- https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html
- https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html
- https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction
- https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
- https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview
- https://docs.cloud.google.com/logging/docs/audit

### Containers, observability, cost, and IaC

- https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
- https://learn.microsoft.com/en-us/azure/aks/what-is-aks
- https://learn.microsoft.com/en-us/azure/container-apps/overview
- https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview
- https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
- https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview
- https://docs.cloud.google.com/monitoring/docs/monitoring-overview
- https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html
- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- https://docs.cloud.google.com/billing/docs/how-to/budgets
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview
- https://docs.cloud.google.com/infrastructure-manager/docs/overview
- https://cloud.google.com/deployment-manager/docs/deprecations

### Cross-cloud toolchain

- https://docs.ansible.com/projects/ansible-core/devel/playbook_guide/playbooks_intro.html
- https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html
- https://www.jenkins.io/doc/
- https://www.jenkins.io/doc/book/pipeline/
- https://opentofu.org/docs/cli/commands/plan/
- https://www.pulumi.com/docs/iac/concepts/
- https://www.pulumi.com/docs/iac/concepts/state-and-backends/
- https://tekton.dev/docs/pipelines/
- https://argo-cd.readthedocs.io/en/stable/
- https://fluxcd.io/flux/concepts/
- https://docs.crossplane.io/latest/composition/compositions/
- https://backstage.io/docs/overview/what-is-backstage/
- https://opentelemetry.io/docs/what-is-opentelemetry/
- https://prometheus.io/docs/introduction/overview/
- https://grafana.com/docs/grafana/latest/introduction/
- https://www.openpolicyagent.org/docs
- https://kyverno.io/docs/introduction/
- https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault
- https://docs.sigstore.dev/cosign/signing/overview/
- https://slsa.dev/spec/v1.2/
- https://opencost.io/docs/
- https://docs.cilium.io/en/stable/overview/intro/
