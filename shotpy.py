#!/usr/bin/env python3
import pyimgur
import imghdr
import sys
import subprocess as s
#import webbrowser
import datetime
import os
from pathlib import Path

CLIENT_ID = "6db1a5668074579"
HOME = str(Path.home())

OS = sys.platform
if (('linux' in OS) or ('bsd' in OS)):
    OS = "linux"

if ('darwin' in OS):
    OS = "mac"

if ('win' in OS):
    OS = "windows"

if (OS == 'mac'):
    import pync
    from pync import Notifier

#global image title
global_title = "Uploaded with shotpy :)"
#print help msg function
def blah():
    print("Usage: shotpy <filename>/<path to file> <OPTIONAL:Upload Image title>")
    print("Or: just shotpy, if you want to upload a screenshot.")
    print("Or just shotpy -$SEC, where $SEC is number of seconds you want delay shotpy taking screenshot")
    print("Visit https://github.com/AyushBhat/shotpy for more info.")
    exit()

# notification function for linux using nofity-send
# feed type 'n' if the notification is normal and 'c' if its critical
def notify_send(string, type):
    if (type == 'n'):
        s.call(['notify-send', '1 Picture Uploaded Successfully :)', string])

    if (type == 'c'):
        s.call(['notify-send', '-t', '50', '-u', 'critical', string])


# sending text to clipboad using subprocess.Popen(), will surely work in linux

def send_text_to_clip(string):
    p1 = s.Popen(["echo", string], stdout=s.PIPE)
    p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    p2.stdout.close()


if (len(sys.argv) > 3):
    blah()

if (len(sys.argv) == 3):
    argv1 = sys.argv[1]
    porn = '/' in sys.argv[1]  # path arg or not
    torn = "-" in argv1[:1]  # time delay or not
    dorn = '.' in sys.argv[1]  # dot in name or not
    aorn = os.path.isfile(sys.argv[1])  # name is ANY file or not
    if (aorn == False):  ##check if the file is image only if file exists
        print("File doesn't exist!!")
        exit()
    legaliorn = imghdr.what(sys.argv[1])  # if the filed named is really an image or not
    corn = "-c" in sys.argv[1]  # compression percentage in the arg or not

    if (porn == False and torn == False and aorn == False):
        blah()

    if(aorn == True and legaliorn == None):
        print("The file is not an image!")
        exit()

    if(porn == True or torn == True or legaliorn != None):
        global_title = sys.argv[2]


# if the shotpy has two arguments:
if (len(sys.argv) == 2):
    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        blah()

if  (len(sys.argv) == 2 or (len(sys.argv) == 3)):

    if ((len(sys.argv) == 2) or (len(sys.argv) == 3)):
        argv1 = sys.argv[1]
        porn = '/' in sys.argv[1]  # path arg or not
        torn = "-" in argv1[:1]  # time delay or not
        dorn = '.' in sys.argv[1]  # dot in name or not
        aorn = os.path.isfile(sys.argv[1])  # name is ANY file or not
        if (aorn == False):  ##check if the file is image only if file exists
            print("File doesn't exist!!")
            exit()
        legaliorn = imghdr.what(sys.argv[1])  # if the filed named is really an image or not
        corn = "-c" in sys.argv[1]  # compression percentage in the arg or not


        if(porn == False and torn == False and aorn == False):
            blah()


        if (aorn == True and legaliorn == None):
            print("The file is not an image!")
            exit()


        ## if the first arg is not path, its just an image name with a dot:

        if (porn == False and legaliorn != None):
            PATH = './' + sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title=global_title)
            if (OS == 'linux'):
                notify_send(uploaded_image.link, 'n')

            if (OS == "linux"):
                send_text_to_clip(uploaded_image.link)

            if (OS == 'mac'):
                Notifier.notify('1 Picture Uploaded Successfully :)' + uploaded_image.link, title='shotpy')

            # START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string

            if (OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)
            if (OS == "linux"):
                p1 = s.Popen(["xdg-open", uploaded_image.link])

            #webbrowser.open_new_tab(uploaded_image.link)

        # if the first argument is a path name of course with a dot:

        if ((porn == True) and (legaliorn != None)):
            PATH = sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title=global_title)
            if (OS == 'linux'):
                notify_send(uploaded_image.link, 'n')

            if (OS == 'mac'):
                Notifier.notify('1 Picture Uploaded Successfully :)' + uploaded_image.link, title='shotpy')

            if (OS == "linux"):
                p1 = s.Popen(["echo", uploaded_image.link], stdout=s.PIPE)
                p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
                p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
                p2.stdout.close()

            # START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string

            if (OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)

            if (OS == "linux"):
                p1 = s.Popen(["xdg-open", uploaded_image.link])

            #webbrowser.open_new_tab(uploaded_image.link)

        # countdt will be the full time delay arg, with -
        countdt = sys.argv[1]

        # if the image is screenshot and has to be uploaded using a count down timer obviously this will have no dot
        
        # this will fuck up the - in countdt
        
        countd = countdt[1:]

        if ((torn == True) and (dorn == False)):
            shotpydir = HOME + "/Pictures/shotpy/"
            if not os.path.exists(shotpydir):
                os.makedirs(shotpydir)
            now = datetime.datetime.now()
            imname_t = now.strftime("%I:%M%p-%B-%d-%Y")
            imname = imname_t + "_shotpy.png"
            full_imname = HOME + '/Pictures/shotpy/' + imname
            s.call(['scrot', '-d', countd, '-s', '-e', 'mv $f ' + HOME + '/Pictures/shotpy/' + imname])

            imdir = HOME + '/Pictures/shotpy/'

            if (OS == 'linux'):
                if not os.path.isfile(full_imname):
                    print("Something really went wrong.")
                    print("Sorry couldn't take the screenshot :(")
                    notify_send("Sorry something went wrong\ncouldn'take screenshot", 'c')
                    exit()

            im = pyimgur.Imgur(CLIENT_ID)

            uploaded_image = im.upload_image(imdir + '/' + imname, title=global_title)

            if (OS == 'linux'):
                notify_send(uploaded_image.link, 'n')

            if (OS == 'mac'):
                Notifier.notify('1 Picture Uploaded Successfully :)' + uploaded_image.link, title='shotpy')

            if (OS == "linux"):
                p1 = s.Popen(["xdg-open", uploaded_image.link])

            #webbrowser.open_new_tab(uploaded_image.link)
            if (OS == "linux"):
                p1 = s.Popen(["echo", uploaded_image.link], stdout=s.PIPE)
                p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
                p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
                p2.stdout.close()

            # START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string

            if (OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)

# if shotpy has no argument except its name :

if (len(sys.argv) == 1):
    shotpydir = HOME + "/Pictures/shotpy/"
    if not os.path.exists(shotpydir):
        os.makedirs(shotpydir)
    now = datetime.datetime.now()
    imname_t = now.strftime("%I:%M%p-%B-%d-%Y")
    imname = imname_t + "_shotpy.png"
    full_imname = HOME + '/Pictures/shotpy/' + imname
    s.call(['scrot', '-s', '-e', 'mv $f ' + HOME + '/Pictures/shotpy/' + imname])

    imdir = HOME + '/Pictures/shotpy/'

    if(OS == 'linux'):
        if not os.path.isfile(full_imname):
            print("Something really went wrong.")
            print("Sorry couldn't take the screenshot :(")
            notify_send("Sorry something went wrong\ncouldn'take screenshot :(", 'c')
            exit()

    im = pyimgur.Imgur(CLIENT_ID)

    uploaded_image = im.upload_image(imdir + '/' + imname, title=global_title)

    if (OS == 'linux'):
        notify_send(uploaded_image.link, 'n')

    if (OS == 'mac'):
        Notifier.notify('1 Picture Uploaded Successfully :)' + uploaded_image.link, title='shotpy')

    if (OS == "linux"):
        p1 = s.Popen(["xdg-open", uploaded_image.link])

    #webbrowser.open_new_tab(uploaded_image.link)
    if (OS == "linux"):
        p1 = s.Popen(["echo", uploaded_image.link], stdout=s.PIPE)
        p2 = s.Popen(["xclip", "-selection", "clipboard"], stdin=p1.stdout, stdout=s.PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        p2.stdout.close()

    # START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string
    if (OS == "mac"):
        cmd = 'echo %s | pbcopy' % uploaded_image.link
        os.system(cmd)
