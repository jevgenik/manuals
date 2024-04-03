===========
Linux users
===========

* USER_UID - user identifier (e.g. 1000)  
* USER_GID - group identifier (e.g. 1000)  

In Linux systems, every user must be a member of at least one group, the primary group.  
The primary group is stored in the /etc/passwd file. 

Commands:

* ``groupadd`` - create a new group (e.g. ``groupadd --gid 1000 mygroup`` - create a new group with gid 1000 and name mygroup)
  
* ``useradd`` - create a new user or update default new user information  
  (e.g. ``useradd --uid 1000 --gid 1000 -s /bin/bash -m myuser``   
  create a new user with uid 1000, gid 1000, shell /bin/bash and home directory /home/myuser)  

* ``groups`` - show groups that current user is a member of

* ``sudo usermod -aG <group name> <username>`` - add user to a group (secondary or supplementary group) 
  (e.g. ``sudo usermod -aG dialout myuser`` - add user myuser to dialout group)

* ``sudo usermode -g <group name> <username>`` - change user's primary group 
  (e.g. ``sudo usermod -g mygroup myuser`` - change user myuser's primary group to mygroup)

* ``chown`` - change file owner and group (e.g. ``chown myuser:mygroup myfile.txt`` - change owner of myfile.txt to myuser and group to mygroup)

* ``chmod u+x simple_velocity_publisher.py`` - make script executable for user (u - user, + - add permission, x - execute)
  

``/home/username/.config`` - directory is typically used to store configuration files and settings specific to a user and their applications
E.g. ``/home/username/.config/xfce4`` - directory that contains Xfce4 configuration files

``/etc/sudoers.d`` - directory that contains sudoers files 
Sudoer file is a configuration file that determines which users can run which commands and as which users. 

``/etc/group`` file is a text file that defines the groups on the system.
Each line of the file contains the following fields:

* *group_name* - It is the name of group. If you run ls -l command, you will also see this name printed in the group field.
* *password* - Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups.
* *group_ID* - Each user must be assigned a group ID. You can see this number in your /etc/passwd file.
* *group_list* - It is a list of user names of users who are members of the group. The user names, must be separated by commas.

``/etc/passwd`` - file that contains one line for each user account, that contans the following fields:  

* *username* - It is used when user logs in. It should be between 1 and 32 characters in length.
* *password* - An x character indicates that encrypted password is stored in /etc/shadow file.
* *user ID (UID)* - Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for  
  other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.  
* *group ID (GID)* - The primary group ID (stored in /etc/group file)
* *user ID info* - The comment field. It allow you to add extra information about the users such as user's full name, phone number etc.
* *home directory* - The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /
* *command/shell* - The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell.

To see a list of users on the system, type the following command: ``cut -d: -f1 /etc/passwd``
cut command is used to extract sections from each line of input. -d option specifies the delimiter, 
-f option specifies the fields to print 

