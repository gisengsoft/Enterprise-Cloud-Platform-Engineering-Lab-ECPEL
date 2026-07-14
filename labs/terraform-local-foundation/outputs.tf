output "normalized_project_name" {
  description = "Normalized project name produced by the naming module."
  value       = module.naming.normalized_project_name
}

output "generated_resource_prefix" {
  description = "Generated local naming prefix for demonstration only."
  value       = module.naming.resource_prefix
}

output "resource_prefix" {
  description = "Backward-readable alias for the generated local naming prefix."
  value       = module.naming.resource_prefix
}

output "normalized_metadata" {
  description = "Normalized metadata map for local lab demonstration."
  value       = module.naming.normalized_metadata
}

output "lab_summary" {
  description = "Human-readable local lab summary."
  value       = module.naming.lab_summary
}
