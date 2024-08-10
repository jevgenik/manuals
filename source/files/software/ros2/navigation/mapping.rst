=======
Mapping
=======
Mapping, in the context of robotics and ROS (Robot Operating System), refers to the process of creating a representation of 
the environment that a robot or sensor can perceive. The goal of mapping is to generate a map, which is typically a 
2D or 3D representation, that captures the spatial layout, obstacles, and other relevant features of the surroundings.


Topological Maps
================
Topological maps focus on the spatial relationships and connectivity between different locations, emphasizing the relative positions 
of features rather than their precise geographic coordinates. These maps are often used in navigation systems  and robotics to plan  
efficient routes and understand the layout of an area. They're handy when you care more about the connections between places  
than the exact distances.  
> Origin of word "topology": Greek topos (place) + logos (study).

.. figure:: images/topological_map.jpg
   :width: 450px
   :alt: Topological Map
   
   Topological Map
   

Discrete map
============ 
Discrete map is like a grid, where the environment is divided into cells. Each cell represents a specific area, and the map is essentially  
a collection of these cells, each with some attribute (like occupancy probability in a slam scenario).  
It's like mapping the world with a bunch of tiny squares or hexagons. 
This makes it computationally more tractable, especially for grid-based algorithms.

.. figure:: images/occupancy_grid_map.png
   :width: 450px
   :alt: Occupancy Grid Map
   
   Occupancy Grid Map


ROS Packages
============

* **depthimage_to_laserscan** - converts depth image to laser scan  
  `GitHub <https://github.com/ros-perception/depthimage_to_laserscan/tree/ros2>`_

* **nav2_map_server** - the Map Server provides maps to the rest of the Nav2 system using both topic and service interfaces.  
  Map server will expose maps on the node bringup, but can also change maps using a load_map service during run-time,   
  as well as save maps using a save_map server. `GitHub <https://github.com/ros-planning/navigation2/tree/main/nav2_map_server>`_



   