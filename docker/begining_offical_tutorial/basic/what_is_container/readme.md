## What is a container

A container is a self-contained unit of software that includes everything needed to run an application, including the code, runtime, system tools, system libraries, and settings.

### What we learned here
1. How to search a image from Docker Hub
2. How to pull a image from Docker Hub
3. How to run a container from an image
4. How to list all running containers

## Command reference

Search image from Docker Hub with terminal command:
```bash
docker search <image_name>
```

Pull image from Docker Hub with terminal command:
```bash
docker pull <image_name>
```

Build a container from image with terminal command:
```bash
docker run <image_name>

# example
docker run -d -p 8080:80 docker/welcome-to-docker

# 注意：这个每次运行都会创建一个新的container
# 如果想要运行已有container，可以使用 docker start <container_id>
# 如果想要停止container，可以使用 docker stop <container_id>

# -d 代表 Detached（分离模式/后台运行）。
# -p 代表 Port（端口映射）。
# 后台运行：容器启动后会立即在后台运行，不会占用你的当前终端窗口。
# 释放终端：你可以继续在当前终端输入其他命令。
# 只显示 ID：启动成功后，它只会打印出一串长长的容器 ID，而不会打印容器内部的日志（你可以用 docker logs <容器ID> 随时查看日志）。
# 不加 -d (默认)：容器在前台运行。你会看到所有的启动日志，但你的终端会被“卡住”，直到你按 Ctrl+C 停止容器。
# 加上 -d：容器在后台默默工作。就像你在 Windows/Mac 上最小化了一个程序一样。
# -p 8080:80：将主机的 8080 端口映射到容器的 80 端口。
```

List all running containers with terminal command:
```bash
docker ps

# to show all containers we need to use -a flag (including stopped ones)
docker ps -a
```

Show history of docker container command
```bash
docker history <image_name>
```

Stop a container with terminal command:
```bash
# the container id has no need to be a full id, just enough to identify the container is enough
docker stop <container_id>
```

## Image vs Container
- **Image**: A read-only template with instructions for creating a Docker container. It's like a **Class** in OOP or a **Recipe** in cooking. When you pull from Docker Hub, you are pulling an Image.
- **Container**: A runnable instance of an image. It's like an **Object** in OOP or the **Cake** baked from the recipe.
- **Relationship**: You create a container *from* an image.

## `docker run` vs `docker start`
- `docker run <image>`: **Creates a NEW container** from the image and starts it. If you run this command 10 times, you will have 10 separate containers.
- `docker start <container_id>`: Starts an **existing** (stopped) container.

## Development Workflow
1. **Local Development**: Write code, `docker build` locally to test. Do NOT push image to Docker Hub yet.
2. **Code Sharing**: `git push` code to GitHub. Colleagues `git pull` code and build their own local images to test.
3. **Review & Merge**: Open a Pull Request (PR). After review, merge code to `main`/`master` branch.
4. **Release**: 
    - **Manual**: You pull the latest `main` branch, build the final image, and `docker push` to Docker Hub.
    - **Automated (CI/CD)**: GitHub Actions (or similar) detects the merge to `main`, automatically builds the image, and pushes it to Docker Hub.