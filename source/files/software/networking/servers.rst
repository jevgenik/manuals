=======
Servers
=======

NGINX
=====
NGINX is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. 
Its architecture is asynchronous and event-driven to handle a large number of concurrent connections.
The software was created by Igor Sysoev and first publicly released in 2004.

`Official website <https://www.nginx.com/>`_


Commands
--------

* ``nginx -h`` - Show help

* ``nginx -V`` - Show version and loaded modules

* ``nginx -s stop`` - Stop the server (*-s send signal*)

* ``nginx -s quit`` - Graceful shutdown

* ``nginx -s reload`` - Reload the configuration file

* ``nginx -t`` - Test the configuration file

* ``nginx -V 2>&1 | grep --color=auto rtmp`` - Check if the RTMP module is installed (2>&1 redirect stderr to stdout)

* ``systemctl status nginx`` - Check the status of the service

* ``systemctl start nginx`` - Start the service


Tornado
=======
Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. 
By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it 
ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

`Official website <https://www.tornadoweb.org/en/stable/>`_
