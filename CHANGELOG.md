# Changelog

This document records notable repository changes. Its structure is compatible with common changelog practices, but it does not declare a formal release process or retroactively define earlier Pull Requests as software releases.

## Unreleased

### Added

- Completed 2026 market-analysis artifacts, including the Cloud Market Matrix and derived roadmap.
- Validated development container support for GitHub Codespaces and VS Code Dev Containers.
- Terraform Local Foundation **Simulated** lab with GitHub-hosted regression validation that provisions no cloud resources.
- ADR-0007 platform-hub boundary documentation.
- ADR-0008 limited Ansible adoption for initial Linux configuration management.
- Ansible Local Foundation PR 1 static scaffold with dependency locking, static playbooks, inventory, guardrail tests, and non-functional evidence boundaries.
- Ansible workflow scope correction that permits unrelated Pull Request paths while preserving Ansible guardrails for relevant pushes and manual validation.
- Adopted the Apache License, Version 2.0, through a root `LICENSE` file and added the root `NOTICE` attribution file.
- Repository contributing guide covering scope, workflow, status terminology, validation, security, cost awareness, documentation standards, and contributor checklist.
- Security policy defining reporting guidance, sensitive information boundaries, response expectations, and security limitations.
- Project-specific Code of Conduct for respectful, evidence-based collaboration.
- Pull Request template for summary, scope, evidence, validation, security, cost, operations, documentation, limitations, rollback, and review checks.
- GitHub Issue Forms for bug reports and feature requests.
