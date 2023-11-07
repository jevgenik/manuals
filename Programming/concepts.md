# Callback function

callback function - a function that is passed as an argument to another function, to be "called back" at a later time.
For example, in ROS, a callback function is passed to a subscriber. The subscriber will call the callback function when it receives a message.  

example code:  

Python
```Python 
def callback_function(msg):
    # do something with msg
    pass

rospy.Subscriber("topic_name", geometry_msgs/Twist, callback_function) # geometry_msgs/Twist - message type, callback_function - name of callback function
```
C++
```C++
void callback_function(const geometry_msgs::Twist::ConstPtr& msg) // ConstPtr is a shared pointer
{
    // do something with msg
}

ros::Subscriber sub = n.subscribe("topic_name", 1000, callback_function); // 1000 - queue size, callback_function - name of callback function
```