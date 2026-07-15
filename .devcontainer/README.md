# ECPEL Development Container

## Status

Designed — validation pending

## Purpose

This development container defines a minimal, reproducible Ubuntu-based environment for working on ECPEL in GitHub Codespaces or VS Code Dev Containers. It supports repository editing, Git and GitHub CLI workflows, Markdown authoring, and the existing Terraform Local Foundation Lab.

The environment is intentionally local-development focused. It does not configure cloud deployment tools, cloud credentials, remote state, or cloud provider authentication.

## Included Tools

The development container configures the following tools:

- Terraform 1.15.8, installed through the official Development Containers Terraform Feature.
- Git, provided by the official Development Containers Ubuntu base image.
- GitHub CLI, installed through the official Development Containers GitHub CLI Feature.
- VS Code HashiCorp Terraform extension for Terraform editing.
- VS Code markdownlint extension for Markdown editing.

## Supported Environments

- GitHub Codespaces
- VS Code Dev Containers

## Creating a Codespace

To test this environment in GitHub Codespaces:

1. Open the repository on GitHub.
2. Select **Code**.
3. Select **Codespaces**.
4. Create a codespace from the PR branch under test.
5. Use the default machine type unless stronger resources are genuinely needed.

Do not mark this environment as validated until a real Codespace successfully builds and the validation commands below execute in that Codespace.

## Validation Commands

Run the following commands inside the development container or Codespace:

```sh
terraform version
git --version
gh --version
```

Then run the existing safe Terraform Local Foundation Lab checks:

```sh
cd labs/terraform-local-foundation
terraform fmt -check -recursive
terraform init -backend=false -input=false
terraform validate -no-color
terraform test -no-color
terraform plan -input=false -lock=false -no-color
```

Do not run `terraform apply` or `terraform destroy` as part of development container validation.

## Security Boundaries

- No cloud credentials are required.
- No cloud login is performed.
- No provider is configured by the dev container.
- No remote state is configured.
- No cloud resources are created.
- Secrets must not be committed.

## Cost Considerations

GitHub Codespaces may consume account quota or generate usage according to the user's GitHub plan. Review the applicable GitHub plan limits and billing settings before creating or leaving Codespaces running.

## Rebuild and Cleanup

To rebuild the container in GitHub Codespaces, use the Codespaces interface or the VS Code command palette action to rebuild the container.

To clean up, delete the Codespace through the GitHub Codespaces interface when testing is complete.

## Evidence

Validation evidence is tracked in [evidence/README.md](evidence/README.md).

## Limitations

The configuration file alone is not evidence of a successful Codespaces build. The environment remains Designed — validation pending until a real Codespace is created, builds successfully, and the documented validation commands are executed with recorded results.
