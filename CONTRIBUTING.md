# Contributing to ECPEL

## Repository Principle

"No evidence, no implementation."

Every contribution must keep repository claims aligned with evidence committed to the default branch. A design, simulation, validation result, or document may describe intent or learning progress, but it must not be presented as deployed infrastructure without supporting implementation evidence.

## Contribution Scope

Accepted contribution categories include:

- documentation;
- architecture decisions;
- labs;
- tests;
- workflows;
- operational templates;
- security improvements;
- cost and reliability improvements.

Contributions should be small, reviewable, and tied to one cohesive objective.

## Contribution Workflow

1. Start from the latest main branch.
2. Create one branch for one cohesive objective.
3. Keep changes within the approved scope.
4. Run applicable validation.
5. Open a Draft Pull Request.
6. Record real evidence.
7. Mark the Pull Request ready only after validation.
8. Merge only after required checks pass.
9. Delete the merged branch.

## Branch Naming

Branch names should make the contribution scope clear. Examples include:

- `docs/<scope>`
- `feat/<scope>`
- `fix/<scope>`
- `ci/<scope>`
- `chore/<scope>`
- `security/<scope>`

These examples describe preferred naming patterns; they do not claim automatic enforcement.

## Commit Messages

Use clear commit messages that describe the change. Conventional Commit-style prefixes are encouraged where helpful, for example:

- `docs:` for documentation changes;
- `feat:` for new capabilities;
- `fix:` for corrections;
- `ci:` for workflow or validation changes;
- `chore:` for maintenance;
- `security:` for security-focused improvements.

This repository does not currently claim automated Conventional Commit enforcement.

## Pull Request Expectations

Each Pull Request should include:

- clear summary;
- explicit scope;
- validation results;
- evidence;
- security considerations;
- cost considerations;
- known limitations;
- rollback or recovery guidance when applicable.

Use `Not Applicable` with an explanation when a section does not apply to the change.

## Status Model

Use the status terminology already defined by the repository roadmap and related documents. Do not introduce a competing status model.

Clarifications:

- **Simulated** is not **Implemented**.
- Validated documentation or tooling is not deployed cloud infrastructure.
- Documentation alone is not implementation evidence.
- A planned, researched, designed, or simulated capability must remain labeled accordingly until repository evidence supports a higher status.

## Validation

The existing Terraform Local Foundation workflow provides repository regression checks using:

- Terraform 1.6.0 local validation;
- Terraform 1.15.8 local validation.

These checks act as a repository regression gate, including for Pull Requests targeting `main`, but they do not validate every possible technology domain. Contributors must run and record additional validation when their change affects documentation links, templates, workflows, security assumptions, cost behavior, or other non-Terraform areas.

## Security

Do not commit:

- secrets;
- tokens;
- passwords;
- private keys;
- cloud credentials;
- account IDs when sensitive;
- customer data;
- personal data;
- internal endpoints.

Security-sensitive findings should not be disclosed publicly with exploitable details. Follow the repository security policy for reporting guidance.

## Cost Awareness

Document expected cost impact before introducing resources, workflows, or examples that could generate cost. If a change is local-only or documentation-only, state that clearly and avoid implying cloud resources were provisioned.

## Documentation Standards

Documentation contributions must include:

- valid relative links;
- clear Markdown structure;
- source references where relevant;
- no fabricated evidence;
- accurate current-state labels.

When linking to repository files, prefer relative links that work from the document location.

## Contributor Checklist

Before requesting review, confirm that:

- [ ] the Pull Request has one cohesive objective;
- [ ] only intended files are changed;
- [ ] status labels match repository evidence;
- [ ] validation results are recorded;
- [ ] links are checked;
- [ ] no secrets or sensitive information are included;
- [ ] security considerations are documented;
- [ ] cost considerations are documented;
- [ ] limitations are documented;
- [ ] no unsupported implementation claims are introduced.
