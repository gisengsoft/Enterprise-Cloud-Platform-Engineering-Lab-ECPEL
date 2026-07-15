# Terraform Local Foundation Lab

## Status

Status: **Simulated**.

This lab is a local-only simulation and learning exercise. Its Terraform configuration has passed automated GitHub Actions validation with Terraform 1.6.0 and Terraform 1.15.8. The lab remains classified as **Simulated** because it does not provision cloud infrastructure, does not represent a production environment, and does not establish Terraform as ECPEL's primary Infrastructure as Code tool. See [evidence](evidence/README.md).

## Purpose

This lab establishes a small, reproducible, local Terraform workflow before any cloud provisioning is introduced. It demonstrates Terraform language structure and validation concepts without using cloud providers, remote state, credentials, paid services, Kubernetes, Docker, apply, or destroy operations.

## Learning Objectives

- Terraform project structure.
- Input variables.
- Variable validation.
- Local values.
- Local module composition.
- Outputs.
- Initialization.
- Formatting.
- Validation.
- Planning.
- Optional native Terraform tests when supported by the local Terraform CLI.
- Safe handling of generated files.

## Scope

This lab is local-only. It models lab metadata and naming conventions through Terraform expressions and a local module. It does not create infrastructure.

## Out of Scope

- AWS provisioning.
- Remote state.
- Production use.
- Application delivery and deployment pipelines.
- Cloud deployment automation.
- Cloud credentials.
- Persistent infrastructure.
- Cost-generating resources.
- Terraform apply or destroy workflows.

## Prerequisites

- Git.
- Terraform CLI compatible with `>= 1.6.0`.
- Terminal access.

Terraform `>= 1.6.0` is selected because the lab includes native Terraform test syntax in `tests/foundation.tftest.hcl`. This version constraint is based on lab features and is not a claim that it is the latest Terraform version.

## Directory Structure

| Path | Purpose |
| --- | --- |
| `README.md` | Lab documentation and usage instructions. |
| `versions.tf` | Required Terraform version constraint. |
| `variables.tf` | Input variables and validation rules. |
| `locals.tf` | Normalized local values. |
| `main.tf` | Local module composition. |
| `outputs.tf` | Lab outputs. |
| `terraform.tfvars.example` | Safe fictional example inputs. |
| `modules/naming/` | Local naming and metadata normalization module. |
| `tests/foundation.tftest.hcl` | Native Terraform test file for plan-time assertions. |
| `evidence/README.md` | Validation evidence record. |

## Usage

Run these commands from this directory:

```bash
terraform version
terraform fmt -check -recursive
terraform init -backend=false -input=false
terraform validate
terraform test
terraform plan -input=false -lock=false
```

Do not run `terraform apply` for this lab.

## Expected Results

Expected result categories:

- Terraform version reports a compatible CLI.
- Formatting check passes.
- Initialization succeeds without remote backend configuration.
- Validation succeeds without cloud providers.
- Native tests pass when supported by the installed Terraform CLI.
- Plan succeeds and shows local outputs such as `normalized_project_name`, `generated_resource_prefix`, `normalized_metadata`, and `lab_summary` without provisioning cloud resources.

Do not treat these expected categories as evidence unless the commands actually run successfully. Current evidence is recorded in [evidence/README.md](evidence/README.md).

## Validation

The validation commands prove:

- formatting through `terraform fmt -check -recursive`;
- initialization through `terraform init -backend=false -input=false`;
- valid configuration through `terraform validate`;
- native test behavior through `terraform test`;
- plan behavior through `terraform plan -input=false -lock=false`.


## Automated GitHub Actions Validation

The Terraform Local Foundation Validation workflow is defined at `../../../.github/workflows/terraform-local-foundation.yml`. It runs for every Pull Request targeting `main`, creating a consistent repository regression gate even when a Pull Request does not modify Terraform files. Pushes to `main` run the workflow when this Terraform lab or the workflow changes, and manual `workflow_dispatch` runs remain supported. This universal Pull Request validation does not change the lab status from **Simulated** and does not establish Terraform as ECPEL's primary Infrastructure as Code tool. The workflow never runs `terraform apply` or `terraform destroy`.

The workflow uses an explicit Terraform version matrix for the minimum supported version, `1.6.0`, and the current stable Terraform release verified during implementation, `1.15.8`. For each matrix entry, Terraform commands run from this lab directory in the following order:

```text
terraform version
terraform fmt -check -recursive
terraform init -backend=false -input=false
terraform validate -no-color
terraform test -no-color
terraform plan -input=false -lock=false -no-color
```

The workflow does not run `terraform apply` or `terraform destroy`, does not require cloud credentials, does not configure remote state, and does not authenticate to any cloud provider. A workflow definition alone is not validation evidence. Successful GitHub Actions executions are recorded in [evidence/README.md](evidence/README.md). Automated validation confirms the local Terraform configuration, but it does not change the lab from **Simulated** to **Implemented** and does not prove that cloud infrastructure exists.

## Cleanup

Generated files should not be committed.

Safe cleanup targets include:

- delete `.terraform/` from this lab directory if initialization creates it;
- delete local `terraform.tfstate` or `terraform.tfstate.backup` files if any are generated during experimentation.

Do not use destructive wildcard cleanup commands.

## Security Considerations

- No credentials are required.
- No cloud provider is configured.
- No secrets should be committed.
- Future `.tfvars` files may contain sensitive data and must not be committed unless they are explicitly safe examples.
- Generated state files must not be committed.

## Cost Considerations

This local lab is designed not to provision paid cloud resources. It does not guarantee zero cost for unrelated user tooling, local environment behavior, or external systems outside this repository.

## Troubleshooting

| Symptom | Possible Cause | Suggested Action |
| --- | --- | --- |
| `terraform: command not found` | Terraform CLI is not installed or not on `PATH`. | Install Terraform outside this repository according to your environment standards, then rerun validation. |
| Unsupported Terraform version | Installed Terraform is older than `>= 1.6.0`. | Use a compatible Terraform CLI before running tests. |
| Formatting failure | Files are not formatted according to Terraform conventions. | Run `terraform fmt -recursive`, review the diff, and rerun the check. |
| Initialization failure | Local module path or Terraform version is invalid. | Review `main.tf`, `versions.tf`, and module paths. |
| Validation failure | Variable, output, or module syntax is invalid. | Review the Terraform error and update the relevant `.tf` file. |
| Test command unavailable | Terraform version does not support native tests. | Upgrade to a compatible Terraform version or record tests as Not Run. |

## Evidence

Validation evidence is recorded in [evidence/README.md](evidence/README.md).

## Related Documents

- [Repository README](../../README.md)
- [Roadmap](../../ROADMAP.md)
- [Architecture](../../ARCHITECTURE.md)
- [Blueprint](../../BLUEPRINT.md)
- [ADR-0006: Defer Primary Infrastructure as Code Tool Decision](../../docs/adr/0006-defer-primary-infrastructure-as-code-tool-decision.md)
- [Capability Dependency Map](../../docs/diagrams/capability-dependency-map.md)
