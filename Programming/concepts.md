## Callback function

callback function - a function that is passed as an argument to another function, to be "called back" at a later time.
For example, in ROS, a callback function is passed to a subscriber. The subscriber will call the callback function when it receives a message.  

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

## Interpolation of strings 
Is the process of substituting values of variables into placeholders in a string.  

Python:  

```Python
name = "John"
age = 20
print("My name is %s and I am %d years old." % (name, age)) # My name is John and I am 20 years old.

# or new way
print(f"My name is {name} and I am {age} years old.") # My name is John and I am 20 years old.
# f is for format and it is used to interpolate variables into strings
```

## Method / function overloading
is the ability to create multiple methods/functions with the same name but with different parameters.  
NOTE Python does not support method overloading.

C++

```C++
// Example of method overloading

class MyClass
{
    public:
        void my_method(int x)
        {
            // do something
        }

        void my_method(int x, int y)
        {
            // do something
        }
};

int main()
{
    MyClass my_object;
    my_object.my_method(1); // calls my_method(int x)
    my_object.my_method(1, 2); // calls my_method(int x, int y)
    return 0;
}
```