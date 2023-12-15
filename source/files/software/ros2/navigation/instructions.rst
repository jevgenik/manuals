================================================
Instructions for running the SLAM and navigation
================================================

Mapping (SLAM)
==============

#. Start Gazebo simulation or connect to the real robot
#. Start SLAM node (e.g. gmapping)
#. Start Rviz to visualize the map
#. Drive the robot around the environment to create the map (e.g. using teleop_twist_keyboard)
#. Save the map (e.g. using map_server)


Navigation (localization + path planning)
=========================================

#. Load the map
#. Start localization node (e.g. amcl)
#. Start navigation node (e.g. nav2 or move_base)
#. Start Rviz to visualize the map and navigation
#. Set the goal pose
#. Robot navigates to the goal pose