==================
Process management
==================

* ``lsof`` - list open files and the processes that opened them. It could be device files, regular files, directories, etc.
  
  - ``lsof /path/to/file`` - list all processes that have opened a file. 
  - ``lsof -i`` - list all network connections.  

* ``ps`` - (process status) report a snapshot of the current processes. It does not show the processes that have finished execution.
  
  - ``ps`` - show processes of the current user in the current terminal session only.
  - ``ps -e`` - [everyone] show all processes of all users. Includes all processes, whether or not they're attached to a terminal.
  - ``ps -f`` - show full format listing (more details about the processes)
  - ``ps aux`` - show all running processes (a - show processes of all users, u - show processes of current user, 
    x - [extended] show processes not attached to a terminal)

* ``top`` - utility in Linux that provides a real-time, dynamic view of the system's performance. It displays information about CPU usage, 
  memory usage, running processes, and more
  