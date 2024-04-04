===============
File management
===============

* ``df -h`` - report file system disk space usage and mount points (-h - human readable)

* ``du -h`` - report disk usage at the directory or file level (eg. `du -h /home/user`)  
  
  - ``du -sh`` - display only a total for each argument (eg. `du -sh /home/user`) *-s - summarize*
  - ``du --max-depth=1 -h /home/user`` - print the total for a directory at depth 1
