==========
Networking
==========

systemd-networkd
================
systemd-networkd is a system daemon that manages network configurations.
Is part of the systemd init system. Comapring to NetworkManager, systemd-networkd is a lightweight 
and low-level network configuration service (us)

* ``/etc/systemd/network/`` - network configuration files are stored in this directory
* ``systemctl status systemd-networkd.service`` - show status of systemd-networkd service

NetworkManager
==============
NetworkManager is a daemon that sits on top of libudev (programming interface for managing and interacting with devices in the Linux kernel)  
and other Linux kernel interfaces and provides a high-level interface for the configuration of the network interfaces

* ``/etc/NetworkManager/`` - NetworkManager configuration files are stored in this directory

* ``/etc/NetworkManager/system-connections/``- this directory holds configuration files for network connections, each represented as a separate file. These files are usually named after the connection's name.

* ``systemctl status NetworkManager.service`` - show status of NetworkManager service
    
* ``mcli`` is a command-line tool for controlling NetworkManager and reporting network status.

  -  ``nmcli device show`` - show all network interfaces

  -  ``nmcli connection show`` - show all connections

  -  ``nmcli connection up <connection_name>`` - activate connection

  -  ``nmcli connection down <connection_name>`` - deactivate connection

  -  ``nmtui`` - text user interface for NetworkManager
   
Netplan
======= 
Netpaln is a network configuration utility for Linux. It is used to configure the network interfaces 
through YAML files. From YAML description Netplan will generate all the necessary configuration for your 
chosen renderer tool (NetworkManager or networkd).

* ``/etc/netplan/`` - config files (.yaml) are located in this directory

* ``netplan apply`` - apply changes

Some useful commands and utilities
==================================

* ``nmap`` - network exploration tool and security / port scanner

  - ``nmap -sn 192.168.5.0/24`` - performs a ping scan to find live hosts in the range 192.168.5.0 (``-sn`` - no port scan, just ping scan)

  - ``nmap -p 22 192.168.5.0/24`` - scan for hosts with port 22 (SSH) open  

* ``netstat`` - is a command-line tool that displays network connections (both incoming and outgoing), routing tables, and a number of network interface statistics.

  - ``netstat -tuln`` - show all listening sockets (``-tuln`` - tcp, udp, listening [omitting non-listening sockets], numeric [numberic means show IP addresses instead of hostnames])

  - ``netstat -a | grep 9090`` - show all connections and filter by port 9090 (``-a`` - show all all sockets)

* ``hostname -I`` - show IP address of the host
  
