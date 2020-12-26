# Docker


## Windows

  * Docker for windows desktop
    * WSL 2 is not installed
> Install WSL using this PowerShell script (in an administrative PowerShell) and restart your computer before using Docker Desktop: Enable-WindowsOptionalFeature -Online -FeatureName $("VirtualMachinePlatform", "Microsoft-Windows-Subsystem-Linux")

Fix the problem
  * https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/
    * download [wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
    * run wsl_update_x64.msi, but **FAIL!!!** (... ends prematurely because of errors ...)
      * first, it did not work, perhaps because windows installer was busy with the update patches sneakingly downloaded by the windows.
      * after rebooting and letting the windows update to finish, it works!
    * run **PowerShell** as administrator
    * type "wsl --set-default-version 2"
  * after installing WSL 2, uninstall the docker and reinstall it again.
