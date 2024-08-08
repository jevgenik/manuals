=================
Nav2 architecture
=================

.. figure:: ../images/nav2_architecture.png
   :width: 100%
   :alt: Nav2 architecture   
   
   `Source <https://docs.nav2.org/index.html>`_

* **BT Navigator Server** - behavioral tree determining the execution of the appropriate step of the algorithm (e.g. first determine the optimal path and then run the controller).
* **Controller Server** - creates a local costmap and implements the server for handling the controller requests.
* **Planner Server** - creates a global costmap and determines the optimal trajectories based on the global costmap.
* **Behavior Server** - determines the actions that should be performed when the robot gets stuck.
* **Smoother Server** - creates smoother path plans to be more continuous and feasible.