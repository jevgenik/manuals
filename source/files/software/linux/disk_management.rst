===============
Disk management
===============

Commands:

* ``fdisk -l`` - list disks and partitions
* ``fdisk /dev/sdX`` - access the disk with fdisk utility
* ``mount /dev/sdX1 /mnt/...`` - mount a partition
* ``umount /dev/sdX1`` - unmount a partition
* ``mkfs.ext4 /dev/sdX1`` - format a partition with ext4 file system

.. tip:: `fdisk` is a command-line utility that provides disk partitioning functions

**************************************************
How to format disk with NTFS file system on Linux:
**************************************************

#. ``fdisk -l`` - list disks and partitions
#. ``fdisk /dev/sdX`` - access the disk with fdisk utility to create a partition
#. ``n`` - create a new partition
#. ``p`` - primary partition
#. ``1`` - partition number
#. ``Enter`` - default first sector
#. ``Enter`` - default last sector
#. ``w`` - write table to disk and exit
#. ``mkfs.ntfs /dev/sdX1`` - format a partition with NTFS file system

***************************************************************
How to use a disk on Windows, that has been formatted on Linux:
***************************************************************

.. note:: If you want to use this disk on Windows, you will need to change the partition type from ``0x83`` to ``0x07``. You can do this with `fdisk` utility.

#. ``fdisk -l`` - list disks and partitions
#. ``fdisk /dev/sdX`` - access the disk with fdisk utility
#. ``p`` - identify the partition by printing the partition table
#. ``t`` - change partition type
#. ``7`` - select partition type ``0x07`` (HPFS/NTFS/exFAT)
#. ``w`` - write table to disk and exit

.. note:: Now you can use this disk on Windows. But if you want to use it on Linux again, you can run a command ``ntfsfix /dev/sdX1``.
