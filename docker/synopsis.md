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
  * Token ```bash``` is the command to run
