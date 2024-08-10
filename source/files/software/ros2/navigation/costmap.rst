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


ROS packages and Interfaces
===========================

* *nav2_costmap_2d* is responsible for building a 2D costmap of the environment, consisting of several "layers" of data about the environment. 
  `GitHub <https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/README.md>`_

* `nav_msgs/OccupancyGrid <https://docs.ros.org/en/melodic/api/nav_msgs/html/msg/OccupancyGrid.html>`_ - represents a 2-D grid map, in which each cell represents 
  the probability of occupancy