#!/bin/bash --login

sudo docker ps -a | grep news_api | awk '{print $1}' | xargs sudo docker rm -f 
sudo docker images | grep news_api | awk '{print $3}' | xargs sudo docker rmi -f 


