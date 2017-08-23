#!/usr/bin/env python
import importlib
from subprocess import call

spam_spec = importlib.util.find_spec("pyimgur")
pyimgur_found = spam_spec is not None

if (pyimgur_found == False):
    print("'pyimgur' was not installed, Installing now!")
    call(["sudo", "pip", "install", "pyimgur"])
    print("-> 'pyimgur' is installed.")
if (pyimgur_found == True):
    print("-> 'pyimgur' is already installed.")

spam_spec = importlib.util.find_spec("subprocess")
subprocess_found = spam_spec is not None

if (subprocess_found == False):
    print("'subprocess' was not installed, Installing now!")
    call(["sudo", "pip", "install", "subprocess"])
    print("-> 'subprocess' is installed")
if (subprocess_found == True):
    print("-> 'subprocess' is already installed.")

spam_spec = importlib.util.find_spec("pyperclip")
pyperclip_found = spam_spec is not None

if (pyperclip_found == False):
    print("'pyperclip' was not installed, Installing now!")
    call(["sudo", "pip", "install", "pyperclip"])
    print("-> 'pyperclip' is installed")
if (pyperclip_found == True):
    print("-> 'pyperclip' is already installed.")


print("Everything is done, you're ready to run 'shotpy'")
