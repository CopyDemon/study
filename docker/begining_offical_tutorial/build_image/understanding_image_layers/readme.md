# Build Images
[Content Reference link to Docker Official Document](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/)
## Understanding the image layers
Just like we learned before, the image is made up by layers, because of image is immutable, but it doesn't mean we can't change it. We can change image by adding new layer.  

## What is adding new layer?
By install anything on top of the image, we are adding a new layer to the image. When we build a image.

```yaml
# example:
# in this example, we are adding a new layer to the image
# the new layer is installing curl on top of the image
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y curl

# if we want to add another layer, we can do it like this, and new layer is installing vim on top of the image
RUN apt-get update && apt-get install -y vim
```

## Images can share layers
Just remember, if we have 2 or more images, they have some same dependencies, they can share the same layers.  

The benefit of this is that it can save space, because we don't need to download the same layer multiple times.

```yaml
# in this example you can see the App1 and App2 share the same layer of Python and pip
App1               App2
Layer1             Layer1
Layer2             Layer2
Layer3             Layer3
      Python and pip
       Debian base
```

### How Docker manage existing layers?
How can this happen?  
Docker is useing some string like SHA256 to identify each layer, so it can know if the layer already exists. 

For example, if we installed `Flask` at Jan, and in Docker Daemon it will store a string like information to remeber this layer and what it does. In future when other docker file run a exect same command, it will know ok we have that layer already, and it will create a pointer to point at that existing layer.

The layer change is a chain reaction, when docker build a SHA256 string, it will calculate one layer above. Which is means if second row changed, then when it calculate the third row, it will use the second row as the base, and calculate the third row. then the third row will be different from the first time, and same as the forth row.

How they change layers example:
```bash
FROM ubuntu:20.04       # layer1 (ID: A1)
RUN apt-get update      # layer2 (ID: B2)
RUN pip install flask   # layer3 (ID: C3)

# later

FROM ubuntu:20.04       # layer1 (ID: A1) - stay the same
RUN apt-get update && apt-get install curl # layer2 (ID: X9)
RUN pip install flask   # layer3... changed ... if forth row, also will be changed 
```

## How to avoid stuck in old layer?
1. Do not use the vague version number in the dockerfile
```bash
pip install flask # this is bad, because it will stack in the version we first installed flask.

# instead, we should use the specific version number
pip install flask==2.0.1    # this is good

# in future, if in other project we want use, lets say flask==3.0.2, it will create a new layer, because the string like of SHA256 is different
```

2. Other ways is to force docker to build without cache
```bash
docker build --no-cache -t my-flask-app .
```

## Stacking the layers
The stacking image is the fundemental of docker image, it is the base of docker image, and it is the base of docker container.

If you understand the image then this is not hard to understand.

Key things to remember:
1. Docker use union filesystems to manage the image
1. These base image are unchangeable, and they are the base of docker image
1. When build a new container and porform additation operation, a dictionary is created specifically for the container, and all layers on top of the base image are saved init


## Create your own image and commit changes
1. build a image

```bash
# what is flag --name -ti?
# --name is to name the container
# -ti are two flags, -t and -i
# -t is (tty: teletypewriter) it's a terminal
# -i is (interactive) it's a interactive mode with -i you can interact with the container terminal

# what is ubuntu do?
# ubuntu is a base image name, it's a offical base image
# first docker will check if we have in local, if not, it will pull from docker hub

docker run --name=base-container -ti ubuntu
```

Confused? Why run first?  
Because we can't directly build a image, so we have to start a container first, this container base on a existing image(Offical base image), then we can perform some operation on this container, and then commit it to save as a new image.  

Tricks & Tips:  
We know the flag -ti but what we may see when we input  different combination of flags?  

1. -t only: it will create a tty, but it will not create a interactive mode, you can see `root@container_id`, but when you type, it will not show anything.  (That root@... is printed text)

2. -i only: it will create a interactive mode, but it will not create a tty, you will only see a flash cursor indicator, and your computer looks frozen. But you can type and input command, and it will execute and response, and the format may look fuzzy, because there is no tty involved. `Sometimes user may use this mode to do some simple jobs like echo something or cat something`. 

3. -ti & -d: This is a trick way to run a docker container, which doesn't have `runtime running ("long-running process")` in that container. What does it mean? Some container like ubuntu base container will start and stop immediately, because it doesn't have any runtime to keep it running, but when we use the flag -ti docker think we want to interact with it, so it will keep contianer running. But we don't want to see the interactive terminal, so we use -d to let it run in the background. When we want to check the container, we can use docker exec to enter the container.

