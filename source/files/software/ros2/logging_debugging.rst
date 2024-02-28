=================================
Logging, monitoring and debugging
=================================

RQt
===
RQt is a graphical user interface framework (Qt for ROS) that implements various tools and interfaces in the form of plugins. 

*Qt is a cross-platform application framework that is widely used for 
developing application software with a graphical user interface (GUI)*

One can run all the existing GUI tools as dockable windows within RQt. The tools can still run in a traditional 
standalone method, but RQt makes it easier to manage all the various windows in a single screen layout.

`Documentation <https://docs.ros.org/en/rolling/Concepts/Intermediate/About-RQt.html>`_

You can run any RQt tools/plugins easily by (This GUI allows you to choose any available plugins on your system):

.. code-block:: bash

   rqt

You can also run plugins in standalone windows:

* ``ros2 run rqt_graph rqt_graph`` - show graph of nodes and topics (rqt_graph is a part of rqt_graph package)  
  
  - *rqt_graph* is a dynamic GUI plugin for visualizing the ROS computation graph (dynamic plugin is a plugin that can be loaded and unloaded at runtime)

* ``ros2 run rqt_image_view rqt_image_view`` - show image from camera (*rqt_image_view* is a part of *rqt_image_view* package)

* ``ros2 run rqt_py_console rqt_py_console`` - interactive Python console

* PlotJuggler - a tool for visualizing time series data from ROS. It is a Qt-based application that can be used to plot and analyze data from ROS topics. 
  
  - ``sudo apt-get install ros-$ROS_DISTRO-plotjuggler-ros`` - install PlotJuggler
  
  - ``ros2 run plotjuggler plotjuggler`` - run PlotJuggler


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
