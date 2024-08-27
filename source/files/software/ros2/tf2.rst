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
* ``ros2 run tf2_ros static_transform_publisher 0.1 0 0.2 0 0 0 base_link base_laser`` - broadcast a static transform between two frames
  Meaning tf2 system publishes the transform to a topic ``/tf_static`` and the transform is not expected to change over time
* ``ros2 run tf2_ros tf2_echo <parent frame> <child frame>`` - reports the transform between any two frames broadcast over ROS
  It continuously listens to the ``/tf`` and ``/tf_static`` topics to retrieve the transformation data between the specified frames. 
  It then prints this information to the terminal in real-time.
  This command is useful for debugging and verifying the correct setup of your coordinate frames in a ROS 2 system. For example, 
  if you're integrating a new sensor or component on your robot and want to ensure that its position relative to the robot's base 
  frame is correctly defined and broadcasted, you can use ``tf2_echo`` to check the transform in real-time


ROS Packages and Interfaces
===========================

* **robot_state_publisher** - ROS package contains the Robot State Publisher, a node and a class to publish the state of a robot to tf2. 
  At startup time, Robot State Publisher is supplied with a kinematic tree model (URDF) of the robot. It then subscribes to the 
  joint_states topic (of type sensor_msgs/msg/JointState) to get individual joint states. 
  These joint states are used to update the kinematic tree model, and the resulting 3D poses are then published to tf2
  `GitHub <https://github.com/ros/robot_state_publisher/tree/rolling>`_

* `geometry_msgs/Transform <https://docs.ros.org/en/latest/api/geometry_msgs/html/msg/Transform.html>`_ - represents the transform between 
  two coordinate frames in free space.

* `geometry_msgs/TransformStamped <https://docs.ros.org/en/latest/api/geometry_msgs/html/msg/TransformStamped.html>`_  - a message that
  expresses a transform from coordinate frame ``header.frame_id`` (parent frame)  to the coordinate frame ``child_frame_id`` 
  at the time of ``header.stamp``

* `tf2_msgs/TFMessage <https://docs.ros.org/en/latest/api/tf2_msgs/html/msg/TFMessage.html>`_ - a message that represents a list of 
  transforms corresponding to joints of a robot. Each transform is represented as a ``geometry_msgs/TransformStamped`` type.

* `sensor_msgs/JointState <https://docs.ros.org/en/latest/api/sensor_msgs/html/msg/JointState.html>`_ - a message that holds data to describe 
  the state of a set of torque controlled joints.