============
Localization
============
Localization is the process of determining where a mobile robot is located with respect to its environment.

.. image:: images/localization_discrete.png   
   :alt: Localization Discrete probability function

.. image:: images/localization_continuous.png   
   :alt: Localization Continuous probability function


Local Localization
==================
Local localization, also known as dead reckoning or position tracking, is the process of determining a robot's position 
relative to its last known position. It relies on sensors like odometers, inertial measurement units (IMUs), 
and wheel encoders to track the robot's motion from a starting point.

Key characteristics of local localization include:

* **Requires known initial position**: The robot's starting location must be known for local localization to work.

* Accumulates errors over time: Sensor noise and errors like wheel slippage cause the estimated position to 
  drift from the true position as the robot moves.

* Cannot recover if lost: If the robot loses track of its position, local localization cannot recover 
  the correct position without external information.


Global Localization
===================
Global localization is the process of **determining a robot's position relative to a map** of the entire environment. 
It **does not require any prior knowledge of the robot's starting position**. 
Global localization techniques are more powerful than local ones and can handle situations where the robot is 
likely to experience serious positioning errors. 

Some global localization methods include:

* Kalman Filters: Estimate the robot's state using noisy sensor measurements and a motion model.

* Particle Filters: Represent the robot's belief as a set of weighted samples (particles) in the state space.

* Monte Carlo Localization: A variant of particle filters that uses a sampling-based approach to determine the robot's position.

* Markov Localization: A Bayesian approach that approximates the probability of the robot's position using a motion model and sensor model.

Global localization techniques are more robust to errors but require a map of the environment and more computation. 
They can recover the robot's position even if it is lost or kidnapped to an unknown location.


Algorithms
==========

* **AMCL (Adaptive Monte Carlo Localization)** is a probabilistic algorithm that uses a particle filter to estimate    
  a robot's 2D pose based on sensor data. The algorithm works by representing the robot's pose as a distribution  
  of particles, where each particle represents a possible pose of the robot  