.. _localization:

============
Localization
============
Localization is the process of determining where a mobile robot is located with respect to its environment.

.. image:: images/localization_discrete.png   
   :alt: Localization Discrete probability function

.. image:: images/localization_continuous.png   
   :alt: Localization Continuous probability function


Local Localization
==================
Local localization involves determining the robot's position relative to a **known starting point** or within a small, 
well-defined area. It assumes that the robot has a good initial estimate of its position, and it focuses on maintaining 
or refining that estimate as the robot moves.

.. note::
   "Local" localization because uncertainty is local and confined to a region near the robot's true pose.

Scope: It usually operates in a local coordinate frame (``/odom``) and is often concerned with small adjustments or 
corrections in position and orientation as the robot moves.

**Technologies/Methods:**

* Odometry: Tracking movement using wheel encoders.

* IMU (Inertial Measurement Unit): Providing data on acceleration and rotation to help estimate changes in position.

* SLAM (Simultaneous Localization and Mapping): In a local context, SLAM can be used to keep track of the robot’s position relative to a recently generated local map.

* Laser Scans or Visual Odometry: Using local sensor data to refine the robot’s current position estimate.


Global Localization
===================
Global localization involves determining the robot’s position within a larger, often **pre-defined, map** or environment **without** 
any prior knowledge of the robot’s **starting position**. It is used when the robot needs to determine its location within an 
entire environment, which could be a large building or outdoor area.

.. note::
   "Global" localization because uncertainty can be spread across the entire map.
   Global localization aka pose estimation

Scope: It operates on a global coordinate frame (``/map`` or ``/world``), often involving a large map where the robot's position is initially unknown.

**Technologies/Methods:**

* GPS: Commonly used for outdoor environments to provide global position estimates.

* Particle Filters or Monte Carlo Localization (MCL): These probabilistic methods can estimate the robot's global position by sampling multiple hypotheses of the robot's location.

* Map Matching: Matching sensor data (like LiDAR scans) with a global map to estimate position.

* :ref:`loop_closure` Detection in SLAM: Detecting when the robot revisits a known location to refine its global position estimate.

* ROMAN(Robust Object Map Alignment Anywhere). ROMAN is a view-invariant global localization method that maps open-set objects and uses the geometry, 
  shape, and semantics of objects to find the transformation between a current pose and previously created object map.
  This enables loop closure between robots even when a scene is observed from opposite views. `More Information <https://acl.mit.edu/ROMAN/>`_


Local localization is precise and focused on the immediate surroundings, useful for fine-tuning the robot's movement and avoiding obstacles. 
Global localization, on the other hand, is about finding the robot's place in the broader context of its environment, 
which is crucial for overall navigation and task planning.


Algorithms
==========

* **AMCL (Adaptive Monte Carlo Localization)** is a probabilistic algorithm that uses a particle filter to estimate    
  a robot's 2D pose based on sensor data. The algorithm works by representing the robot's pose as a distribution  
  of particles, where each particle represents a possible pose of the robot  


ROS Packages and Interfaces
===========================

* **nav2_amcl** - Adaptive Monte Carlo Localization (AMCL) is a probabilistic localization module which estimates the position 
  and orientation (i.e. Pose) of a robot in a given known map using a 2D laser scanner. `GitHub <https://github.com/ros-navigation/navigation2/tree/main/nav2_amcl>`_

* `geometry_msgs/Pose <https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Pose.html>`_ - a representation of pose in free space, composed of position and orientation

* **roman_ros** - ROS package for ROMAN (Robust Object Map Alignment Anywhere) global localization method. `GitHub <https://github.com/mit-acl/roman_ros>`_