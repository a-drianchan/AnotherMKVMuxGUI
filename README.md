

# AnotherMKVMuxGUI
A(nother) GUI wrapper allowing user to utilize pymkv to batch mux .mkv files, and batch mux tracks between two mkv folders together. 

Requirments.txt will be uploaded once the GUI is completely functional.

![Single Mux Mode](https://i.ibb.co/ngzpBWT/Single-Mux-Screenshot.png)

## **Required Packages (WIP)**

-Python 3
-PySide2
-pymkv
-events


## **Instruction**

 1. Open command line / powershell.  
 2. run "python home.py"

## **Current Status**

**Working**
 - Single File Mux Working
	 - Load in tracks by selecting individual .mkv files
	 - Read track info inside the .mkv file

**WIP /Planned**

 - Batch Mux
	 - Load in all mkv files using directory
	 - Mux all files in directory based on one reference file
	 - Match .mkv files between two source directories for batch muxing
- Proper  display of mkvmerge progress into the GUI itself

