========
Services
========

Services are another method of communication for nodes in the ROS graph. Services are based on a **call-and-response**  
model versus the publisher-subscriber model of topics. While topics allow nodes to subscribe to data streams and get  
continual updates, **services only provide data when they are specifically called by a client**.

.. figure:: images/service.gif 
   :alt: ROS 2 services

   Source: `ROS 2 Documentation <https://docs.ros.org/en/rolling/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html>`_


Commands
========

* ``ros2 service call <service_name> <service_type> <arguments>`` - call a service 
  (e.g. ros2 service call /spawn turtlesim_msgs/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}")