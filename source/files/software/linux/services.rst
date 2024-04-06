==============
Linux Services
==============

Systemd is a replacement for init. It is intended to provide a better framework for expressing services' dependencies,
allowing for faster boot times through parallelization. It replaces the init system inherited from UNIX System V and Berkeley 
Software Distribution (BSD)

Init and Systemd are both init daemons but it is better to use the latter since it is commonly used in recent Linux Distros. 
Init uses service whereas Systemd uses systemctl to manage Linux services

The ``/sbin/init`` is a symbolic link to the actual init process. You can follow the symbolic link and see real process. 
I am using the ``stat`` command and you can see that ``/sbin/init`` is linked to ``/lib/systemd/systemd`` in Ubuntu. 
This is an indication that systemd is in use.

Systemctl 
=========
Systemctl is a systemd utility that is responsible for Controlling the systemd system and service manager.
Service manager is a background process that manages the life cycle of services in the system.

.. note::
   In systemd , a **unit** refers to any resource that the system knows how to operate on and manage. This is the primary object that 
   the systemd tools know how to deal with. These resources are defined using configuration files called unit files, which are stored 
   in the ``/usr/lib/systemd/system/`` and ``/etc/systemd/system/`` directories.
   They are merely configuration files that describe the unit and define its behavior 
   (e.g. /etc/systemd/system/docker.service, .socket, .target, etc)                              

* ``systemctl list-units``- lists all currently loaded in memory systemd units, which includes both active and inactive units

* ``systemctl list-units --type=service`` - show list of services that are currently loaded

* ``systemctl list-unit-files`` - lists all available systemd unit files on your system. Unit files define services, targets, 
  sockets, timers, and other systemd units that can be activated.

* ``systemctl status <service_name>`` - show status of service

* ``systemctl enable <service_name>`` - enable service to start automatically at boot

* ``systemctl disable <service_name>`` - disable service to start automatically at boot

* ``systemctl start <service_name>`` - start service

* ``systemctl stop <service_name>`` - stop service

* ``systemctl get-default`` - show default target (default target is a special systemd unit that is loaded by default when 
  the system boots. It is similar to runlevel in the init system)

.. note::
   Target is a special kind of unit that does not do anything itself but instead acts as a
   collection of other units. It is used to group units together and to simplify the boot process

* ``systemctl set-default <target_name>`` - set default target 
  (e.g. ``systemctl set-default multi-user.target`` - set default target to multi-user.target)

* ``systemctl list-units --type=target`` - show list of targets (shown only active targets)

* ``systemctl list-dependencies <target_name>`` - show list of units that are dependencies of target 
  (e.g. ``systemctl list-dependencies multi-user.target``)