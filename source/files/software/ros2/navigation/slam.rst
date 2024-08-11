====
SLAM
====
SLAM (Simultaneous Localization and Mapping) is a technique used in robotics to build a map of an unknown environment 
while simultaneously keeping track of the robot's location within it. 
This is a key technology for autonomous robots that need to operate in unknown environments.


:ref:`localization`

:ref:`mapping`


Loop Closure 
============
Loop Closure is what helps a robot understand that an object has already been visited, and therefore the robot will update 
its location and the map accordingly.

Imagine being blindfolded, and then transported at the back of a car with armed kidnappers, 
only to be released near the Eiffel Tower. Suddenly, you realize "Hey, I know this place!" and you're (somewhat) relieved 
[`Source <https://www.thinkautonomous.ai/blog/loop-closure/>`_].

.. figure:: images/loop_closure.gif
   :width: 450px
   :alt: Loop Closure
   
   Loop Closure. `Source <https://www.youtube.com/watch?v=OV6wNr62nqQ>`_


Libraries and ROS packages
==========================

* RTAB-Map (Real-Time Appearance-Based Mapping) is a RGB-D, Stereo and Lidar Graph-Based SLAM approach. `GitHub <https://introlab.github.io/rtabmap/>`_

* `nav_msgs/OccupancyGrid <https://docs.ros.org/en/melodic/api/nav_msgs/html/msg/OccupancyGrid.html>`_ - represents a 2-D grid map, in which each cell represents 
  the probability of occupancy

* **gmapping** (g means grid because this algorithm uses a grid map) is a highly efficient Rao-Blackwellized particle filter to learn grid maps from laser range data  
  `GitHub <https://openslam-org.github.io/gmapping.html>`_