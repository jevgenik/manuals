=====
Nodes
=====
Each node in ROS **should be responsible for a single, modular purpose**, e.g. controlling the wheel motors 
or publishing the sensor data from a laser range-finder. 
Each node can send and receive data from other nodes via topics, services, actions, or parameters.

A full robotic system is comprised of many nodes working in concert. In ROS 2, a single executable 
(C++ program, Python program, etc.) can contain one or more nodes.

* `Documentation <https://docs.ros.org/en/rolling/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html>`_
* `More documentation <https://docs.ros.org/en/rolling/Concepts/Basic/About-Nodes.html>`_