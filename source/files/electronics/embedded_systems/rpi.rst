============
Raspberry Pi
============
Raspbeery PI (RPi) is a small single-board computer developed in the UK by the Raspberry Pi Foundation. It is a low-cost, 
high-performance computer that is designed to be easily accessible to people of all ages. It is a credit-card sized computer 
that plugs into a computer monitor or TV, and uses a standard keyboard and mouse.

`Official Website <https://www.raspberrypi.org/>`_

Commands in linux
=================

* ``vcgencmd`` is a command-line utility used on Raspberry Pi devices that runs the VideoCore GPU on the Raspberry Pi.
  VideoCore is a low-power mobile multimedia processor originally developed for the Raspberry Pi project. 
  It allows you to query various hardware-related information, such as firmware revision, temperature.

  - ``vcgencmd commands`` - show all available commands
  
  - ``vcgencmd measure_temp`` - show CPU temperature
  
  - ``vcgencmd get_throttled`` - show under-voltage and over-temperature flags (if 0x0 - everything is ok, if 0x50000 - under-voltage, 
    if 0x50005 - under-voltage and over-temperature,
    if 0x50001 - under-voltage and currently throttled, if 0x50006 - under-voltage, over-temperature and currently throttled)
    (throttled means that CPU frequency is reduced because of under-voltage or over-temperature)         
  
  - ``vcgencm get_camera`` - show camera status (if supported, if detected, if enabled)

* ``raspistill`` - capture images with the camera module
  - ``raspistill -o image.jpg`` - capture an image and save it to a file
  - ``raspistill -k`` - keep the preview window open (realtime preview of the camera module)

* ``raspivid`` - capture video with the camera module

**To set RPi to boot to console (without GUI)**
  ``sudo systemctl set-default multi-user.target`` - set default target to multi-user.target (multi-user.target is a target that 
  provides a console login and is the default target for non-graphical Raspberry Pi OS images)

