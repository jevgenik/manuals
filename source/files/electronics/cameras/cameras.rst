=======
Cameras
=======

Stereo cameras
==============
Stereo camera is a pair of cameras that are mounted on the same platform and have parallel optical axes. The distance between the optical axes is called
baseline. The baseline is usually measured in millimeters. The baseline is usually in the range of 50-100 mm. The baseline is usually fixed and cannot be
changed. The baseline is usually measured from the center of the camera lenses.

Stereo cameras are used to capture 3D information about the scene.

.. figure:: images/stereo_camera_zed.png
   :alt: Stereo camera
   :width: 500px

.. figure:: images/parallax.png
   :alt: Stereo camera setup
   :width: 400px
   
   `Source <https://www.researchgate.net/figure/Principle-drawing-of-a-stereo-camera-setup-Objects-1-2-in-various-depth-ranges-are_fig5_303307354>`_


Objects (1,2) in various depth ranges are captured from different camera views. The displacement of the object position from left to right stereo image 
is called **parallax** and depends on the object's distance.

To find distance to the object we need to know the baseline and the parallax. The baseline is fixed and known. The parallax can be measured from the
stereo image. The parallax is measured in pixels. The parallax is inversely proportional to the distance to the object. **The closer the object the larger
the parallax**. 

Camera parameters
=================

.. figure:: images/camera_parameters.png
   :alt: Camera parameters
   :width: 500px
   
   `Source <https://download.autodesk.com/us/maya/mayamatchmoveronlinehelp/index.html?url=WS1a9193826455f5ff-e569a012180ce5891-548a.htm,topicNumber=d0e2765>`_

Camera calibration
==================
Camera calibration is the process of estimating a camera's intrinsic and extrinsic parameters to correct distortions and ensure accurate measurements
in computer vision tasks. It involves determining factors such as Focal Length, Principal Point, and lens distortion coefficients.
To calibrate a camera, we need to take pictures of a calibration pattern from different angles and orientations.

* The **intrinsic parameters** deal with the camera's internal characteristics, such as, principal point, focal length, distortion  
* The **extrinsic parameters** deal with the camera's position and orientation in the world (rotation matrix and translation vector)

**Lens distortion** is caused by the lens of the camera. It causes straight lines to appear curved.

.. figure:: images/lens_distortion.png
   :alt: Lens distortion


.. _intel_realsense:
Intel RealSense depth cameras
=============================
The Intel RealSense Depth Camera D400-Series uses stereo vision to calculate depth. 

`Official website <https://www.intelrealsense.com/>`_

**Intel RealSense SDK 2.0** (librealsense) is a cross-platform library for Intel RealSense depth cameras (D400 & L500 series and the SR300).
The SDK allows depth and color streaming, and provides intrinsic and extrinsic calibration information. 
The library also offers synthetic streams (pointcloud, depth aligned to color and vise-versa), 
and a built-in support for record and playback of streaming sessions.

* `Intel RealSense on GitHub <https://github.com/IntelRealSense/librealsense>`_
* `ROS wrapper for Intel RealSense on GitHub <https://github.com/IntelRealSense/realsense-ros>`_

UVC (USB Video Class)
=====================
UVC cameras (USB video class) are USB-powered devices that incorporate a standard video streaming functionality – 
connecting seamlessly with the host machines.

UVC is supported by the Linux kernel and is natively available in most Linux distributions.

V4L
===
Video4Linux, V4L for short, is a collection of device drivers and an API for supporting realtime video capture on Linux systems.

V4L2 (Video4Linux2) is the second version of V4L.

Video4Linux2 is responsible for creating V4L2 device nodes aka a device file (/dev/videoX, /dev/vbiX and /dev/radioX) 
and tracking data from these nodes

* ``v4l2-ctl`` is a V4L2 utility that can be used to configure video for Linux devices (installed as part of the ``v4l-utils`` package)

  - ``v4l2-ctl --list-devices`` lists the available video devices. 
  - ``v4l2-ctl --all`` lists all the controls for the video device.


Libcamera
=========
Libcamera is a cross-platform camera support library that provides a generic way to access and control camera devices.
Libcamera is designed to be a camera stack that is agnostic to the underlying hardware and supports multiple camera devices.
Comparing to V4L2, libcamera provides a higher level of abstraction and a more consistent API across different camera devices.

.. figure:: images/libcamera.jpg
   :alt: Libcamera      

   `Source <https://www.raspberrypi.com/news/an-open-source-camera-stack-for-raspberry-pi-using-libcamera/>`_


