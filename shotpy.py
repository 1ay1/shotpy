#!/usr/bin/env python
import pyimgur
import sys
import subprocess as s
import pyperclip
import webbrowser

CLIENT_ID = "6db1a5668074579"

if(len(sys.argv) > 2):
    print("Usage: shotpy <filename>/<path to file>")
    print("Or: just shotpy, if you want to upload a screensot.")

if(len(sys.argv) == 2):
    if(len(sys.argv) == 2):
        argv1 = sys.argv[1]
        porn = '/' in sys.argv[1]
        if(porn == False):
            PATH = './' + sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title="Uploaded with shotpy :)")
            s.call(['notify-send', '1 Picture Uploaded Successfully :)', uploaded_image.link])
            pyperclip.copy(uploaded_image.link)
            webbrowser.open_new_tab(uploaded_image.link)

        if (porn == True):
            PATH = sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title="Uploaded with shotpy :)")
            s.call(['notify-send', '1 Picture Uploaded Successfully :)', uploaded_image.link])
            pyperclip.copy(uploaded_image.link)
            webbrowser.open_new_tab(uploaded_image.link)

