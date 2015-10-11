Documentation
-------------
Project: Project 1 - Movie Trailer Website
Version: 1
Author: Mark Purser
Python version: Python 3

Contents
--------
Package contains:
 1) entertainment_center.py: Primary file to be executed
 2) media.py: Initializes instance of class 'movie', referenced by 
    entertainment_center.py
 3) fresh_tomatoes.py: Generates and opens html file; 
    referenced by entertainment_center.py and provided by
    Udacity team.

Overview
--------
These files contain python procedures that generate and 
open an html file that displays movies and allows users 
to view the movie trailer by clicking on the movie poster.

The python file 'entertainment_center.py' references a 
class type initialized in the python file 'media.py'. 
An instance of this class is created for each movie in 
'entertainment_center.py'. These instances are then passed 
to a procedure in 'fresh_tomatoes.py', which generates an 
html file (saved in the same directory when created--previous 
versions are overwritten) and then opens the html file for 
users to view movie posters and play trailers.

How to run
----------
In order to run:

1) Place all files in a single directory
2) Verify that Python 3 is installed on your computer. If
   not, visit 'https://www.python.org/'.
2) Execute python file 'entertainment_center.py' using Python.exe.
   If Python.exe is the default program for running '*.py' files,
   then double-clicking on the 'entertainment_center.py' should
   automatically execute the program and open the html file in your
   default webbrowser. If Python.exe is not the default, then the 
   file can be executed by opening and running via the Python IDLE 
   program.

Changelog
---------
Version 1: Initial build