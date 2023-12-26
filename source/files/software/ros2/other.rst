========================
Tips and troubleshooting
========================

Workaround for an error: SetuptoolsDeprecationWarning - 'setup.py install' is deprecated.  
========================================================================================

Run ``pip install setuptools==58.2.0``

Setuptools version 58.2.0 is the last version that works with ROS 2 python packages without any warnings because it 
is the last version that supports the old installation method, "python setup.py install." This method has been deprecated 
and replaced by newer, standards-based tools, such as pip and ament.