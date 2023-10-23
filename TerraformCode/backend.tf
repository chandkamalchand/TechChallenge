terraform {
  backend "azurerm" {
    resource_group_name   = "rg_sa"
    storage_account_name = "testsaterraformcode"
    container_name       = "newcontainer"
    key                  = "terraform.tfstate"
  }
}
