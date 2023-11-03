Fiducial markers in computer vision are markers that are placed in the field of view of a camera and are used to estimate the pose (position and orientation) of the camera relative to the markers.

<img src="images/fiducial_markers.png" alt="Fiducial markers" width="550">

ARtag and AprilTag are two popular libraries for fiducial markers. They are both based on the same algorithm, but ARtag is more mature and has more features. AprilTag is a newer library and is more actively developed. Both libraries are open source and are available on GitHub.

ARtag advantages:
- More mature
- More stable
- More documentation
- More tutorials

AprilTag advantages: 
- More active development
- More features
- More flexible
- More accurate

**fiducacial_msgs/Fiducial.msg** is the message type for a single fiducial marker.

**Orientation** is represented by a quaternion (x, y, z, w). The quaternion is a 4-dimensional vector that represents a rotation in 3-dimensional space. The quaternion is normalized so that the magnitude of the vector is 1.0. The quaternion is used to represent the orientation of the marker because it is more compact than a 3-dimensional vector.

Pictures below show orientation in Euler angles (roll, pitch, yaw)

<div style="display: flex; align-items: flex-end;">
  <img src="images/roll_pitch_yaw_1.png" alt="Roll Pitch Yaw" width="250">
  <img src="images/roll_pitch_yaw_2.png" alt="Roll Pitch Yaw" width="250">
</div>
  