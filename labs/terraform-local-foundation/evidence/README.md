# Terraform Local Foundation Lab Evidence

This evidence record tracks validation for the Terraform Local Foundation Lab, which is classified as **Simulated** because it is a local-only, non-production demonstration.

> **Principle:** No evidence, no implementation.

## Execution Metadata

| Field | Value |
| --- | --- |
| Execution date | 2026-07-14 |
| Execution environment | Codex container shell environment |
| Terraform availability | Not available in the execution environment |
| Terraform version used | Not Applicable |
| Cloud credentials used | No |
| Cloud resources provisioned | No |
| `terraform apply` executed | No |
| `terraform destroy` executed | No |

## Validation Results

| Check | Command | Result | Evidence or Notes |
| --- | --- | --- | --- |
| Terraform version | `terraform version` | Failed | Terraform CLI was unavailable; preflight shell returned `terraform: command not found`. |
| Format | `terraform fmt -check -recursive` | Not Run | Not executed because Terraform CLI was unavailable. |
| Initialization | `terraform init -backend=false -input=false` | Not Run | Not executed because Terraform CLI was unavailable. |
| Validation | `terraform validate` | Not Run | Not executed because Terraform CLI was unavailable. |
| Test | `terraform test` | Not Run | Native test file is present, but tests were not executed because Terraform CLI was unavailable. |
| Plan | `terraform plan -input=false -lock=false -no-color` | Not Run | Not executed because Terraform CLI was unavailable. |

## Limitations

- Terraform command validation was not performed in this execution environment.
- The lab status remains **Simulated** and not **Validated** until Terraform formatting, initialization, validation, test, and plan commands run successfully.
- No generated Terraform state, plan, or lock files are included as evidence.

## Files Generated During Validation

No Terraform-generated files were created during validation because Terraform was unavailable.

## Cloud Provisioning Confirmation

No cloud provider is configured by this lab, no cloud authentication was attempted, and no cloud resources were provisioned.

## Automated Validation

Status: **Pending**.

The automated validation workflow is defined at `../../../.github/workflows/terraform-local-foundation.yml`. It is intended to run the following checks for the Terraform Local Foundation Lab:

- `terraform version`
- `terraform fmt -check -recursive`
- `terraform init -backend=false -input=false`
- `terraform validate -no-color`
- `terraform test -no-color`
- `terraform plan -input=false -lock=false -no-color`

The first GitHub Actions result is pending. Terraform checks must not be marked **Passed** until a real workflow run succeeds and provides evidence. Until then, use **Pending** or **Not Run** for automated validation results.

The lab remains **Simulated**. No cloud resources are provisioned, no cloud credentials are required, and the workflow does not execute `terraform apply` or `terraform destroy`.
