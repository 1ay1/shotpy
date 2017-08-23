#!/usr/bin/env python
import pyimgur
import sys
import subprocess as s
import webbrowser
import datetime
import os
from pathlib import Path

CLIENT_ID = "6db1a5668074579"
HOME = str(Path.home())
OS = sys.platform
if( 'linux' in OS):
    OS = "linux"

if( 'darwin' in OS):
    OS = "mac"

if ( 'win' in OS):
    OS = "windows"

#echo -n "string" | xclip -selection clipboard

if (len(sys.argv) > 2):
    print("Usage: shotpy <filename>/<path to file>")
    print("Or: just shotpy, if you want to upload a screensot.")

if (len(sys.argv) == 2):
    if (len(sys.argv) == 2):
        argv1 = sys.argv[1]
        porn = '/' in sys.argv[1]
        torn = "--" in sys.argv[1]
        dorn = '.' in sys.argv[1]

        if ((porn == False) and (dorn == True)):
            PATH = './' + sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title="Uploaded with shotpy :)")
            s.call(['notify-send','1 Picture Uploaded Successfully :)',uploaded_image.link])
            if(OS == "linux"):
                s.call(['echo', '-n', uploaded_image.link , '|' , 'xclip', '-selection', 'clipboard'])
            webbrowser.open_new_tab(uploaded_image.link)

        if ((porn == True) and (dorn == True)):
            PATH = sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title="Uploaded with shotpy :)")
            s.call(['notify-send', '1 Picture Uploaded Successfully :)', uploaded_image.link])
            if(OS == "linux"):
                s.call(['echo', '-n', uploaded_image.link , '|' , 'xclip', '-selection', 'clipboard'])
            webbrowser.open_new_tab(uploaded_image.link)

        countdt = sys.argv[1]
        countd = countdt[2:]
        if ((torn == True) and (dorn == False)):
            shotpydir = HOME + "/Pictures/shotpy/"
            if not os.path.exists(shotpydir):
                os.makedirs(shotpydir)
            now = datetime.datetime.now()
            imname_t = now.strftime("%I:%M%p-%B-%d-%Y")
            imname = imname_t + "_shotpy.png"
            s.call(['scrot', '-d', countd, '-s', '-e', 'mv $f ' + HOME + '/Pictures/shotpy/' + imname])

            imdir = HOME + '/Pictures/shotpy/'

            im = pyimgur.Imgur(CLIENT_ID)

            uploaded_image = im.upload_image(imdir + '/' + imname, title="Uploaded with shotpy :)")

            s.call(['notify-send','1 Picture Uploaded Successfully :)',uploaded_image.link])
            webbrowser.open_new_tab(uploaded_image.link)

            if(OS == "linux"):
                


# if (len(sys.argv) == 1):
#    scrot - e
#    'mv $f ~/Pictures/Screenshots/'
