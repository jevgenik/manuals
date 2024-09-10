================
Gazebo Simulator
================
Gazebo is an open-source 2D/3D robotics simulator that began development in 2002.

* `Official website <http://gazebosim.org/>`_

* `Gazebo GitHub <https://github.com/gazebosim>`_

* `Documentation <https://gazebosim.org/docs/latest/getstarted/>`_

* `Gazebo for ROS 2 installation <https://gazebosim.org/docs/latest/ros_installation/>`_

* `Gazebo for ROS 2 GitHub (roz_gz) <https://github.com/gazebosim/ros_gz/tree/ros2>`_

* `ROS 2 integration <https://gazebosim.org/docs/latest/ros2_overview/>`_


**ros_gz_bridge** - ROS 2 package that provides a network bridge which enables the exchange of messages 
between ROS 2 and Gazebo Transport
`Documentation <https://gazebosim.org/docs/latest/ros2_integration/>`_, 
`GitHub <https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_bridge>`_ 


SDF (Simulation Description Format)
===================================
SDFormat (Simulation Description Format), sometimes abbreviated as SDF, is an XML format that describes objects 
and environments for robot simulators, visualization, and control. Originally developed as part of the 
Gazebo robot simulator, SDFormat was designed with scientific robot applications in mind.

`Official website <http://sdformat.org/>`_


Commands
========

.. note::
   ``ign`` is used only for versions Fortress and and Citadel for new versions use ``gz`` e.g ``gz topic -l``

Topics
------

* ``ign topic -l`` - list all of the topics that are currently available in the Ignition transport system 

* ``ign tipic -t /topic_name -i`` - display information about a specific topic  

* ``ign topic -t /topic_name -e`` - echo topic /topic_name (-t - topic name. -e -echo)


Plugins
=======
Gazebo plugins are shared libraries (a chunk of code that is compiled as a shared library) that are 
inserted into the simulation. They can be used to model sensors, actuators, or controllers. 
Plugins are written in C++ and are loaded when the simulation starts. 

`Tutorial <https://gazebosim.org/docs/latest/moving_robot/>`_