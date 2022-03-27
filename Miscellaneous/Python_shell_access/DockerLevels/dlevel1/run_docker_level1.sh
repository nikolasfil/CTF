#!/bin/bash

ip a | grep 'inet'
echo "Port 601"
docker run -p 601:500 python_shell_level1

# docker run -p host:port_inside_image -it (interctive , if you dont have a CMD in the end of the dockerfile)
#to stop it ,, docker ps and docker stop container_id
