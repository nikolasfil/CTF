#!/bin/bash
ip a | grep 'inet'

echo "Port 600"
docker run -p 600:500 no_response_ctf

# docker run -p host:port_inside_image -it (interctive , if you dont have a CMD in the end of the dockerfile)
#to stop it ,, docker ps and docker stop container_id

