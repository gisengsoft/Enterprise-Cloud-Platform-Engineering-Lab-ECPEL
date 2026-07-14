output "normalized_project_name" {
  description = "Lowercase normalized project name."
  value       = local.normalized_project_name
}

output "resource_prefix" {
  description = "Deterministic local naming prefix."
  value       = local.resource_prefix
}

output "normalized_metadata" {
  description = "Normalized metadata map."
  value       = local.normalized_metadata
}

output "lab_summary" {
  description = "Human-readable local lab summary."
  value       = local.lab_summary
}
