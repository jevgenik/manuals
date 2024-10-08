====
URDF
====
URDF (Unified Robot Description Format)  is a file format for specifying the geometry and organization of robots in ROS.
Is an XML format for representing a robot model.

`URDF Documentation <https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/URDF-Main.html>`_

ROS Packages and Interfaces
===========================

* **robot_state_publisher** - publishes the state of a robot to the tf2 library. `GitHub <https://github.com/ros/robot_state_publisher/tree/rolling>`_

* `sensor_msgs/JointState <https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/JointState.html>`_ - a message that holds data to describe 
  the state of a set of torque controlled joints

* `Example <https://github.com/ros-navigation/navigation2_tutorials/blob/master/sam_bot_description/launch/display.launch.py>`_ of a launch file 
  that starts robot_state_publisher and joint_state_publisher