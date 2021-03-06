# Docker

## Build (with [Dockerfile](https://github.com/tatpongkatanyukul/Learn/blob/main/docker/Dockerfile) in the current directory .)
```
docker build -t my_image0 .
```

## List images
```
docker images
```

## List containers
```
docker ps
```

or
```
docker ps -a
```

## Run a container from an image
```
docker run my_image0
```

Note: files and directories of a docker container are different from the ones of the host!!!

## Run interactive mode from an image

```
docker run -v /home/tatpong/sandbox:/home/sandbox -it p35:201226 bash
```
where
  * Option ```-v``` is to bind a local ```/home/tatpong/sandbox``` to container ```/home/sandbox```
  * Option -it ```-it``` is to have it in the interactive mode
  * Token ```bash``` is the command to run. In this case, it is a bash shell.

```
docker run -v /home/tatpong/sandbox:/home/sandbox -it python39_image bash
```


```
docker run --rm -v /home/tatpong/sandbox:/home/sandbox -it p35:201226 bash
```
where
  * ```--rm``` to remove container after use (stop container)

## Save docker image to a tar file

```
docker save imgpy3np1 > imgpy3np1.tar
```

## Delete docker image
```
docker image rm --force imgpy3np1
```

  * stop: stop a container
  ```docker stop python_image```
  
  * rm: remove the image
    * Remove its containers first!
      * ```docker rm <container_id>``` 
      * ```docker rmi <image_id>```


## Load docker image from a tar file
```
docker load --input imgpy3np1.tar
```

## Create a docker image from a container

(src: https://www.scalyr.com/blog/create-docker-image/)

  * First, start the container of choice: e.g., ```docker run -v /home/tatpong/sandbox:/home/sandbox -it p35:201226 bash```
  * Modify it to our need: e.g., ```apt-get install nano```
  * Commit the container to an image: ```docker commit <container name>```
  * Tag the newly created image: e.g., ```docker tag <image id> <image tag>```

