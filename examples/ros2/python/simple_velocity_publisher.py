#!/usr/bin/env python3 # Shebang line is needed to tell the OS what interpreter to use

# Simple velocity publisher node that publishes a constant linear velocity
# of 0.1 m/s for 5 seconds.

import rclpy # Python library for ROS 2
import time # Python library for sleep function
from geometry_msgs.msg import Twist # Message type for velocity commands

def main():
    rclpy.init() # Initialize the ROS 2 client library
    node = rclpy.create_node('velocity_publisher') # Create a node

    velocity_pub = node.create_publisher(Twist, 'cmd_vel', 10) # Create a publisher with a queue_size of 10
    node.get_logger().info('Waiting for publisher to be ready...')
    time.sleep(2)  # Wait for 2 seconds for the publisher to be ready

    loop_rate = rclpy.timer.Rate(10)  # Set the loop rate in Hz (10 messages per second)

    starting_time = rospy.get_time() # Get the current time in seconds since the Epoch

    while rclpy.ok() and (rclpy.clock.Clock().now().to_msg().sec - starting_time < 5):
        robot_vel = Twist()
        robot_vel.linear.x = 0.1
        robot_vel.linear.y = 0.0
        robot_vel.linear.z = 0.0
        robot_vel.angular.x = 0.0
        robot_vel.angular.y = 0.0
        robot_vel.angular.z = 0.0

        velocity_pub.publish(robot_vel) # Publish the velocity command
        
        loop_rate.sleep() # This is needed to ensure that the loop runs at the specified rate (10 Hz)
        
    node.destroy_node() # Destroy the node explicitly (optional)
    rclpy.shutdown() # Shutdown the ROS client library for Python (mandatory)

if __name__ == "__main__": # Python's way of checking if the script is run as an executable or imported as a module
                           # If the script is run as an executable, then the main() function is called
                           # If the script is imported as a module, then the main() function is not called
                           # __name__ is a built-in variable that is set to "__main__" when the script is run as an executable
    try:
        main()
    except rospy.ROSInterruptException: # This exception is raised when the node is killed or shutdown
        pass
