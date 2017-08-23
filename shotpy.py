import pyimgur
import sys
import subprocess as s

# import importlib
# try:
#    importlib.find_module('pyimgur')
#    found = True
# except ImportError:
#    found = False

# print(found)

import importlib

spam_spec = importlib.util.find_spec("")
found = spam_spec is not None

print(found)
