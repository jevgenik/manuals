============
Localization
============
Localization is the process of determining where a mobile robot is located with respect to its environment.

.. image:: /images/localization_discrete.png   
   :alt: Localization Discrete probability function

.. image:: /images/localization_continuous.png   
   :alt: Localization Continuous probability function

Algorithms
==========

* **AMCL (Adaptive Monte Carlo Localization)** is a probabilistic algorithm that uses a particle filter to estimate    
  a robot's 2D pose based on sensor data. The algorithm works by representing the robot's pose as a distribution  
  of particles, where each particle represents a possible pose of the robot  