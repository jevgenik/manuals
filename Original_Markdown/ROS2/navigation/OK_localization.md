# Localization
is the process of determining where a mobile robot is located with respect to its environment.

<img src="../images/localization_discrete.png" alt="Localization Discrete probability function" width="700">  

<img src="../images/localization_continuous.png" alt="Localization Continuous probability function" width="700">  

## Algorithms
- **AMCL (Adaptive Monte Carlo Localization)** is a probabilistic algorithm that uses a particle filter to estimate  
  a robot's 2D pose based on sensor data. The algorithm works by representing the robot's pose as a distribution  
  of particles, where each particle represents a possible pose of the robot