===
IMU
===
An IMU, standing for Inertial Measurement Unit, is an electronic device that measures and reports acceleration, orientation, angular rates. 
It is composed of 3-axis accelerometer, 3-axis gyroscope, and, depending on the heading requirements, 3-axis magnetometer.

It is worth noting that IMU provides relative positioning information. Its function is to measure the route of the object relative 
to the starting point, so it cannot provide information about your specific location. Therefore, it is often used together with GPS. 
When the GPS signal is weak in some places, IMU can play its role, allowing the car to continue to obtain absolute position 
information so as not to get lost.

.. figure:: ../images/imu_sensor.png
   :alt: IMU sensor   

   IMU sensor


ROS
===

* `sensor_msgs/Imu <https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Imu.html>`_ - message type for IMU data in ROS
