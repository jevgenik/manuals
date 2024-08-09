=======
Costmap
=======
A costmap is a representation of the robot environment that assigns a cost value to each cell 
based on the occupancy, obstacle distance, inflation radius, and other factors.

A costmap consists of multiple layers that stack on top of each other and combine their cost values. 
Each layer can have its own update frequency, data source, and parameters. 

The most common layers are static, obstacle, and inflation layers. 

* The static layer represents the fixed map of the environment, such as walls and furniture. 
* The obstacle layer detects and marks dynamic obstacles, such as people and other robots, using sensor data. 
* The inflation layer adds a buffer zone around the obstacles to account for the robot size and uncertainty.


Costmap 2D (ROS package)
========================
The Costmap 2D package implements a 2D grid-based costmap for environmental representations and a 
number of sensor processing plugins (AI outputs, depth sensor obstacle buffering, semantic information, etc)


OctoMap
=======
The OctoMap library implements a 3D occupancy grid mapping approach, providing data structures and 
mapping algorithms in C++ particularly suited for robotics. The map implementation is based on an octree.

`Official Website <https://octomap.github.io/>`_


ROS packages
============

* nav2_costmap_2d