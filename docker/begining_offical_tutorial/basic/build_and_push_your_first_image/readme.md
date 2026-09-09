## Build and push your first image

### What we do here:
We clone the offical getting-started repository, build an image from it, and push it to Docker Hub.

### What we learn here:
1. docker hub is the go-to place to host your images
1. learned how to build and push an image to docker hub
1. learned how to remove an image
1. learned some docker commands:
    - [check detail for command in reference part.](#learned-command-reference)
    - `docker image ls`: list all images
    - `docker image rm`: remove an image
    - `docker image rm -f`: remove an image, `-f` flag use to force remove a running image
    - `docker build`: build an image
    - `docker push`: push an image to docker hub

### learned command reference:
List all images
```bash
# list all images
docker image ls
```
Remove an image
```bash
# remove an image, `-f` flag use to force remove a running image. 
docker image rm imageName
# or
docker image rm -f imageName
```
Build an image
```bash
# build an image is docker build imageName

# -t flag use to tag an image, if no tag it will show hash name and hard to remember and use.

# userName is the username on Docker Hub, packageName is the name of the package, you can think packageName as same as repository name.

# . is the path to the build context, it is the path to the directory where the Dockerfile is located.

docker build -t userNameCaseSensitive/packageName . 
```

Push an image to docker hub
```bash
# push an image to docker hub

# userNameCaseSensitive/packageName usually copy from the docker hub page package name

docker push userNameCaseSensitive/packageName
```
