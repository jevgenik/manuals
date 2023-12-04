#!/usr/bin/env python3

# This is a Python script that uses the ROS2 framework to control a robot's movement 
# in a square pattern. 
# The script defines functions to create and publish Twist messages, which are used to 
# control the robot's linear and angular velocity. 
# The main function uses these functions to move the robot forward, turn left, and repeat to form a square shape.

import rclpy
import time
from geometry_msgs.msg import Twist

# Creates a Twist message with the specified linear and angular velocities
def create_twist_message(linear_x, linear_y, linear_z, 
                         angular_x, angular_y, angular_z):
    robot_vel = Twist()
    robot_vel.linear.x = linear_x
    robot_vel.linear.y = linear_y
    robot_vel.linear.z = linear_z
    robot_vel.angular.x = angular_x
    robot_vel.angular.y = angular_y
    robot_vel.angular.z = angular_z

    return robot_vel

# Publishes a Twist message for a specified duration (in seconds)
# twist_msg is object of type geometry_msgs.msg.Twist
# duration_secs is a float
# velocity_pub is object of type rospy.Publisher
# lopp_rate is object of type rospy.Rate
def publish_twist_for_duration(twist_msg, duration_secs, velocity_pub, loop_rate):
    starting_time = rclpy.clock.Clock().now()
    while rclpy.ok() and (rclpy.clock.Clock().now() - starting_time).to_sec() < duration_secs:
        velocity_pub.publish(twist_msg)
        loop_rate.sleep()

def main():
    rclpy.init() # Initialize the ROS 2 client library
    node = rclpy.create_node("velocity_publisher")
    
    velocity_pub = node.create_publisher(Twist, "cmd_vel", 10) # 10 is the queue_size
    time.sleep(2)  # Wait for 2 seconds for the publisher to be ready

    loop_rate = rclpy.timer.Rate(10) # Send messages at 10Hz (10 messages per second)

    # Move forward 2sec (square top line)
    twist_msg = create_twist_message(linear_x=0.1, linear_y=0.0, linear_z=0.0,
                                     angular_x=0.0, angular_y=0.0, angular_z=0.0) 
    publish_twist_for_duration(twist_msg, 2, velocity_pub, loop_rate)

    # Turn left 90deg
    # 0.785rad/sec * 2sec = 1.57rad = 90deg
    twist_msg = create_twist_message(linear_x=0.0, linear_y=0.0, linear_z=0.0,
                                     angular_x=0.0, angular_y=0.0, angular_z=0.7854) 
    publish_twist_for_duration(twist_msg, 2, velocity_pub, loop_rate)


    # Move forward 2sec (square left vertical line)
    twist_msg = create_twist_message(linear_x=0.1, linear_y=0.0, linear_z=0.0,
                                     angular_x=0.0, angular_y=0.0, angular_z=0.0) 
    publish_twist_for_duration(twist_msg, 2, velocity_pub, loop_rate)

    # Turn left 90deg
    # 0.785rad/sec * 2sec = 1.57rad = 90deg
    twist_msg = create_twist_message(linear_x=0.0, linear_y=0.0, linear_z=0.0,
                                     angular_x=0.0, angular_y=0.0, angular_z=0.7854) 
    publish_twist_for_duration(twist_msg, 2, velocity_pub, loop_rate)

    # Move forward 2sec (square bottom line)
    twist_msg = create_twist_message(linear_x=0.1, linear_y=0.0, linear_z=0.0,
                                     angular_x=0.0, angular_y=0.0, angular_z=0.0) 
    publish_twist_for_duration(twist_msg, 2, velocity_pub, loop_rate)


    # Turn left 90deg
    # 0.785rad/sec * 2sec = 1.57rad = 90deg
    twist_msg = create_twist_message(linear_x=0.0, linear_y=0.0, linear_z=0.0,
                                     angular_x=0.0, angular_y=0.0, angular_z=0.7854) 
    publish_twist_for_duration(twist_msg, 2, velocity_pub, loop_rate)

    # Move forward 2sec (square right vertical line)
    twist_msg = create_twist_message(linear_x=0.1, linear_y=0.0, linear_z=0.0,
                                     angular_x=0.0, angular_y=0.0, angular_z=0.0) 
    publish_twist_for_duration(twist_msg, 2, velocity_pub, loop_rate)

    node.destroy_node() # Destroy the node explicitly (optional)
    rclpy.shutdown() # Shutdown the ROS client library for Python (mandatory)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
