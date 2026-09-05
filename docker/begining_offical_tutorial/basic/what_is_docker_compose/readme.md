## What is Docker Compose
Compose is a tool to deal with multi-container. It's write in YAML file, and we define how different containers are linked to each other and how to run them.  

### Naming in docker compose
<p style="color:cyan;">
In compose.yaml, each thing like web, db, proxy are called service. The thing running service is called container. and the result of compose is called project(stack).
</p>

## Learned commands
* Compose and build  

<p style="color:orange;">
* All compose related command MUST running within the folder has compose.yaml file, or it will throw error.
</p>

Everytime when we make changes to the YAML file, we need to run this command to apply the changes.  

This command can repackage the image and restart the container. If we only change port mapping, we don't need to `--build`, because these changes related to container, docker could check changes and apply changes to existing container intelligently. If we changed context, we need to `--build` to repackage the image because the changes related to image.  

```bash
# make sure pwd has docker-compose.yml
# -d means run in background
# --build means build the image

$ docker compose up -d --build
```

* Teardown running containers (which started with compose)
```bash
# because we in the folder has compose.yaml, so we can use docker compose down and docker know which container to teardown
$ docker compose down
```

*Teardown volumes
```bash
# because we in the folder has compose.yaml, so we can use docker compose down and docker know which volumes to teardown

# --volumes means teardown volumes
$ docker compose down --volumes
```



