==================
Process management
==================

* ``lsof`` - list open files and the processes that opened them. It could be device files, regular files, directories, etc.
  
  - ``lsof /path/to/file`` - list all processes that have opened a file. 
  - ``lsof -i`` - list all network connections.  

* ``ps`` - (process status) report a snapshot of the current processes. It does not show the processes that have finished execution.

 - ``ps aux`` - show all running processes (a - show processes of all users, u - show processes of current user, 
   x - show processes not attached to a terminal)