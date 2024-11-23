===
GPS
===
GPS (Global Positioning System) is a satellite-based navigation system that provides location and time information 
anywhere on or near the Earth where there is an unobstructed line of sight to four or more GPS satellites. 
The system is operated by the United States government and is freely accessible to anyone with a GPS receiver.

**GPS works by using a network of satellites that orbit the Earth**

#. These satellites continuously transmit signals that contain the satellite's position and the precise time the signal was transmitted. 

#. A GPS receiver on the ground or in a vehicle picks up these signals from multiple satellites and uses the timing information to calculate 
   its distance from each satellite based on the time it took for the signals to arrive. 
  
#. By combining distance measurements from multiple satellites, the GPS receiver can determine its own three-dimensional position (latitude, longitude, and altitude) 
   as well as the precise time.

It has become an essential tool for navigation, mapping, tracking, and timing synchronization in many industries and everyday activities.


**Compoments of GPS**

1. Satellites – They serve like stars in the constellation.
2. Ground stations – They monitor and control satellites. Ground stations also identify their location.
3. Receivers – Receivers are constantly listening for signals from the satellites. Highly advanced receivers can even identify the exact location within a fraction of an inch.


.. figure:: ../images/gps_architecture.jpeg
   :alt: GPS principle
   :width: 500px
   
   `Source <https://trakkitgps.com/how-gps-works/>`_


NMEA
====
NMEA is an acronym for the National Marine Electronics Association. NMEA existed well before GPS was invented. 
According to the NMEA website, the association was formed in 1957 by a group of electronic dealers to create better 
communications with manufacturers. 

Today in the world of GPS, NMEA is a standard data format supported by all GPS manufacturers, much like ASCII is the standard 
for digital computer characters in the computer world.

Example of NMEA sentence (standardized data string). Here is popular NMEA sentence GGA (there exist different types of NMEA sentences):

.. code-block:: bash

  $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47

Where:

- **GP**           GPS position (GL would denote GLONASS). GGA is the NMEA sentence for GPS Fix Data.
- **123519**       is the time stamp: UTC time in hours, minutes and seconds.
- **4807.038**     Latitude 48 deg 07.038' (in format ddmm.mmm)
- **N**            North latitude
- **01131.000**    Longitude 11 deg 31.000' (in format dddmm.mmm)
- **E**            East longitude
- **1**            Quality Indicator (1 = GPS fix, or  uncorrected coordinate)                          
- **08**           Number of satellites being tracked
- **0.9**          Horizontal dilution of position (poition accuracy, the lower the better [<1 is Ideal])
- **545.4**        Altitude in relation (from) to WGS84 ellipsoid
- **M**            Units of altitude (Meters)
- **46.9**         Height of geoid (mean sea level) above WGS84 ellipsoid. This means the geoid (mean sea level) is 46.9 meters below the WGS84 ellipsoid.
- **M**            Units of geoidal height (Meters)
- (empty field) time in seconds since last DGPS update
- (empty field) DGPS station ID number
- ***47**          the checksum data, always begins with *  

.. tip:: 
   To obtain orthometric height (height above mean sea level) from the GPS altitude, you need to subtract the geoid height from the GPS altitude.
   orthometric height = GPS altitude - geoid height.
   So the orthometric height = 545,4 - 46,9 = 498,5 meters above mean sea level

RTK
===
Real-time kinematic positioning (RTK) is the application of surveying to correct for common errors in current satellite 
navigation (GNSS) systems. It uses measurements of the phase of the signal's carrier wave in addition to the information 
content of the signal and relies on a single reference station or interpolated virtual station to provide real-time corrections, 
providing up to centimetre-level accuracy (see DGPS).

`Wikipedia <https://en.wikipedia.org/wiki/Real-time_kinematic_positioning>`_


Software, libraries to work with GPS data
=========================================

Python libraries
----------------

* ``pyserial`` - a library for reading and writing data to serial ports (``pip install pyserial``)
* ``pynmea2`` - a library for parsing NMEA 0183 (GPS) data (``pip install pynmea2``)


ROS
---

* `sensor_msgs/NavSatFix <https://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/NavSatFix.html>`_ - Navigation Satellite fix (position fix) 
  for any Global Navigation Satellite System. Specified using the WGS 84 reference ellipsoid.
      

