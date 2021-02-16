# Docker

Feb 16th, 2021.
Tried
```
docker build Dockerfile -t my_image0
```
Result:
```
=> ERROR [internal] load build definition from Dockerfile
     :
     
Failed to solve with frontend dockerfile.v0: failed to read dockerfile: error from sender: walk Dockerfile: not a directory
```

Fix --> Docker application > click troubleshoot (bug icon) > restart docker desktop | clean/purge data

Tried
```
docker build . -t my_image0
```

Result:
```
Sending build context to Docker daemon  176.1kB
Error response from daemon: dial unix docker.raw.sock: connect: connection refused
```

Tried:
```
docker build -t my_image0 .
```

Result: this seems to work!!!
