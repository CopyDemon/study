## What is a registry?

A registry is a service that stores and manages Docker images. It is a place where you can store and share your Docker images with others.   
For example:   
1. Docker Hub amazon elastic container registry(ECR)
1. Google Container Registry(GCR)
1. Azure Container Registry(ACR)

You even can run your own registry on your own server.  
For example:  
1. Harbor
1. GitLab Container Registry

### Is registry the same as repository?
Registry is not repository.  
Repository is a place where you store your images.  
Registry is a place where you store your repositories.  
You can think of registry as GitHub, and repository as a GitHub repository.  

### Newly learned command
When a folder contains dockerfile, we can use `docker build` to build an image, and run it.
* Build an image 
```bash
# example about how to build an image
# -t flag is for tag
docker build -t <yourDockerHubUsername/imageName> <pathToDockerfile>
```

* Tag an image  
```bash
# As default, the image is tagged with `latest` version. If you want to tag it with a specific version, you can use the following command:
docker tag <yourDockerHubUsername/imageName> <yourDockerHubUsername/imageName>:<versionNumber>
```

* List images
```bash
docker images
```

* Run an image
```bash
# run builded image
# -d is for detached mode (running in background)
# -p is for port mapping
docker run -d -p localPort:containerPort <yourDockerHubUsername/imageName>
```

* Stop a container
```bash
docker stop <containerId> # containerId can be any part of the container id
```

### How to tag and push an image to Docker Hub
* Tag an image
```bash
# The tag information can be anything, people usually use version number like v1.0.0.

# This tag is really like cp command in linux, in cp command we copy a file from a to b and in b we can rename it. In this tag command we tag image from a to b in b we can tag it.

# actual command
docker tag <yourDockerHubUsername/imageName> <yourDockerHubUsername/imageName>:<TagInformation>

# example:
docker tag userHubName/a userHubName/newName:vNewVersionOrAnyThing

```

* Push an image to Docker Hub
```bash
docker push <yourDockerHubUsername/imageName>:<versionNumber>
```
