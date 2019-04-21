## Build docker image

    $ docker build -t girnara/nameko-gateway:1.0.0 -f docker.run .


## Push Docker image
    $ docker push girnara/nameko-gateway:1.0.0


## Ssh to Docker box
 ```
 $ docker run -i -t girnara/nameko-gateway:1.0.0 /bin/bash
 ```
