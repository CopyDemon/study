#!/bin/bash

# this file is auto made docker-compose build and run container
# if container already exist it will stop and remove it
# if image already exist it will remove it and build new image

# check if docker container is running if it is stop and remove it
if docker ps | grep -q 'idaes_ui'
then
   # stop and remove container
   docker stop idaes_ui
   docker rm idaes_ui
fi

# check if already have the image if it is remove it
if docker image list --format'{{.Repository}}' | grep -q 'idaes_ui'
then
   # remove image
   docker rmi idaes_ui
fi

# build docker image
docker-compose build

# run docker container
docker-compose up

echo "idaes_ui container started"