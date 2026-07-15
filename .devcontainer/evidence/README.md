# ECPEL Development Container Evidence

## Status

Pending

## Validation Record

| Check | Expected Command or Action | Result | Notes |
| --- | --- | --- | --- |
| Codespace creation | Create a Codespace from the PR branch under test | Not Run | Must be performed in GitHub Codespaces. |
| Dev container build | Build the configured development container | Not Run | A configuration file alone is not build evidence. |
| Terraform version | `terraform version` | Not Run | Expected Terraform version is 1.15.8. |
| Git version | `git --version` | Not Run | Verifies Git availability in the container. |
| GitHub CLI version | `gh --version` | Not Run | Verifies GitHub CLI availability in the container. |
| Terraform formatting | `cd labs/terraform-local-foundation && terraform fmt -check -recursive` | Not Run | Safe formatting check only. |
| Terraform initialization without backend | `cd labs/terraform-local-foundation && terraform init -backend=false -input=false` | Not Run | Backend initialization is explicitly disabled. |
| Terraform validation | `cd labs/terraform-local-foundation && terraform validate -no-color` | Not Run | Safe validation check only. |
| Terraform tests | `cd labs/terraform-local-foundation && terraform test -no-color` | Not Run | Safe Terraform test execution only. |
| Speculative Terraform plan | `cd labs/terraform-local-foundation && terraform plan -input=false -lock=false -no-color` | Not Run | Speculative plan only; no apply. |

## Explicit Non-Actions

- `terraform apply` not executed.
- `terraform destroy` not executed.
- No cloud credentials used.
- No cloud authentication.
- No cloud resources provisioned.
