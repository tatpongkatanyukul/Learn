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

[Docker Tutorial for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)
  * [Public docker images at Docker Hub](https://hub.docker.com/)
  * run command
    * start a container
    * run and exit immediately
    * `docker run -d <image>` # detach mode/background mode
    * `docker attach <docker id>` # attach mode/get the backgroud docker to foreground
    * run does not take host input. If we want a host input, we have to map a host input to a docker container.
      * `docker run -i <image>` # interactive mode
      * `docker run -it <image>` # interactive mode + sudo terminal
    * `docker run -p 80:5000 <image>` # map port 80 for port 5000   
    * `docker run -v /external-data-path:/contain-path <image>` # map external path to container 
      * e.g., ```docker run -v /home/tatpong/sandbox:/home/sandbox -it p35:201226 bash```
    * `docker logs <image>` # ???
    * `docker run <image> [command]`
    
  * ps: list containers
    * `docker ps -a`
  * stop: stop a container
    * `docker stop python_image`
  * rm: remove the image
  * docker images
  * remove images: `docker rmi <image>`
  * `docker pull <image>`
    * just pull the image, but not run the command
  * exec: execute a command on a running container


How to create my own image?

Dockerfile
```
FROM Ubuntu

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run

```

```docker build Dockerfile -t <image-app>```


Dockerfile 2 is equivalent to ```docker run ubuntu sleep 5```
```
FROM Ubuntu

CMD ["sleep", "5"]
```

Dockerfile 3 is equivalent to ```docker run ubuntu sleep [default 5]```
```
FROM Ubuntu

ENTRYPOINT ["sleep"]

CMD ["5"]
```

Default networks

```docker run Ubuntu --network=host```

Clone a container

```docker commit --message="Snapshot of my container" <my_container|container id> my_container_snapshot:yymmdd```
  * see container id from ```docker ps -a```

---

## When building Docker fails, Docker may collapse.

To fix: https://docs.docker.com/docker-for-windows/install/
  * install linux on windows
  * switch daemon: ```C:\"Program Files"\Docker\Docker\DockerCli.exe -SwitchDaemon```


# Docker on Autolab

```
docker run -it python35_image bash
python3.5 myprog.py
```

```
docker run -v /home/tatpong/sandbox:/home/sandbox -it p35:201226 bash
```

# Docker on Mac

## Tutorial

Build
```
docker run --name repo alpine/git clone https://github.com/docker/getting-started.git
docker cp repo:/git/getting-started/ .
```

