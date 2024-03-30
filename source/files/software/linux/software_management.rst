===================
Software management
===================

APT - Advanced Package Tool (apt is a command-line utility for installing, updating, removing, and otherwise managing  
deb packages on Ubuntu, Debian, and related Linux distributions) apt is a newer command-line tool that provides 
the same functionality as apt-get, and possibly more.  

* ``apt update`` - update list of available packages

* ``apt upgrade`` - upgrade all installed packages

* ``apt search <package_name>`` - search for package in repositories

* ``apt list --installed`` - list all installed packages

* ``apt insall --no-install-recommends <package_name>`` - install package without recommended packages and only packages 
required to satisfy dependencies for the specified package (useful in docker images to reduce image size)

* ``apt remove <package_name>`` - remove package

* ``apt purge <package_name>`` - remove package and its configuration files

* ``apt autoremove`` - remove packages that were automatically installed to satisfy dependencies 
for other packages and are now no longer needed

* ``apt-key add <key_file>`` - add key_file to apt trusted keys (Key is a file containing a PGP key in ASCII 
armor format is needed to authenticate the package repository. The apt-key add command is used to add the key)  

* ``apt-key list`` - list apt trusted keys

* ``dpkg`` - install, remove, and inspect deb packages (dpkg is a low-level tool for installing, removing, and inspecting deb packages)

* ``dpkg -i <package_name>`` - install package (e.g. ``dpkg -i google-chrome-stable_current_amd64.deb``)