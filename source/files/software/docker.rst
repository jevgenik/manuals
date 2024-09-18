======
Docker
======
Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. 

Containers allow a developer to **package up an application with all of the parts it needs**, such as libraries 
and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer 
can rest assured that the **application will run on any other Linux machine** regardless of any customized 
settings that machine might have that could differ from the machine used for writing and testing the code.

.. image:: /files/images/docker.png
   :alt: Docker

.. image:: /files/images/docker_build_and_run.jpg
   :alt: Docker Build and Run

Docker commands
===============

Commands related to images
--------------------------

* ``docker build -f Dockerfile.nav -t nav_cont:latest --build-arg BASE_IMAGE="nvidia_x86" ..`` - build image passing build-time variable BASE_IMAGE to docker file

.. note:: 
   Build-time variable *ARG BASE_IMAGE* in a docker file is accessable only during build time
  
* ``docker build --no-cache -t nav_cont:latest ..`` - rebuild image without cache (useful when you want to rebuild image with new dependencies)

* ``docker pull <image name>`` - pull an image from a registry (e.g. Docker Hub). When is called after image already pulled, it will pull the latest version of the image.

* ``docker history <image name>`` - show the history of an image (layers, size, etc)


Commands related to containers
------------------------------

Run docker containers with GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. ``xhost +local:root`` OR ``xhost +`` - allow any user to connect to your X server (This is not recommended for security reasons) To disable access, run ``xhost -``

#. ``docker run -it --rm --privileged --network host --runtime=nvidia --gpus all --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" nav_cont:latest``
   
   * ``--rm`` - automatically remove the container when it exits   
  
   * ``--privileged`` flag gives all capabilities to the container (i.e. device access)
  
   * ``--gpus`` flag when you start a container to access GPU resources. Specify how many GPUs to use (all - use all GPUs)  

   * ``env="DISPLAY"`` - pass the DISPLAY environment variable to the container
  
   * ``--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"`` this volume is needed to share the X11 socket with the container. Read-write mode (i.e. the container can write as well as read files on the host)

.. note::    
   If a container was started in attached mode (``docker run -it``), you can detach from the container without stopping it by pressing ``Ctrl + P + Q``   

Some more useful commands
~~~~~~~~~~~~~~~~~~~~~~~~~
  
* ``docker ps -a`` - list all containers (running and stopped)
  
* ``docker container ls -a`` - list all containers (running and stopped) it is alias for ``docker ps -a``

* ``docker compose ps`` - list containers for a Compose project, with current status and exposed ports (NB! should be run in the same directory where docker-compose.yml is located)

* ``docker exec -it <container-name/ID> bash`` - run bash in a running container


Inspect (containers, networks, images, volumes)
-----------------------------------------------

* ``docker inspect <container name> or <id>`` - show container info (IP address, etc)

* ``docker inspect <network name> or <id>`` - show network info

* ``docker inspect <image name> or <id>`` - show image info

* ``docker inspect <volume name> or <id>`` - show volume info


Free up disk space
------------------

* ``docker system df`` - show docker disk usage
  
* ``docker builder du`` - show disk usage by build cache

* ``docker system prune`` - cleans up dangling resources (unused data such as stopped containers, dangling images, networks, and more)

* ``docker system prune -a`` -a removes all unused images (those that are not associated with any container) not just the dangling ones. NB! all images will be removed

* ``docker builder prune`` - remove build cache


To capture docker build logs to a file
--------------------------------------

``docker build -f Dockerfile.bfb_camera_d435i -t bfb_camera_d435i:latest ../.. 2>&1 | tee build.log`` 2>&1 redirects stderr to stdout, 
and then | tee build.log pipes stdout to :ref:`tee <linux_text_manipulation>`, which writes it to build.log and also displays it on the screen.


Docker compose 
--------------

Create, start, stop and remove containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``docker compose -f docker-compose_lenovo.yml up``

* ``docker compose up``

* ``docker compose up --build`` (Build images before starting containers.)

* ``docker compose start``- start the stopped containers, can't create new ones

* ``docker compose down`` - stop and remove containers, networks, images, and volumes


Docker Installation
===================

1. `Docker Intallation Guide <https://docs.docker.com/engine/install/>`_

2. After installation, add your user to the docker group to avoid using sudo when you use the docker command:  
   ``sudo usermod -aG docker $USER``


Acess Nvidia GPUs in Containers (GPU-accelerated containers)
============================================================

**NVIDIA Container Toolkit** enables users to build and run GPU-accelerated containers. The toolkit includes a container 
runtime library and utilities to automatically configure containers to leverage NVIDIA GPUs.

`Official documentation <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html>`_

..note::
   
  This installation guide is for Linux only. In Windows GPU support is included in Docker Desktop.
  `Dockerdocs <https://docs.docker.com/desktop/gpu/>`_

1. Install Nvidia Container Toolkit:  
   `Nvidia Container Toolkit Installation Guide <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html>`_

2. Restart Docker:  
   ``sudo systemctl restart docker``

3. Test Nvidia Container Toolkit:  
   ``docker run -it --rm --gpus all ubuntu nvidia-smi``

4. Run your container with GPU support:  
   
   .. code-block:: bash      
      
      docker run -it --rm --runtime=nvidia \
      -e DISPLAY \
      -e NVIDIA_VISIBLE_DEVICES=all \
      -e NVIDIA_DRIVER_CAPABILITIES=all \
      -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
      <image name>``

* `Turn on GPU access with Docker Compose (Docker documentation) <https://docs.docker.com/compose/gpu-support/>`_

* `Specialized Configurations with Docker (NVIDA docs) <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html>`_