- `tee` - read from standard input and write to standard output and files
          install with `sudo apt install tee`  
          Convenient to write logs to file and print them to stdout at the same time (python script.py | tee log.txt)  
          `echo "Hello World" | tee hello.txt` - write "Hello World" to hello.txt and print it to stdout  
          `echo "Hello World" | tee -a hello.txt` - append "Hello World" to hello.txt and print it to stdout  

- `cut`- remove sections from each line of files (install with `sudo apt install cut`)
         `cut -d' ' -f1 <filename>` - cut first column from file f1 means field 1, d means delimiter
         Data in a file is supposed to be separated by a delimiter. The default delimiter is tab.          

#### Sed is a stream editor for filtering and transforming text (install with `sudo apt install sed`)
- `sed 's/old/new/g' <filename>` - replace all occurrences of old with new in file s - substitute, g - global
- To delete a line with start and end pattern use `sed '/start_pattern/,/end_pattern/d' <filename>`

#### Vim is is a highly configurable text editor built to make creating and changing any kind of text very efficient
- `vim <filename>` - open file in vim or create new file if it doesn't exist
- `:q` - quit
- `:w` - save
- `:wq` - save and quit
- `:q!` - quit without saving
- `:help` - show help
- `i` - insert mode. Means that you can type text. Press `Esc` to exit insert mode
- `d` - delete line
- `: set number` - show line numbers
- `v` - visual mode. Means that you can select text. Press `Esc` to exit visual mode
        To select text press `v` and move cursor to select text 
- `y` - yank (copy) selected text
- `p` - paste copied text
- `u` - undo
- `Ctrl + r` - redo
- `/` - search for text (e.g. `/Hello` + `Enter` - search for Hello)
- `n` - go to next search result
- `N` - go to previous search result
- `:s/old/new/g` - replace all occurrences of old with new in file s - substitute, g - global
- `o` - insert new line below current line
- `dd` - delete line
<!-- ![Alt Text](images/gazebo_and_ros.png) -->
<!--img src="images/gazebo_and_ros.png" alt="Alt Text" width="300" height="200"-->