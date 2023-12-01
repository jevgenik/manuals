======
Docker
======
is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow 
a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, 
and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that 
the application will run on any other Linux machine regardless of any customized settings that machine might have 
that could differ from the machine used for writing and testing the code.

Docker commmands
================

Buid image
----------

* ``docker build -f Dockerfile.nav -t nav_cont:latest --build-arg BASE_IMAGE="nvidia_x86" ..`` - build image passing build-time variable BASE_IMAGE to docker file

.. note:: 
   Build-time variable *ARG BASE_IMAGE* in a docker file is accessable only during build time
  
* ``docker build --no-cache -t nav_cont:latest ..`` - rebuild image without cache (useful when you want to rebuild image with new dependencies)

* ``docker exec -it <container-name/ID> bash`` - run bash in a running container

--- Run docker containers with GUI ---
xhost +local:root 
OR
xhost +

docker run -it --rm --privileged --network host --runtime=nvidia --gpus all --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" aarch64_humble_realsense:latest  
(--rm Automatically remove the container when it exits)  
(--gpus # flag when you start a container to access GPU resources. Specify how many GPUs to use (all - use all GPUs))  
(--privileged flag gives all capabilities to the container, and it also lifts all the limitations enforced by the device cgroup controller.   
(--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" read-write mode (i.e. the container can write as well as read files on the host))  
In other words, the container can then do almost everything that the host can do)  

To capture docker build logs to a file
 `docker build -f Dockerfile.bfb_camera_d435i -t bfb_camera_d435i:latest ../.. 2>&1 | tee build.log`
 2>&1 redirects stderr to stdout, and then | tee build.log pipes stdout to tee, which writes it to build.log and also displays it on the screen.

--- end of block 'run docker containers wit GUI ---

--- Create and start containers
docker compose -f docker-compose_lenovo.yml up # Version2

docker-compose up
docker-compose up --build (Build images before starting containers.)

--- Start the stopped containers, can't create new ones
docker-compose start

--- Stop and remove containers, networks, images, and volumes
docker-compose down

List containers
---------------

``docker-compose ps`` - list running containers 
``docker ps -a`` - list all containers (running and stopped)
``docker container ls -a`` - list all containers (running and stopped) it is alias for ``docker ps -a``

--- Inspect (containers, networks, images, volumes)
`docker inspect <container name>` - show container info (IP address, etc)
   docker container inspect 2186a1927d6a | grep compose 
`docker inspect <network name>` - show network info
`docker inspect <image name>` - show image info
`docker inspect <volume name>` - show volume info

--- end of block 'docker commmands ---


### Free up disk space
`docker system prune` - cleans up dangling resources (unused data such as stopped containers, dangling images, networks, and more)
`docker system prune -a` -a removes all unused images (those that are not associated with any container) not just the dangling ones.
                         NB! all images will be removed