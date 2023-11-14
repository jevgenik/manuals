# Topological maps 
focus on the spatial relationships and connectivity between different locations, emphasizing the relative positions of features  
rather than their precise geographic coordinates. These maps are often used in navigation systems  and robotics to plan  
efficient routes and understand the layout of an area. They're handy when you care more about the connections between places  
than the exact distances.  
> Origin of word "topology": Greek topos (place) + logos (study).

<img src="../images/topological_map.jpg" alt="Topological map" width="700">

# Geometric maps
are based on the **precise geographic coordinates of features**. They're useful for navigation systems that need to know the exact  
distances between locations. They're also used in robotics to plan efficient routes and understand the layout of an area.

### Descrete map 
is like a grid, where the environment is divided into cells. Each cell represents a specific area, and the map is essentially  
a collection of these cells, each with some attribute (like occupancy probability in a slam scenario).  
It's like mapping the world with a bunch of tiny squares or hexagons. 
This makes it computationally more tractable, especially for grid-based algorithms.

#### Occupancy grid map

<img src="../images/occupancy_grid_map.png" alt="Occupancy grid map" width="300">


### Continuous map
represents the environment as a smooth, mathematical function. Instead of breaking the world into discrete cells, you model it  
as a continuous surface. Continuous maps offer a more detailed representation, but they can be computationally demanding

# SLAM algorithms

## gmapping 
(g means grid because this algorithm uses a grid map)
is a highly efficient Rao-Blackwellized particle filter to learn grid maps from laser range data  
[Details](https://openslam-org.github.io/gmapping.html)

Particle filter is a Monte Carlo algorithm that uses a set of particles (samples) to represent the belief distribution.


# ROS2 Packages
- depthimage_to_laserscan - converts depth image to laser scan  
  [Github](https://github.com/ros-perception/depthimage_to_laserscan/tree/ros2)