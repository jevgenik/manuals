# Mapping (SLAM)
1. Start Gazebo simulation or connect to the real robot
2. Start SLAM node (e.g. gmapping)
3. Start Rviz to visualize the map
4. Drive the robot around the environment to create the map (e.g. using teleop_twist_keyboard)
5. Save the map (e.g. using map_server)


# Navigation (localization + path planning)
1. Load the map
2. Start localization node (e.g. amcl)
3. Start navigation node (e.g. nav2 or move_base)
4. Start Rviz to visualize the map and navigation
5. Set the goal pose
6. Robot navigates to the goal pose