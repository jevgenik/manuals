=================
Text manipulation
=================
.. _linux_text_manipulation:

* ``touch`` - create empty file (e.g. ``touch file.txt``)
  
  - ``echo "Hello World" > file.txt`` - write "Hello World" to file.txt 
  - ``echo "Hello World" >> file.txt`` - append "Hello World" to file.txt
  
* ``tee`` - read from standard input and write to standard output and files. Convenient to write logs to file and print them to stdout at the same time 
  
  - ``python script.py | tee log.txt`` - write output of script.py to log.txt and print it to stdout
  - ``echo "Hello World" | tee hello.txt`` - write "Hello World" to hello.txt and print it to stdout  
  - ``echo "Hello World" | tee -a hello.txt`` - append "Hello World" to hello.txt and print it to stdout       

* ``sed`` is a stream editor for filtering and transforming text
  
  - ``sed 's/old/new/g' <filename>`` - replace all occurrences of old with new in file ``s`` - substitute, ``g`` - global  
  - ``sed '/start_pattern/,/end_pattern/d' <filename>`` - delete a line with start and end pattern use

Vim 
===
Vim is is a highly configurable text editor

Modes in vim:

* Normal mode - for navigating and editing text (default mode). You can switch to normal mode by pressing ``Esc`` key
* Insert mode - for inserting text. You can switch to insert mode by pressing ``i`` key
* Visual mode - for selecting text. You can switch to visual mode by pressing ``v`` key
  
  - Visual character mode - for selecting characters of text. You can switch to visual character mode by pressing ``v`` key
  - Visual line mode - for selecting lines of text. You can switch to visual line mode by pressing ``V`` key
  - Visual block mode - for selecting blocks of text. You can switch to visual block mode by pressing ``Ctrl + v`` key

* Command mode - for executing commands. You can switch to command mode by pressing ``:`` key
* Replace mode - for replacing text. You can switch to replace mode by pressing ``R`` key

Commands in vim:

* ``vim <filename>`` - open file in vim or create new file if it doesn't exist
* ``:q`` - quit
* ``:q!`` - quit without saving
* ``:w`` - save
* ``:wq`` - save and quit
* ``:q!`` - quit without saving
* ``:help`` - show help
* ``i`` - insert mode. Means that you can type text. Press ``Esc`` to exit insert mode
* ``d`` - delete line
* ``:set number`` - show line numbers
* ``:set tabstop=4`` - set tabstop to 4 spaces (when you press tab it will insert 4 spaces) (default is 8 spaces)
* ``:set paste`` - paste text without auto indent
* ``y`` - yank (copy) selected text
* ``x`` - cut selected text
* ``p`` - paste copied text
* ``u`` - undo
* ``Ctrl + r`` - redo
* ``/`` - search for text (e.g. ``/Hello`` + ``Enter`` - search for Hello)
* ``n`` - go to next search result
* ``N`` - go to previous search result
* ``:s/old/new/g`` - replace all occurrences of old with new in file s - substitute, g - global
* ``o`` - insert new line below current line
* ``dd`` - delete line