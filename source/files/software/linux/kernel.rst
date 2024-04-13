==================
Kernel and devices
==================
Linux kernel is the core of the system. It is responsible for managing the hardware, running the processes, 
and providing the services that make the system usable. 

The kernel is the lowest level of the operating system. 
It is the first piece of software that is loaded into memory when the system boots up. 
It is the last piece of software that is unloaded from memory when the system shuts down.

* ``dmesg`` - print kernel messages
  
  -  ``dmesg --follow`` - print kernel messages as they are generated
  -  ``dmesg | tail`` - print last kernel messages (last 10 lines)

* ``dkms`` - Dynamic Kernel Module Support (DKMS). It is a framework that allows for the installation of 
  low-level system software on a running system. It is used to automatically build and install kernel modules 
  that are not included in the mainline kernel.

  - ``dkms status`` - display the status of kernel modules managed by DKMS 

* ``lsusb`` - list USB devices
  
  -  ``lsusb -t`` - show USB devices in a tree
  -  ``lsusb -v`` - show USB devices in verbose mode

To debug USB camera, you can use the following commands:

* ``lsusb`` - list USB devices

* ``lsusb -t`` - show USB devices in a tree

* ``lsusb -v`` - show USB devices in verbose mode

* ``dmesg | grep usb`` - show USB messages

* ``dmesg | grep video`` - show video messages

* ``v4l2-ctl --list-devices`` - list video devices

* ``v4l2-ctl --list-formats-ext`` - list video formats

* ``cheese`` - open video device with Cheese application (it is a simple webcam viewer)

* ``rtmpdump -r rtmp://localhost/live/1234 -o output.flv`` - record video stream from RTMP server to output.flv file


udev
====
The udev is a device manager for the Linux kernel. As the successor of devfsd and hotplug, udev primarily manages 
device nodes in the /dev directory. 

At the same time, udev also handles all user space events raised while 
hardware devices are added into the system or removed from it, including firmware loading as required by certain devices.

**udev rules** are used to assign predictable names to devices, or to create symlinks to devices that may not always be present.
For example, you can create a udev rule to create a symlink to a USB camera that is always present in the system.

Udev rules are stored in the ``/etc/udev/rules.d`` directory.

For example: 

``/etc/udev/rules.d/99-usb-camera.rules``

.. code-block:: bash

   # Create a symlink to USB camera
   KERNEL=="video*", SUBSYSTEM=="video4linux", SYMLINK+="usb_camera"

*usb_camera* will be added to the /dev directory as a symlink to the USB camera device.

To reload udev rules, you can use the following command:

.. code-block:: bash
 
   sudo udevadm control --reload-rules && sudo udevadm trigger

