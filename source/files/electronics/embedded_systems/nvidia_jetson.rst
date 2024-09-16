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

* ``nvidia-smi`` - NVIDIA System Management Interface program. Provides monitoring and management capabilities for NVIDIA GPUs

* ``jtop`` - Jetson System Monitoring Tool. A ``top``-like tool for monitoring the system (CPU, GPU, RAM, etc.)

* ``prime-select`` - Command-line tool to switch between Intel and NVIDIA graphics cards on Ubuntu (on hybrid systems)

* ``nvidia-settings`` - GUI tool to configure the NVIDIA graphics driver

* ``glxinfo | grep "OpenGL renderer"`` - to check the OpenGL renderer (to make sure the NVIDIA GPU is being used)
  (install: ``sudo apt install mesa-utils``)