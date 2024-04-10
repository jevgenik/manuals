=== Linux commands ====
 `grep` - is a command-line utility for searching plain-text data sets for lines that match a regular expression. 
          Its name comes from g/re/p (globally search a regular expression and print)
          e.g. `grep "Hello" hello.txt` - print lines containing "Hello" in hello.txt)  
 `eog` - Eye of GNOME, is the official image viewer for the GNOME desktop environment
 `xdg-open` - opens a file or URL in the user's preferred application (e.g. `xdg-open hello.txt` - open hello.txt in the default text editor)
 `lsb_release -a` - show Linux distribution information  
 `cat /etc/os-release` - show Linux distribution information)  
 `tail -f /var/log/syslog` - show last 10 lines of syslog and continuously print new lines as they are appended to syslog  
 `tail -15 /var/log/syslog` - show last 15 lines of syslog  
 `stat` - display file or file system status (e.g. `stat /dev/ttyACM0` - show status of ttyACM0)  
 `tree` - list contents of directories in a tree-like format (install with `sudo apt install tree`)  
 `tree -L 1` - show only first level of directories  
 `tmux` - terminal multiplexer, allows you to run multiple terminal sessions inside a single   
          terminal window or remote terminal session (install with `sudo apt install tmux`)  
  `tmux ls` - list all tmux sessions  
  `tmux attach -t <session_name>` - attach to tmux session with specified name  
  `tmux kill-session -t <session_name>` - kill tmux session with specified name  
  `tmux new -s <session_name>` - create new tmux session with specified name  
  `tmux rename-session -t <old_session_name> <new_session_name>` - rename tmux session  
  `tmux detach` - detach from tmux session (keep session running in background) or simply `CTRL-B d`  
  `tmux windows` - list all windows in tmux session  
  `tmux new-window` - create new window in tmux session, or simply `CTRL-B c`  
  `Ctrl-b %` - split tmux window vertically  
  `Ctrl-b "` - split tmux window horizontally  
  `Ctrl-b <arrow key>` - switch between tmux windows  
  `Ctrl-b : list-command` - list all tmux commands  
  `Ctrl-b : [` - enter copy mode (use arrow keys to navigate, press `v` to select text, press `y` to copy selected text)  
  `chmod u+x simple_velocity_publisher.py` - make script executable for user (u - user, + - add permission, x - execute)

### Process management
- `top` - display Linux processes (top -  display Linux processes in real time)  
  `top -p <PID>` - display Linux process with specified PID  
  `top -u <username>` - display Linux processes of specified user    
  `Shift + M` - sort processes by memory usage  
  `Shift + P` - sort processes by CPU usage  
- `pstree` - display a tree diagram of running processes  
  `pstree <PID>` - This will show the process tree starting from the specified PID
- `kill -l` - list all signals  
  `kill <PID>` - terminate process with specified PID (by default sends SIGTERM (15) signal to the process, same as `kill -SIGTERM <PID>`)  
  `kill -SIGINT <PID>` - terminate process with specified PID (sends SIGINT (2) signal to the process) this is the default signal  
                        sent by the `Ctrl + C` command. The primary purpose of SIGINT is to notify a process that  
                        the user has requested an interruption.  SIGINT is a gentle nudge asking the process to stop. If that fails,  
                        SIGTERM is a more forceful, but still polite request for the process to terminate (it still provides the process  
                        with a chance to tidy up (save data) before shutting down). 
                        Finally, if all else fails, SIGKILL terminates the process with no questions asked.  
  `kill -9 <PID>` (same as `kill -SIGKILL <PID>`) - terminate process with specified PID (sends SIGKILL (9) signal to the process)  
                  this is a "forceful" or "hard" kill signal because it immediately terminates the processes without allowing them  
                  to perform any cleanup tasks, to save any data or graceful shutdown procedures.  
- `killal` - send a signal to all processes running any of the specified commands  
  `killall chrome` -  terminate all running instances of the Google Chrome browser on your Linux system  
  `killall -9 process_name` - This signal is commonly known as a "forceful" or "hard" kill signal because it immediately  
                             terminates the processes without allowing them to perform any cleanup tasks or graceful shutdown procedures.  
- `Ctrl + Z` - bash job control. To suspend a foreground process running in a terminal. Stops the process and returns you  
              to the current shell. You can now type `fg` to continue process, or type `bg` to continue the process in the background  
              Ctrl+Z is a useful way to temporarily halt a process without terminating it, allowing you to continue using the terminal  
              for other tasks and then later bring the suspended process back when needed.  
              - If you have a process running in the foreground in your terminal, such as a long-running command or program,  
              pressing Ctrl+Z will suspend that process.  
              - You will see a message indicating that the process has been stopped, along with a job number, typically   
              something like [1]+ Stopped command  
              - The suspended process is now in the background, and you can use the `bg` command to resume it in the background  
              or the `fg` command to bring it back to the foreground.  
 - `Ctrl + C` - terminate a running process (SIGINT [Signal Interrupt - Signal Number 2] signal is sent to the process)  
              (SIGTERM [command kill sends TERM by default] is the preferred way as the process has the chance to terminate gracefully)  

 - `miniterm` - simple terminal program for the serial port (installed as part of pyserial package `sudo apt install python3-serial`)  
              can be used to send commands to the serial port (e.g. send to Arduino [Arduino is used as a motor controller])  
              `miniterm /dev/ttyACM0 115200` - open serial port with baudrate 115200  

 `wget` - command-line utility for downloading files from the web (install with `sudo apt install wget`)
          `wget -O <filename> <url>` - download file from url and save it as filename
          or simply `wget <url>` - download file from url and save it with original name
  


  --Shortcuts in Linux Ubuntu Gui
  `Ctrl + H` - show hidden files
  `Ctrl + L` - go to address bar
  `Ctrl + Shift + C` - copy path of selected file in terminal
  `Ctrl + Shift + V` - paste path of selected file in terminal
  `Ctrl + Z` - stops the process and returns you to the current shell. You can now type fg to 
               continue process, or type bg to continue the process in the background

  --- Journal is a system service for collecting and storing log data (it is a part of systemd) ---
  `journalctl` - query the systemd journal (systemd is a system and service manager for Linux operating systems, that is 
                 responsible for starting and stopping services and daemons, mounting and unmounting file systems, 
                 maintaining the system clock, and other system management tasks)
  `journalctl -fe` - show the latest journal entries and continuously print new entries as they are appended to the journal
  `journalctl -f` - show only new entries as they are appended to the journal
  `journalctl -b` - show messages from the current boot
  `journalctl -u <service_name>` - show logs of service (to get list of services use `systemctl list-units --type=service`)
                                 E.g. `journalctl -b -u docker.service` - show logs of docker service from the current boot            




 
=== WSL2 ===
-- Attach USB devices
--- From an administrator command prompt on Windows, run this command. 
--- It will list all the USB devices connected to Windows.
usbipd wsl list

--- Select the bus ID of the device you’d like to attach to WSL and run this command. 
--- You’ll be prompted by WSL for a password to run a sudo command.
usbipd wsl attach --busid <busid>