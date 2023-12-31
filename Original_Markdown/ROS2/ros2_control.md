# ros2_control

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
- **hardware components** represent abstraction of physical hardware in ros2_control framework. There are three types of  
                          hardware Actuator, Sensor and System  
                          Documentation: [Hardware Components](https://control.ros.org/master/doc/getting_started/getting_started.html#overview-hardware-components)  
- **pluginlib** - pluginlib is a library for writing and dynamically loading plugins.  
                  Plugins are classes that are loaded at runtime using the C++ classloader.  
                  Plugins are useful for making code more modular and reusable.  
                  For example, a plugin can be used to implement a hardware interface for a robot.                  
                  Documentation: [pluginlib](https://docs.ros.org/en/iron/Tutorials/Beginner-Client-Libraries/Pluginlib.html)                              


![ros2_control architecture](images/ros2_control_architecture.jpeg)