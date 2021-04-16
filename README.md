## For Intro to Docker Workshop. ##

Adapted from  [Docker demo](https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md).

Edited with images that work from [Lorem Picsum](https://picsum.photos/images).

## Run ##

docker build -t <DOCKER_HUB_USERNAME>/myfirstapp

docker run -p 8888:5000 --name myfirstapp <DOCKER_HUB_USERNAME>/myfirstapp
