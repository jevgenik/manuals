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

