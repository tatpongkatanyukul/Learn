# Docker


## Windows

  * Docker for windows desktop
    * WSL 2 is not installed
> Install WSL using this PowerShell script (in an administrative PowerShell) and restart your computer before using Docker Desktop: Enable-WindowsOptionalFeature -Online -FeatureName $("VirtualMachinePlatform", "Microsoft-Windows-Subsystem-Linux")

      * https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/
        * download [wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
        * run wsl_update_x64.msi, but **FAIL!!!** (... ends prematurely because of errors ...)
