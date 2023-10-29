#!/usr/bin/env python3 # Shebang line is needed to tell the OS what interpreter to use

# Simple velocity publisher node that publishes a constant linear velocity
# of 0.1 m/s for 5 seconds.

import rospy # Python client library for ROS
from geometry_msgs.msg import Twist # Message type for velocity commands

def main():
    rospy.init_node("velocity_publisher") # Initialize the node with the name "velocity_publisher"
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0) # Create a publisher object
    rospy.sleep(2) # Wait for 2 seconds for the publisher to be ready

    loop_rate = rospy.Rate(10) # Set the loop rate in Hz (10 times per second)
    starting_time = rospy.get_time() # Get the current time in seconds since the Epoch

    while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < 5):
        robot_vel = Twist()
        robot_vel.linear.x = 0.1
        robot_vel.linear.y = 0.0
        robot_vel.linear.z = 0.0
        robot_vel.angular.x = 0.0
        robot_vel.angular.y = 0.0
        robot_vel.angular.z = 0.0

        velocity_pub.publish(robot_vel) # Publish the velocity command
        
        loop_rate.sleep() # This is needed to ensure that the loop runs at the specified rate (10 Hz)

if __name__ == '__main__': # Python's way of checking if the script is run as an executable or imported as a module
                           # If the script is run as an executable, then the main() function is called
                           # If the script is imported as a module, then the main() function is not called
                           # __name__ is a built-in variable that is set to "__main__" when the script is run as an executable
    try:
        main()
    except rospy.ROSInterruptException:
        pass
