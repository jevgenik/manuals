================
Gazebo Simulator
================
Gazebo is an open-source 2D/3D robotics simulator that began development in 2002.

* `Official website <http://gazebosim.org/>`_

* `Gazebo GitHub <https://github.com/gazebosim>`_

* `Documentation <https://gazebosim.org/docs/latest/getstarted/>`_

* `Gazebo for ROS 2 installation <https://gazebosim.org/docs/latest/ros_installation/>`_

* `Packages that provide integration between ROS and Gazebo (roz_gz) <https://github.com/gazebosim/ros_gz/tree/ros2>`_

* `Demos showing how to use Gazebo Sim with ROS <https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_sim_demos>`_

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

* `Official website of SDFormat <http://sdformat.org/>`_

* `Gazebo SDF worlds GitHub <https://github.com/gazebosim/gz-sim/tree/gz-sim9/examples/worlds>`_

* `Gazebo SDF worlds tutorial <https://gazebosim.org/docs/latest/sdf_worlds/>`_


Commands
========

.. note::
   ``ign`` is used only for versions Fortress and and Citadel for new versions use ``gz`` e.g ``gz topic -l``

Topics
------

* ``ign topic -l`` - list all of the topics that are currently available in the Ignition transport system 

* ``ign topic -i -t /topic_name`` - display information about a specific topic  

* ``ign topic -e -t /topic_name`` - echo topic /topic_name (-e -echo, -t - topic name)


Plugins
=======
Gazebo plugins are shared libraries (a chunk of code that is compiled as a shared library) that are 
inserted into the simulation. They can be used to model sensors, actuators, or controllers. 
Plugins are written in C++ and are loaded when the simulation starts. 

`Tutorial <https://gazebosim.org/docs/latest/moving_robot/>`_


Sensors
-------
Gazebo provides a suite of sensors that can be attached to models. These sensors can be used to simulate
real-world sensors such as IMU, camera, LiDARs, depth camera, GPS and others.

* `Tutorial <https://gazebosim.org/docs/latest/sensors/>`_
* `Library of sensors on GitHub <https://github.com/gazebosim/gz-sensors>`_
* `Demo launch files for ROS 2 <https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_sim_demos/launch>`_


Moving the robot 
----------------
Gazebo provides plugins to simulate motor controllers.

* `Tutorial <https://gazebosim.org/docs/latest/moving_robot/>`_

* `SDF file containing a world and a robot <https://github.com/gazebosim/docs/blob/master/harmonic/tutorials/moving_robot/moving_robot.sdf>`_


Other Useful Information
========================

* `Gazebo Fuel <https://app.gazebosim.org/dashboard>`_ is a cloud service that provides a free library of robot models and environments. 
  Models can easily be added to a world running in the Gazebo GUI.

* Path to the default worlds: ``/usr/share/ignition/ignition-gazebo6/worlds`` (for Fortress)

* Path to the resources downloaded from Fuel: ``~/.ignition/fuel``