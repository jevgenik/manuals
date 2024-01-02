===============
RAID management
===============

* ``RAID (Redundant Array of Independent Disks)`` - is a data storage virtualization technology that combines multiple physical disk drive components into one or more logical units for the purposes of data redundancy, performance improvement, or both.

.. tip:: 
   ``mdadm`` is a tool for managing Linux software RAID devices (eg. RAID 0, RAID 1, RAID 5, etc.)

Commands:

* ``mdadm --manage /dev/md0 --add /dev/sdX`` - add a new disk to RAID
* ``mdadm --manage /dev/md0 --fail /dev/sdX`` - mark a disk as faulty
* ``mdadm --manage /dev/md0 --remove /dev/sdX`` - remove a disk from RAID

* ``mdadm --detail /dev/md0`` and ``cat /proc/mdstat`` - display RAID status and show information about RAID

* ``mdadm --stop /dev/md0`` - stop RAID
* ``mdadm --run /dev/md0`` - start RAID

* ``mdadm --assemble --run /dev/md0 /dev/sdX /dev/sdY /dev/sdZ /dev/sdW`` - assemble RAID from disks and start it
* ``mount /dev/md0 /srv/...`` - mount RAID

* ``fdisk -l`` - list disks and partitions
* ``lsblk`` - list block devices
* ``blkid`` - locate/print block device attributes


How to replace a faulty disk in RAID with a new one:
====================================================

#. Identify a faulty disk: ``mdadm --detail /dev/md0`` or ``cat /proc/mdstat``
#. Mark a disk as faulty: ``mdadm --manage /dev/md0 --fail /dev/sdX``
#. Remove a disk from RAID: ``mdadm --manage /dev/md0 --remove /dev/sdX``
#. Turn off RAID: ``mdadm --stop /dev/md0``
#. Physically replace a faulty disk with a new one
#. Add the new disk to the RAID array: ``mdadm --manage /dev/md0 --add /dev/sdY``
#. Start RAID: ``mdadm --run /dev/md0``
#. Verify RAID status: ``mdadm --detail /dev/md0`` or ``cat /proc/mdstat``
