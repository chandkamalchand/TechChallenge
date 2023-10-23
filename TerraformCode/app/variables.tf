variable "prefix" {
  description = "A prefix used for the resources"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
}

variable "subnet_id" {
  description = "Subnet ID for the VM"
  type        = string
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "East US"
}
