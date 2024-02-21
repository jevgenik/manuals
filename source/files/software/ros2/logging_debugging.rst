=================================
Logging, monitoring and debugging
=================================

Recording and playing back data
===============================
``ros2 bag`` is a command line tool for recording data published on topics in your system. It accumulates the data 
passed on any number of topics and saves it in a file. You can then replay the data to reproduce the 
results of your tests and experiments. 

.. note::

   NB! Starting from ROS 2 Iron, the default bag file type has been changed from .db3 (sqlite3) to .mcap (MCAP).

* ``ros2 bag record <topic_name>`` - record messages from a topic to a bag file
* ``ros2 bag play <bag_file>`` - play back messages from a bag file
* ``ros2 bag info <bag_file>`` - display information about a bag file


`ROS 2 documentation <https://docs.ros.org/en/rolling/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html#recording-and-playing-back-data>`_


MCAP
====
MCAP (pronounced "em-cap") is an open source container file format for multimodal log data. It supports multiple channels of 
timestamped pre-serialized data, and is ideal for use in pub/sub or robotics applications.

`Official website <https://mcap.dev/>`_

`Online MCAP editor <https://mcap-editor.netlify.app/>`_
