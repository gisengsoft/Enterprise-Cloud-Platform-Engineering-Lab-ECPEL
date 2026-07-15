# Naming Module

This local-only module normalizes metadata values and produces a deterministic naming prefix.

It does not configure providers, remote state, cloud services, or external infrastructure.

## Inputs

- `project_name`
- `environment`
- `owner`
- `cost_center`
- `managed_by`

## Outputs

- `normalized_project_name`
- `resource_prefix`
- `normalized_metadata`
- `lab_summary`

The root module exposes `generated_resource_prefix` as the public output name for this prefix.

## Status

Simulated. This module is part of the Terraform Local Foundation Lab and must not be treated as production-ready infrastructure code or evidence of cloud infrastructure implementation.
