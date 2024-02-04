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

Message ``geometry_msgs/TransformStamped``
--------------------------------------  
Expresses a transform from coordinate frame ``header.frame_id`` (parent frame)  
to the coordinate frame ``child_frame_id`` at the time of ``header.stamp``

`Message Definition <https://docs.ros2.org/latest/api/geometry_msgs/msg/TransformStamped.html>`_  

tf2 commands
------------ 

* ``ros2 run tf2_tools view_frames`` - generate pdf file with TF transform tree
* ``ros2 run tf2_ros tf2_echo <parent frame> <child frame>`` - reports the transform between any two frames broadcast over ROS