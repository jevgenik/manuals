========
Odometry
========
Odometry is the use of data from motion sensors to estimate change in position over time. It is used in robotics  
by some legged or wheeled robots to estimate their position relative to a starting location.

.. tip::
   Origin of word "odometry": Greek hodos (way) + metron (measure).

Visual Odometry
===============
Visual odometry is the process of determining the position and orientation of a robot by analyzing the associated camera images.


VIO (Visual Inertial Odometry)
------------------------------
Visual Inertial Odometry is like Visual Odometry but it also uses data from an Inertial Measurement Unit (IMU) to estimate the position 
and orientation of a robot.


ROS packages and messages
=========================

* `geometry_msgs/Twist <https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html>`_ - this expresses velocity in free space broken into its linear and angular parts

* `geometry_msgs/Pose <https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Pose.html>`_ - a representation of pose in free space, composed of position and orientation

* `nav_msgs/Odometry <https://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html>`_ - this represents an estimate of a position (Pose) and velocity (Twist) in free space