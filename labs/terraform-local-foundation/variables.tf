variable "project_name" {
  description = "Short project name used to build local naming examples."
  type        = string
  default     = "ecpel-local-foundation"

  validation {
    condition     = length(trimspace(var.project_name)) > 0
    error_message = "project_name must not be empty."
  }

  validation {
    condition     = can(regex("^[a-zA-Z][a-zA-Z0-9-]{1,30}$", var.project_name))
    error_message = "project_name must start with a letter and contain only letters, numbers, or hyphens, with length from 2 to 31 characters."
  }
}

variable "environment" {
  description = "Local lab environment label."
  type        = string
  default     = "local"

  validation {
    condition     = contains(["local", "dev", "test", "sandbox"], lower(var.environment))
    error_message = "environment must be one of: local, dev, test, sandbox."
  }
}

variable "owner" {
  description = "Fictional owner or team name for local metadata examples."
  type        = string
  default     = "platform-team"

  validation {
    condition     = length(trimspace(var.owner)) > 0
    error_message = "owner must not be empty."
  }
}

variable "cost_center" {
  description = "Fictional cost center used for local metadata examples."
  type        = string
  default     = "learning"

  validation {
    condition     = can(regex("^[a-zA-Z0-9-]{2,32}$", var.cost_center))
    error_message = "cost_center must contain only letters, numbers, or hyphens, with length from 2 to 32 characters."
  }
}

variable "managed_by" {
  description = "Tool or process that manages this local lab metadata."
  type        = string
  default     = "terraform"

  validation {
    condition     = can(regex("^[a-zA-Z0-9-]{2,32}$", var.managed_by))
    error_message = "managed_by must contain only letters, numbers, or hyphens, with length from 2 to 32 characters."
  }
}
