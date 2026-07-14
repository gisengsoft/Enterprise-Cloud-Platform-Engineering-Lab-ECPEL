locals {
  normalized_project_name = lower(trimspace(var.project_name))
  normalized_environment  = lower(trimspace(var.environment))
  resource_prefix         = "${local.normalized_project_name}-${local.normalized_environment}"

  normalized_metadata = {
    project_name = local.normalized_project_name
    environment  = local.normalized_environment
    owner        = lower(trimspace(var.owner))
    cost_center  = lower(trimspace(var.cost_center))
    managed_by   = lower(trimspace(var.managed_by))
  }

  lab_summary = "${local.resource_prefix} managed by ${local.normalized_metadata.managed_by} for ${local.normalized_metadata.owner}"
}
