#!/usr/bin/env python3
import importlib
from subprocess import run, PIPE, call
from importlib import util
import platform
import sys
import os
import platform
import subprocess
import string


# function to find out if a program is installed in system

def isitin_sys_linux(string):
    command = ['which', string]

    # using run() to run an external command
    checko = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)

    if checko.returncode == 1:
        return False
    if checko.returncode == 0:
        return True


## this will check which platform ( os ) shotpy is running on
OS = sys.platform
if ('linux' or 'bsd' in OS):
    OS = "linux"

if ('darwin' in OS):
    OS = "mac"

if ('win' in OS):
    OS = "windows"


# this will check if scrot and lib notify is installed in system
if (OS == 'linux'):
    if not isitin_sys_linux('scrot'):
        print("'Scrot' not installed, please install 'scrot' first.\n Then run `configure` again.")
        exit()
    if isitin_sys_linux('scrot'):
        print("-> 'scrot' is installed.")

    if not isitin_sys_linux('notify-send'):
        print("Please install 'libnotify' for getting notification on upload")

    if isitin_sys_linux('notify-send'):
        print("-> 'libnotify' is installed.")

print("------------------Python Modules--------------------")

spam_spec = importlib.util.find_spec("pip")
pip_found = spam_spec is not None

if (pip_found == False):
    print("Please install pip first!")

if(pip_found == True):
    print("Pip is installed!")

spam_spec = importlib.util.find_spec("pyimgur")
pyimgur_found = spam_spec is not None

if (pyimgur_found == False):
    print("'pyimgur' was not installed, Installing now!")
    if(os.getuid() != 0):
        print("Installation failed.")
        print("You have to run it script with 'sudo' to make it install the modules")
        exit()
    call(["sudo", "pip3", "install", "pyimgur"])
    print("-> 'pyimgur' is installed.")
if (pyimgur_found == True):
    print("-> 'pyimgur' is already installed.")

spam_spec = importlib.util.find_spec("subprocess")
subprocess_found = spam_spec is not None

if (subprocess_found == False):
    print("'subprocess' was not installed, Installing now!")
    if(os.getuid() != 0):
        print("Installation failed.")
        print("You have to run it script with 'sudo' to make it install the modules")
        exit()
    call(["sudo", "pip3", "install", "subprocess"])
    print("-> 'subprocess' is installed")
if (subprocess_found == True):
    print("-> 'subprocess' is already installed.")

spam_spec = importlib.util.find_spec("pyperclip")
pyperclip_found = spam_spec is not None

if (pyperclip_found == False):
    print("'pyperclip' was not installed, Installing now!")
    if(os.getuid() != 0):
        print("Installation failed.")
        print("You have to run it script with 'sudo' to make it install the modules")
        exit()
    call(["sudo", "pip3", "install", "pyperclip"])
    print("-> 'pyperclip' is installed")
if (pyperclip_found == True):
    print("-> 'pyperclip' is already installed.")

print("Everything is done, you're ready to run 'shotpy'")
