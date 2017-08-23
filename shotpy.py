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

if (len(sys.argv) > 2):
    print("Usage: shotpy <filename>/<path to file>")
    print("Or: just shotpy, if you want to upload a screensot.")
    print("Or just shotpy -$SEC, where $SEC is number of seconds you want delay shotpy taking screenshot")
    print("Visit https://github.com/AyushBhat/shotpy for more info.")

if (len(sys.argv) == 2):
    if (len(sys.argv) == 2):
        argv1 = sys.argv[1]
        porn = '/' in sys.argv[1] # path arg or not
        torn = "-" in sys.argv[1] # time delay or not
        dorn = '.' in sys.argv[1] # dot in name or not
        corn = "-c" in

        if ((porn == False) and (dorn == True)):
            PATH = './' + sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title="Uploaded with shotpy :)")
            s.call(['notify-send','1 Picture Uploaded Successfully :)',uploaded_image.link])


            if(OS == "linux"):
                p1 = s.Popen(["echo", uploaded_image.link], stdout=s.PIPE)
                p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
                p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
                p2.stdout.close()
            
            #START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string

            if(OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)


            webbrowser.open_new_tab(uploaded_image.link)

        if ((porn == True) and (dorn == True)):
            PATH = sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title="Uploaded with shotpy :)")
            s.call(['notify-send', '1 Picture Uploaded Successfully :)', uploaded_image.link])
            if(OS == "linux"):
                p1 = s.Popen(["echo", uploaded_image.link], stdout=s.PIPE)
                p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
                p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
                p2.stdout.close()
                
            #START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string
            
            if(OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)


            webbrowser.open_new_tab(uploaded_image.link)


        # countdt will be the full time delay arg, with -
        countdt = sys.argv[1]

        # this will fuck up the - in countdt

        countd = countdt[1:]

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
                p1 = s.Popen(["echo", uploaded_image.link], stdout=s.PIPE)
                p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
                p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
                p2.stdout.close()

                
            #START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string
            
            if(OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)



if (len(sys.argv) == 1):
    shotpydir = HOME + "/Pictures/shotpy/"
    if not os.path.exists(shotpydir):
        os.makedirs(shotpydir)
    now = datetime.datetime.now()
    imname_t = now.strftime("%I:%M%p-%B-%d-%Y")
    imname = imname_t + "_shotpy.png"
    s.call(['scrot','-s', '-e', 'mv $f ' + HOME + '/Pictures/shotpy/' + imname])

    imdir = HOME + '/Pictures/shotpy/'

    im = pyimgur.Imgur(CLIENT_ID)

    uploaded_image = im.upload_image(imdir + '/' + imname, title="Uploaded with shotpy :)")

    s.call(['notify-send', '1 Picture Uploaded Successfully :)', uploaded_image.link])
    webbrowser.open_new_tab(uploaded_image.link)
    if (OS == "linux"):
        p1 = s.Popen(["echo", uploaded_image.link], stdout=s.PIPE)
        p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        p2.stdout.close()

    #START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string
    if (OS == "mac"):
        cmd = 'echo %s | pbcopy' % uploaded_image.link
        os.system(cmd)
