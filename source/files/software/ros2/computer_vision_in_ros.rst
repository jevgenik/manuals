======================
Computer Vision in ROS
======================

Video encoding and decoding
============================
Video encoding is the process of compressing and potentially changing the format of video content, sometimes even 
changing an analog source to a digital one. In regards to compression, the goal is so that it consumes less space. 
This is because it's a lossy process that throws away information related to the video

Decoding is essentially the reverse of encoding. A decoder takes an encoded, compressed stream/file and decompresses it back into its raw form. 
Raw video data is required for editing processes and for viewing of the raw video.

.. figure:: images/video_encoding_decoding.jpg
   :alt: Video Encoding and Decoding   
   :width: 100%

   Video Encoding and Decoding. `Source <https://imagekit.io/blog/video-encoding/>`_

FFmpeg
======
FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, 
stream, filter and play pretty much anything that humans and machines have created.

`Official Website <https://ffmpeg.org/>`_


ROS2 image transport for FFmpeg encoding
========================================
This ROS 2 image transport supports encoding/decoding with the FFMpeg library. With this transport you can encode h264 and h265, 
using Nvidia hardware acceleration when available.

`GitHub <https://github.com/ros-misc-utilities/ffmpeg_image_transport>`_

Cameras
=======
:ref:`Cameras <intel_realsense>`





