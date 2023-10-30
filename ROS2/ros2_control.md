The ros2_control is a framework for (real-time) control of robots using (ROS 2)
ros2_control’s goal is to simplify integrating new hardware and overcome some drawbacks.
> Documentation: [ros2_control](https://ros-controls.github.io/control.ros.org/index.html)  

<!--img src="images/ros2_control_architecture.jpeg" alt="Alt Text"-->

- **controller**
- **controller_manager** - the controller manager loads controllers and manages their life cycle           
- **joint_state_broadcaster** - the broadcaster reads all state interfaces and reports them on /joint_states  
                                and /dynamic_joint_states       
- **diff_drive_controller** - controller for mobile robots with differential drive.  
                              As input it takes velocity commands for the robot body, which are translated to wheel commands for the differential drive base.  
                              Odometry is computed from hardware feedback and published  
                              Documentation: [diff_drive_controller](https://control.ros.org/master/doc/ros2_controllers/diff_drive_controller/doc/userdoc.html)


![ros2_control architecture](images/ros2_control_architecture.jpeg)