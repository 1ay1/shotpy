#!/usr/bin/env python3
import imghdr
import sys
import subprocess as s
#import webbrowser
import datetime
from pathlib import Path
import importlib
from importlib import util
import os

########A bit of a configuration for first run ######################

spam_spec = importlib.util.find_spec("pip")
pip_found = spam_spec is not None

if (pip_found == False):
    print("Please install pip first!")
    exit(0)

spam_spec = importlib.util.find_spec("pyimgur")
pyimgur_found = spam_spec is not None

if (pyimgur_found == False):
    print("pyimgur module not found!")
    if (os.getuid() != 0):
        print("Please run this script one time as root, to install pyimgur.\nOR run 'pip3 install pyimgur' to install manually.")
        exit(0)
    print("Installing now!")
    s.call(["pip3", "install", "pyimgur"])
    print("-> 'pyimgur' is installed.")
    print("Run shotpy again as 'non-root' to upload pictures or to take screenshot.")
    exit(0)
##########################################################################

import pyimgur

CLIENT_ID = "6db1a5668074579"
HOME = str(Path.home())

OS = sys.platform
if (('linux' in OS) or ('bsd' in OS) or ('gnu' in OS)):
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
    print("Or: just shotpy, if you want to take a screenshot instantly and upload it.")
    print("Or: just shotpy -d <SEC>, where <SEC> is number of seconds you want delay shotpy taking screenshot")
    print("Visit https://github.com/0xBAAAAAAD/shotpy for more info.")
    exit()

# notification function for linux using nofity-send
# feed type 'n' if the notification is normal and 'c' if its critical
def notify_send(string, type):
    if (type == 'n'):
        s.call(['notify-send', 'shotpy\n1 Picture Uploaded Successfully :)', string])

    if (type == 'c'):
        s.call(['notify-send', '-t', '50', '-u', 'critical', 'shotpy\n' + string])


# sending text to clipboad using subprocess.Popen(), will surely work in linux

def send_text_to_clip(string):
    p2 = s.Popen(["xclip", "-se", "c", "-t", "image/png", "-i", string])

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

    if (OS == "linux"):
        send_text_to_clip(imdir + "/" + imname)

    if(OS == 'linux'):
        if not os.path.isfile(full_imname):
            print("Something really went wrong.")
            print("Sorry couldn't take the screenshot :(")
            notify_send("Sorry something went wrong\ncouldn'take screenshot :(", 'c')
            exit()

    im = pyimgur.Imgur(CLIENT_ID)

    uploaded_image = im.upload_image(imdir + '/' + imname, title=global_title)

    if (OS == 'linux'):
        print("1 Picture Uploaded Successfully :)")
        print(uploaded_image.link)
        notify_send(uploaded_image.link, 'n')

    if (OS == 'mac'):
        Notifier.notify('1 Picture Uploaded Successfully :)' + uploaded_image.link, title='shotpy')

    if (OS == "linux"):
        p1 = s.Popen(["xdg-open", uploaded_image.link])

    #webbrowser.open_new_tab(uploaded_image.link)
    if (OS == "linux"):
        send_text_to_clip(imdir + "/" + imname)

    # START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string
    if (OS == "mac"):
        cmd = 'echo %s | pbcopy' % uploaded_image.link
        os.system(cmd)
    exit(0)


if (len(sys.argv) > 3):
    blah()

if (len(sys.argv) == 3):
    argv1 = sys.argv[1]
    porn = '/' in sys.argv[1]  # path arg or not
    torn = "-d" == argv1 or "-D" == argv1  # time delay or not
    dorn = '.' in sys.argv[1]  # dot in name or not
    aorn = os.path.isfile(sys.argv[1])  # name is ANY file or not


    if (torn == False and aorn == False):  ##check if the file is image only if file exists, and if timer is there
        print("File doesn't exist!!")
        exit()

    if(aorn == True):
        legaliorn = imghdr.what(sys.argv[1])  # if the filed named is really an image or not

    corn = "-c" in sys.argv[1]  # compression percentage in the arg or not

    if(not sys.argv[2].isdigit() and torn is True):
        print("Time should be in numbers! Type 'shotpy -h' for help.")
        exit()

    if (porn == False and torn == False and aorn == False):
        blah()

    if(aorn == True):
        if(legaliorn == None):
            print("The file is not an image!")
            exit()

    if(aorn == True):
        if(porn == True or legaliorn != None):
            global_title = sys.argv[2]


# if the shotpy has two arguments:
if (len(sys.argv) == 2):
    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        blah()


if  (len(sys.argv) == 2 or (len(sys.argv) == 3)):

    if ((len(sys.argv) == 2) or (len(sys.argv) == 3)):
        argv1 = sys.argv[1]
        porn = '/' in sys.argv[1]  # path arg or not
        torn = "-d" == argv1 or "-D" == argv1 # time delay or not
        dorn = '.' in sys.argv[1]  # dot in name or not
        aorn = os.path.isfile(sys.argv[1])  # name is ANY file or not

        if(len(sys.argv) == 2 and torn == True and aorn == False): #if args are just 2 and has -d in it which is not a file
            print("You forgot to feed the <time> delay in seconds! Type 'shotpy -h' for help.")
            exit(0)

        if (aorn == False and torn == False):  ##check if the file is image only if file exists
            print("File doesn't exist!!")
            exit()

        if(aorn == True):
            legaliorn = imghdr.what(sys.argv[1])  # if the filed named is really an image or not

        corn = "-c" in sys.argv[1]  # compression percentage in the arg or not


        if(porn == False and torn == False and aorn == False):
            blah()


        if (aorn == True and legaliorn == None):
            print("The file is not an image!")
            exit()



        ## if the first arg is not path, its just an image name with a dot:

        if (aorn == True and porn == False and legaliorn != None):
            PATH = './' + sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title=global_title)
            if (OS == 'linux'):
                print("1 Picture Uploaded Successfully :)")
                print(uploaded_image.link)
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

        if (aorn == True and porn == True and legaliorn != None):
            PATH = sys.argv[1]
            im = pyimgur.Imgur(CLIENT_ID)
            uploaded_image = im.upload_image(PATH, title=global_title)
            if (OS == 'linux'):
                print("1 Picture Uploaded Successfully :)")
                print(uploaded_image.link)
                notify_send(uploaded_image.link, 'n')

            if (OS == 'mac'):
                Notifier.notify('1 Picture Uploaded Successfully :)' + uploaded_image.link, title='shotpy')

            if (OS == "linux"):
               send_text_to_clip('./' + sys.argv[1])


            # START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string

            if (OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)

            if (OS == "linux"):
                p1 = s.Popen(["xdg-open", uploaded_image.link])

            #webbrowser.open_new_tab(uploaded_image.link)

        if ((torn == True) and (aorn == False)):
            # countdt will be the full time delay arg, with -
            countdt = sys.argv[2]

            # if the image is screenshot and has to be uploaded using a count down timer obviously this will have no dot

            # this will fuck up the - in countdt
            shotpydir = HOME + "/Pictures/shotpy/"
            if not os.path.exists(shotpydir):
                os.makedirs(shotpydir)
            now = datetime.datetime.now()
            imname_t = now.strftime("%I:%M%p-%B-%d-%Y")
            imname = imname_t + "_shotpy.png"
            full_imname = HOME + '/Pictures/shotpy/' + imname
            s.call(['scrot', '-d', countdt, '-s', '-e', 'mv $f ' + HOME + '/Pictures/shotpy/' + imname])

            imdir = HOME + '/Pictures/shotpy/'
            #webbrowser.open_new_tab(uploaded_image.link)
            if (OS == "linux"):
                send_text_to_clip(imdir + "/" + imname)


            if (OS == 'linux'):
                if not os.path.isfile(full_imname):
                    print("Something really went wrong.")
                    print("Sorry couldn't take the screenshot :(")
                    notify_send("Sorry something went wrong\ncouldn'take screenshot", 'c')
                    exit()

            im = pyimgur.Imgur(CLIENT_ID)

            uploaded_image = im.upload_image(imdir + '/' + imname, title=global_title)

            if (OS == 'linux'):
                print("1 Picture Uploaded Successfully :)")
                print(uploaded_image.link)
                notify_send(uploaded_image.link, 'n')

            if (OS == 'mac'):
                Notifier.notify('1 Picture Uploaded Successfully :)' + uploaded_image.link, title='shotpy')

            if (OS == "linux"):
                p1 = s.Popen(["xdg-open", uploaded_image.link])

            #webbrowser.open_new_tab(uploaded_image.link)
            if (OS == "linux"):
                send_text_to_clip(shotpydir + "/" + imname)


            # START#### THIS IS FOR YOU TO HANDLE SIFER, upload_image.link is the string

            if (OS == "mac"):
                cmd = 'echo %s | pbcopy' % uploaded_image.link
                os.system(cmd)

