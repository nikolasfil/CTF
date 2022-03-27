#!/bin/bash

ip a | grep 'inet'
echo "Port 605"
docker run -p 605:500 python_shell_level5

# docker run -p host:port_inside_image -it (interctive , if you dont have a CMD in the end of the dockerfile)
#to stop it ,, docker ps and docker stop container_id
