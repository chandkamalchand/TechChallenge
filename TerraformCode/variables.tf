variable "prefix" {
  description = "A prefix used for all resources in this example"
  type        = string
  default     = "3tier"
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "East US"
}
