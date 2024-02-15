======
WebRTC
======
WebRTC (Web Real-Time Communications) is a free, open project that provides browsers and mobile applications with Real-Time Communications (RTC) capabilities 
via simple APIs.

WebRTC enables peer-to-peer communication for video, audio, and data sharing directly between web browsers without the need 
for any plugins or external software.

The technologies behind WebRTC are implemented as an open web standard and available as regular JavaScript APIs in all major browsers.

`Website <https://webrtc.org/>`_

.. figure:: images/webrtc.png
   :width: 450px
   :alt: How WebRTC works
   
   How WebRTC works. `Source <https://www.techtarget.com/searchunifiedcommunications/definition/WebRTC-Web-Real-Time-Communications>`_.


Janus Gateway
=============
Janus is a WebRTC Server conceived as a general purpose WebRTC gateway.
It's purpose is to provide a high-level API to handle WebRTC sessions and to perform media and data processing.

Janus WebRTC Server is needed when your real-time communication requirements go beyond simple point-to-point connections and 
involve scenarios such as multi-protocol support, multi-user conferences, broadcasting, or custom applications. 
Janus has modular architecture, scalability, and support for various communication protocols.

`Official Website <https://janus.conf.meetecho.com/>`_

`GitHub <https://github.com/meetecho/janus-gateway>`_

.. figure:: images/janus_architecture_video_room.png
   :width: 450px
   :alt: Janus WebRTC Server Architecture
   
   Janus WebRTC Server Architecture. `Source <https://webrtc.ventures/2020/12/janus-webrtc-media-server-video-conference-app/>`_.