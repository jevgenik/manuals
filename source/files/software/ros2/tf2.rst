==============
ROS Transforms
==============
Transformations (or more simply, "transforms") express an object's position and orientation in relation to another.

**A frame** refers to the coordinate system describing an object's position and orientation, typically along x, y, and z axes  
ROS requires each frame to have its own unique frame_id, and a typical scene consists of multiple frames for each  
robot component (i.e. limb, sensor), detected object, and player in the robot's world.

Transforms define the translations and rotations needed to get from a source frame to a target frame – whether it's  
parent-to-child, child-to-parent, or across multiple "generations" of frames. A complete set of a scene's transforms,  
from the base frame to all its related children, constitutes a **transform tree**.  
`More about transforms <https://foxglove.dev/blog/understanding-ros-transforms>`_

.. figure:: images/transforms.png 
   :width: 450px
   :alt: ROS transforms

   `Source <https://foxglove.dev/blog/understanding-ros-transforms>`_

tf2
===
tf2 is the transform library, which lets the user keep track of multiple coordinate frames over time. tf2 maintains the  
relationship between coordinate frames in a tree structure buffered in time and lets the user transform points, vectors,   
etc. between any two coordinate frames at any desired point in time.  \

`tf2 Documentation <https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Tf2.html>`_

.. figure:: images/amr_tf2.png 
   :width: 450px
   :alt: AMR tf2

tf2 commands
------------ 

* ``ros2 run tf2_tools view_frames`` - generate pdf file with TF transform tree
* ``ros2 run tf2_ros tf2_echo <parent frame> <child frame>`` - reports the transform between any two frames broadcast over ROS


ROS Packages and Interfaces
===========================

* **robot_state_publisher** - ROS package contains the Robot State Publisher, a node and a class to publish the state of a robot to tf2. 
  At startup time, Robot State Publisher is supplied with a kinematic tree model (URDF) of the robot. It then subscribes to the 
  joint_states topic (of type sensor_msgs/msg/JointState) to get individual joint states. 
  These joint states are used to update the kinematic tree model, and the resulting 3D poses are then published to tf2
  `GitHub <https://github.com/ros/robot_state_publisher/tree/rolling>`_

* `sensor_msgs/JointState <https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/JointState.html>`_ - a message that holds data to describe 
  the state of a set of torque controlled joints

* `tf2_msgs/TFMessage <https://docs.ros.org/en/melodic/api/tf2_msgs/html/msg/TFMessage.html>`_ - a message that represents a list of 
  transforms corresponding to joints of a robot. Each transform is represented as a ``geometry_msgs/TransformStamped`` type.

* `geometry_msgs/TransformStamped <https://docs.ros2.org/latest/api/geometry_msgs/msg/TransformStamped.html>`_  - a message that
  expresses a transform from coordinate frame ``header.frame_id`` (parent frame)  to the coordinate frame ``child_frame_id`` 
  at the time of ``header.stamp``