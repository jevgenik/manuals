.. _websocket:
=========
WebSocket
=========
WebSocket is a protocol providing full-duplex communication channels over a single long lived TCP connection.

Comparing to HTTP, WebSocket is more suitable for real-time communication, such as online games, trading systems, and chat applications.


.. figure:: images/websocket.png
   :width: 400px
   :alt: WebSocket
   
   WebSocket. `Source <https://www.wallarm.com/what/a-simple-explanation-of-what-a-websocket-is>`_.



Socket.IO
=========
Socket.IO is an event-driven library for real-time web applications. It enables real-time, bi-directional communication 
between web clients and servers. It consists of two components: a client, and a server. Both components have a nearly identical API.
It is built on top of the WebSocket protocol and can fallback to HTTP long polling in case the WebSocket connection cannot be established.

`Official website <https://socket.io/`_