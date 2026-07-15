locals {
  normalized_project_name = lower(trimspace(var.project_name))
  normalized_environment  = lower(trimspace(var.environment))
  normalized_owner        = lower(trimspace(var.owner))
  normalized_cost_center  = lower(trimspace(var.cost_center))
  normalized_managed_by   = lower(trimspace(var.managed_by))
}
