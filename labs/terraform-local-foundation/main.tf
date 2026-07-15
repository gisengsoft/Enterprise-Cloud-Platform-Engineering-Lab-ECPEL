module "naming" {
  source = "./modules/naming"

  project_name = local.normalized_project_name
  environment  = local.normalized_environment
  owner        = local.normalized_owner
  cost_center  = local.normalized_cost_center
  managed_by   = local.normalized_managed_by
}
