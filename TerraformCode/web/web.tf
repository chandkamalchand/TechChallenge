resource "azurerm_virtual_machine" "web" {
  name                  = "${var.prefix}-web"
  location              = var.location
  resource_group_name   = var.resource_group_name
  network_interface_ids = [azurerm_network_interface.web.id]
  vm_size               = "Standard_F1s"

  storage_os_disk {
    name              = "myOsDisk3"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  storage_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2016-Datacenter"
    version   = "latest"
  }

  os_profile {
    computer_name  = "hostname"
    admin_username = "testadmin"
    admin_password = "Password1234!"
  }

  os_profile_windows_config {}
}

resource "azurerm_network_interface" "web" {
  name                = "${var.prefix}-web-nic"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "myNicConfiguration"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
  }
}

output "web_ip" {
  value = azurerm_network_interface.web.private_ip_address
}
