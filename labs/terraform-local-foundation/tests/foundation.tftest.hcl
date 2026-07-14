run "valid_local_metadata" {
  command = plan

  variables {
    project_name = "ecpel"
    environment  = "dev"
    owner        = "platform-team"
    cost_center  = "learning"
    managed_by   = "terraform"
  }

  assert {
    condition     = output.normalized_project_name == "ecpel"
    error_message = "Expected normalized project name to be ecpel."
  }

  assert {
    condition     = output.generated_resource_prefix == "ecpel-dev"
    error_message = "Expected generated resource prefix to be ecpel-dev."
  }

  assert {
    condition     = output.normalized_metadata.environment == "dev"
    error_message = "Expected normalized environment to be dev."
  }

  assert {
    condition     = output.lab_summary == "ecpel-dev managed by terraform for platform-team"
    error_message = "Unexpected lab summary output."
  }
}
