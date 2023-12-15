# Path planning 
is the process of finding a path from a start point to a goal point through obstacles. 

<img src="../images/path_planning.png" alt="Path planning">

<img src="../images/navigation.gif" alt="Path planning" width="400">  

## Global planning


## Local planning


## Navigation Stack

<img src="../images/nav2_stack.png" alt="Nav2 stack">  

## ROS2 packages
- **nav2_bt_navigator** (replaces move_base)
  The BT Navigator receives a goal pose and navigates the robot to the specified destination(s). To do so,  
  the module reads an XML description of the Behavior Tree from a file, as specified by a Node parameter, and passes that to a generic  
  BehaviorTreeEngine class which uses the Behavior-Tree.CPP library to dynamically create and execute the BT. The BT XML can also be  
  specified on a per-task basis so that your robot may have many different types of navigation or autonomy behaviors on a per-task basis  
  [Github](https://github.com/ros-planning/navigation2/tree/main/nav2_bt_navigator)  



## ROS1
- **move_base** 
  provides an implementation of an action (see the actionlib package) that, given a goal in the world, will attempt to reach it with  
  a mobile base. The move_base node links together a global and local planner to accomplish its global navigation task.  