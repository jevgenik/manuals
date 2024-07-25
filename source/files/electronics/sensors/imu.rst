===
IMU
===
An IMU, standing for Inertial Measurement Unit, is an electronic device that measures and reports acceleration, orientation, angular rates, 
and other gravitational forces. It is composed of 3 accelerometers, 3 gyroscopes, and depending on the heading requirement, 3 magnetometers. 
One per axis for each of the three vehicle axes: roll, pitch, and yaw.

It is worth noting that IMU provides relative positioning information. Its function is to measure the route of the object relative 
to the starting point, so it cannot provide information about your specific location. Therefore, it is often used together with GPS. 
When the GPS signal is weak in some places, IMU can play its role, allowing the car to continue to obtain absolute position 
information so as not to get lost.

.. figure:: ../images/imu_sensor.png
   :alt: IMU sensor

   `IMU sensor`
