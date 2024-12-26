=============
NVIDIA Jetson 
=============
Nvidia Jetson is a series of embedded computing boards from Nvidia.
Jetson devices carry a Tegra SoC from Nvidia that integrates an ARM architecture CPU and a GPU.

Jetson is a low-power system and is designed for accelerating machine learning applications


Useful resources
================

* `Official NVIDIA Jetson page <https://developer.nvidia.com/embedded-computing>`_
* `Jetson Software Documentation <https://docs.nvidia.com/jetson/>`_
* `Jetpack SDK <https://developer.nvidia.com/embedded/jetpack>`_
* `How to Install and Configure JetPack SDK <https://docs.nvidia.com/jetson/jetpack/install-setup/index.html>`_ 
* `SDK Manager <https://developer.nvidia.com/sdk-manager>`_ - end-to-end development environment setup solution for NVIDIA’s Jetson, Holoscan and other SDKs
* `JetsonHacks <https://jetsonhacks.com/>`_
* `NVIDIA Isaac ROS <https://nvidia-isaac-ros.github.io/>`_ - a collection of NVIDIA-accelerated, high performance, low latency 
  ROS 2 packages for making autonomous robots which leverage the power of Jetson and other NVIDIA platforms.


Tools
=====

* ``nvidia-smi`` - NVIDIA System Management Interface program. Provides monitoring and management capabilities for NVIDIA GPUs (not available on Jetson devices)

* ``jetson-stats`` (command ``jtop``) - A package to monitor and control your NVIDIA Jetson [Xavier NX, Nano, AGX Xavier, TX1, TX2] embedded board. 
  It is a collection of various tools to monitor the system, including CPU, GPU, and RAM usage, temperature, and power consumption.
  `Repository <https://github.com/rbonghi/jetson_stats>`_

* ``prime-select`` - Command-line tool to switch between Intel and NVIDIA graphics cards on Ubuntu (on hybrid systems)

* ``nvidia-settings`` - GUI tool to configure the NVIDIA graphics driver

* ``glxinfo | grep "OpenGL renderer"`` - to check the OpenGL renderer (to make sure the NVIDIA GPU is being used)
  (install: ``sudo apt install mesa-utils``)
  
  - ``glxinfo -B`` - to get more detailed information about 3D acceleration setup


Nvidia Jetson Xavier NX Setup
=============================

1. Install Nvidia SKD Manager on your host machine
