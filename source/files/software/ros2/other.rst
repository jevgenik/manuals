========================
Tips and troubleshooting
========================

Workaround for an error: SetuptoolsDeprecationWarning - 'setup.py install' is deprecated.  
========================================================================================

Run ``pip install setuptools==58.2.0``

Setuptools version 58.2.0 is the last version that works with ROS 2 python packages without any warnings because it 
is the last version that supports the old installation method, "python setup.py install." This method has been deprecated 
and replaced by newer, standards-based tools, such as pip and ament.

=========================
Other Helpful information
=========================

* **FogROS 2** is an open-source cloud-robotics pilot platform from UC Berkeley. Cloud computing using commercial clusters 
  such as Amazon Web Services (AWS) is now fast enough to enable secure compute-intensive robot functions such as SLAM map 
  building from video, grasp planning, and high dimensional motion planning to be performed in the Cloud using 
  high-performance hardware and GPUs in near real-time.

  `Website <https://berkeleyautomation.github.io/FogROS2/about>`_