# shotpy
A simple python script to upload images/screenshots to imgur for sharing.
<br>
![Alt Text](https://github.com/AyushBhat/shotpy/raw/master/demo.gif)

# Modules required:
* Linux:
    * `pyimgur` 
    * `scrot` (this is not a python module, a screenshot util written in c.)
    * `notify-send` (for notifications) <br> <br>
Thats all you need.

Install `pyimgur` by using `pip` or just run `configure.py` after cloning the repository.

# How to use:
* If you want to take a screenshot and then upload it to imgur, just run `shotpy` and select the amount of screen you want to capture.
* For making shotpy wait for S number of seconds to capture the seleted area, run `shotpy -S`
* If you want to upload an image thats already in your drive to imgur just run `shotpy <path-to-image>`

The URL of the uploaded image will be copied to the clipboard so that you can paste it anywere.
