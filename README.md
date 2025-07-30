<h1 align="center" style="margin-top: -10px"> Gizmo </h1>
<p align="center" style="width: 100;">
  Your computer co-pilot.<br>
</p>
A python I/O program that automates running other python scripts. Use it to speed up your workflow, use it as a universal launcher, or whatever you can suit it for.

## Setup
Required: Python 3, and a terminal.

Clone or download this repository, then run `pip install -r .packages` from the `/source` folder.

## How to run and use
Running `gizmo.py` will run Gizmo as intended (the main input/output loop).

> Personally, I use [AutoHotkey](https://www.autohotkey.com/) on Windows, so `Hotkey.ahk` is the script I use and it binds my Home key to running Gizmo.

While in Gizmo, just type in a command, and Gizmo will find the `.py` program associated with that command. Using commas to seperate inputs, you can chain as many commands as you want, and they will execute in that order. Gizmo comes with a bunch of scripts to demonstrate it's usage. You can add your own easily. Use the command `programs` or `help` to list all available programs (`.py` scripts).

## Scripts and file structure
In Gizmo's root folder, there's a `/programs` folder. Gizmo will recognize all scripts under the programs folder, no matter where under that they are. Gizmo simply will look for python scripts (ending in`.py`) and look for command words, named *calls*, in those files, and just run the script with the call that was found.  

When writing your own scripts, include the following three lines at the top of your file:  
```
# Name: Your script/program name
# Desc: Your script/program's short description
# Calls: myscript, mycommand, opensesame, abracadabra
```
With a comment indicator first, include your script's name, description, and calls, separated by commas. This means you can use as many different texts as you want to run the same program, which could open up some flexible use cases. Look through the official scripts if you want to see examples. Output/prints from the programs that run will appear inside the I/O program.

## Arguments
You can make use of arguments in your scripts because a call is only needed at the start of the given input, it does not have to be equal. You can find a handful of implimentations of this by looking at some of the official programs like `YouTube.py`.

## Credits
Written by telekrex.

## License
This project is released into the public domain. See the [LICENSE](LICENSE) file for details.