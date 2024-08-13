====
SLAM
====
SLAM (Simultaneous Localization and Mapping) is a technique used in robotics to build a map of an unknown environment 
while simultaneously keeping track of the robot's location within it. 
This is a key technology for autonomous robots that need to operate in unknown environments.


:ref:`localization`

:ref:`mapping`


.. _loop_closure:
Loop Closure 
============
Loop Closure is the process by which a robot recognizes that it has returned to a previously visited location in its environment, 
even after traveling a significant distance or through complex paths. Detecting loop closure is essential for **reducing drift** in the 
robot’s estimated position and **improving the accuracy of the map** it is building.

Imagine being blindfolded, and then transported at the back of a car with armed kidnappers, 
only to be released near the Eiffel Tower. Suddenly, you realize "Hey, I know this place!" and you're (somewhat) relieved 
[`Source <https://www.thinkautonomous.ai/blog/loop-closure/>`_].

.. figure:: images/loop_closure.gif
   :width: 450px
   :alt: Loop Closure
   
Loop Closure. `Source <https://www.thinkautonomous.ai/blog/loop-closure/>`_


Libraries and ROS packages
==========================

* **SLAM Toolbox** is a set of tools and capabilities for 2D SLAM `GitHub <https://github.com/SteveMacenski/slam_toolbox`_
  It is also the currently supported ROS2-SLAM library. See tutorials for working with it in 
  `ROS 2 Nav2 here <https://docs.nav2.org/tutorials/docs/navigation2_with_slam.html>`_.

* RTAB-Map (Real-Time Appearance-Based Mapping) is a RGB-D, Stereo and Lidar Graph-Based SLAM approach. `GitHub <https://introlab.github.io/rtabmap/>`_

* `nav_msgs/OccupancyGrid <https://docs.ros.org/en/melodic/api/nav_msgs/html/msg/OccupancyGrid.html>`_ - represents a 2-D grid map, in which each cell represents 
  the probability of occupancy

* **GMapping** (G means grid because this algorithm uses a grid map) is a highly efficient Rao-Blackwellized particle filter to learn grid maps from laser range data  
  `GitHub <https://openslam-org.github.io/gmapping.html>`_