=============
ROS 2 commands
=============

General commands
================

* ``ros2 run <package_name> <executable_name>`` - run executable from a package. Executable can be written in C++ or Python  
* ``ros2 node list`` - list active nodes     
* ``ros2 node info <node_name>`` - show information about node (e.g. ``ros2 node info /turtlesim``)  
* ``ros2 interface show <interface_name>`` - show interface (interface is a message or service) definition (e.g. ``ros2 interface show geometry_msgs/msg/Twist``)
* ``ros2 wtf`` or ``ros2 doctor`` - show diagnostic information about the ROS 2 system
* ``:=`` - remapping arguments (e.g. ``ros2 run turtlesim turtlesim_node __ns:=/turtle1`` - run turtlesim_node with namespace /turtle1)

ROS 2 topic commands
===================

* ``ros2 topic echo <topic_name>`` - show messages published to topic
* ``ros2 topic echo <topic_name> --no-arr`` - show messages published to topic without array brackets
* ``ros2 topic list`` - list active topics
* ``ros2 topic list --verbose`` - list active topics with their types
* ``ros2 topic list -t`` - list active topics with their types
* ``ros2 topic info <topic_name>`` - show information about topic (e.g. `ros2 topic info /turtle1/cmd_vel`)
* ``ros2 topic type <topic_name>`` - show type of topic (e.g. `ros2 topic type /turtle1/cmd_vel`)
* ``ros2 topic hz <topic_name>`` - show publishing rate of topic (e.g. `ros2 topic hz /turtle1/cmd_vel`)

Name remapping
==============

* ``ros2 run rplidar_ros rplidar_node --ros-args -r __ns:=scanner2``  
* ``--ros args`` - allows you to pass arguments to the node  
* ``-r __ns:=scanner2`` this changes the namespace of the node rplidar_node to 'scanner2' (/scanner/rplidar_node)  
* ``-r __node:=<new node name>`` this renames the node to 'new_node_name'.  
Namespace allows you to run multiple instances of the same node with separate parameter spaces. 

Package commands
================

* ``ros2 pkg create --build-type ament_cmake <package_name>`` - create package with cmake build system (default)
* ``ros2 pkg create --build-type ament_python <package_name>`` - create package with python build system
* ``ros2 pkg create --build-type ament_cmake  --dependencies urdf xacro <package_name>`` - create package with cmake build system and dependencies urdf and xacro
* ``ros2 pkg prefix <package name>`` - get the installation location of package	
* ``ros2 pkg list`` - list all installed packages

ROS 2 params
============

* ``ros2 param list`` - shows parameters belonging to your nodes
* ``ros2 param get <node_name> <parameter_name>`` - displays the type and current value of a parameter
* ``ros2 param set <node_name> <parameter_name> <parameter_value>`` - sets the value of a parameter (``ros2 param set /my_node my_string off``)
* ``ros2 param dump <node_name>`` - this command will print out all of the parameters on a particular node in a YAML file format

TF2 commands
============

    TF2 is the transform library, which lets the user keep track of multiple coordinate frames over time. TF2 maintains  
    the relationship between coordinate frames in a tree structure buffered  in time, and lets the user transform points, 
    vectors, etc between any two coordinate frames at any desired point in time.

* ``ros2 run tf2_tools view_frames.py`` - generate pdf file with TF transform tree
* ``tf_echo`` - reports the transform between any two frames broadcast over ROS
* ``ros2 run tf2_ros tf2_echo <parent frame> <child frame>``


ROS 2 launch commands
=====================

* ``ros2 launch <package_name> <launch_file_name>`` - run launch file from a package
* ``ros2 launch <package_name> <launch_file_name> <args>`` - run launch file from a package with arguments (e.g. ``ros2 launch turtlesim turtlesim_launch.py x:=5 y:=5``)
* ``ros2 launch <package_name> <launch_file_name> --show-args`` - show arguments for launch file

Rviz commands
=============

* ``rviz -d <path_to_rviz_config_file>`` - run rviz with config file (e.g. ``rviz -d /ros_ws/src/bigfootbot_description/rviz/bigfootbot.rviz``)

ROS 2 control commands
======================

* ``ros2 control list_controllers`` - list loaded controllers, their type and status
* ``ros2 control list_hardware_components`` - list available hardware components
* ``ros2 control list_hardware_interfaces`` - list available command and state interfaces


Gazebo
======

Add path to robot model (this line maybe added to ~/.bashrc or docker images entrypoint [ros_entrypoint.sh])

.. code-block:: console

   export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/ros_ws/src/bigfootbot_description/models/

