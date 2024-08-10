====
SLAM
====
SLAM (Simultaneous Localization and Mapping) is a technique used in robotics to build a map of an unknown environment 
while simultaneously keeping track of the robot's location within it. 
This is a key technology for autonomous robots that need to operate in unknown environments.


Mapping
=======
Mapping is the process of creating a map of the environment.


Libraries and ROS packages
==========================

* RTAB-Map (Real-Time Appearance-Based Mapping) is a RGB-D, Stereo and Lidar Graph-Based SLAM approach. `GitHub <https://introlab.github.io/rtabmap/>`_

* `nav_msgs/OccupancyGrid <https://docs.ros.org/en/melodic/api/nav_msgs/html/msg/OccupancyGrid.html>`_ - represents a 2-D grid map, in which each cell represents 
  the probability of occupancy

* **gmapping** (g means grid because this algorithm uses a grid map) is a highly efficient Rao-Blackwellized particle filter to learn grid maps from laser range data  
`GitHub <https://openslam-org.github.io/gmapping.html>`_