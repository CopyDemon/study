#!/bin/bash

# start idaes_ui_container
task -t ./start_idaes_ui_container.yml

# display idaes_ui_container info
docker ps | grep idaes_ui_container

# trap cleanup SIGINT stop container and remove container
trap cleanup SIGINT

# Function to stop container and remove container by calling stop_idaes_ui_container.yml
cleanup() {
    echo "Stopping container..."
    task -t ./stop_idaes_ui_container.yml
    echo -e "\n Container stopped and removed \n"
    exit 0
}

