#!/bin/bash
echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
echo "||||||||||||||| Play Ground: |||||||||||||||"
echo "
play ground is use for test bash commands.
want to play? write bash code below, this file is already sourced to main.
"
echo "==================== START ===================="
















#ask user input:
echo "Enter your name:"
read name

if [[ -z $name ]]; then
    echo "we need your name"
fi;
echo "Hello $name"



# Try working on a file watching system
# Define a function
function fileChangeWatching(){
    echo "My watching dog..."
    script=$(cat ../main.bash)
    while true; do
        watchFile=$(cat ../main.bash)

        if [[$script != $watchFile]]; then
            echo "updated"
            script=$watchFile
            bash $script
        fi
        sleep 1
    done
}

# Execute function:
# fileChangeWatching


echo "====================  END  ===================="
echo "|||||||||||||||||||||||||||||||||||||||||||||"
echo "*************************************"