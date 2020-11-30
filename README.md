# winter_code
Code for the Scottish Winter Webcam Project

This is the code that gets all the webcam images. The images are downloaded every time the script is run. `cron` is used to schedule the `full.sh` bash script which calls each of the bash/python scripts in turn.

The bash scripts need no other dependencies if you want them to run **locally**. You may wish to change the names of the directories. To pull and push from GitHub, I use [Keychain](https://www.funtoo.org/Keychain), having linked the corresponding SSH key up to my GitHub account so that I am not prompted for my password every time `cron` calls the `full.sh` script.

The `bennevis.py` script requires the following Python (I'm using Python 3 obvs) packages (I have put which versions I am using in brackets):
 - `bs4` (0.0.1)
 - `requests` (2.21.0)
 - `shutil`
 - `os`
 - `time`
 - `wget` (3.2)

The `updates.py` script (which deals with adding captions to the CIC Hut images, and making the "last updated" jpgs - so isn't necessary for a "rugged" look, but hey ho, what can I say) requires:
 - `cv2` (`opencv-python`) (4.4.0.46)
     - I had trouble installing opencv, but with some help from [StackOverflow](https://stackoverflow.com/questions/57211068/raspberry-pi-4-pip-install-opencv-python), I managed to get it to work having run the following:
 ```
      sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100
      sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
      sudo apt-get install libatlas-base-dev
      sudo apt-get install libjasper-dev
      pip install opencv-contrib-python
```

 - `numpy` (1.16.2)
 - `matplotlib` (3.0.2)

The `screengrab.py`, `morlich.py` and `nevis_gondola.py` scripts take screenshots of live video feeds and require the following Python packages:

- `selenium` (3.141.0) - you also need a webdriver for your processor. Getting one to work with chromium (the browser on my Pi) and the Pi's processor was a pain, but I solved it by installing [`chromium-chromedriver`](https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi). 
- `cv2` (`opencv-python` - see notes above about installing opencv) (4.4.0.46)
- `numpy` (1.16.2)
- `matplotlib` (3.0.2)
- `shutil`
- `os`
- `time`
