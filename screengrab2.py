from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time

from selenium.webdriver.chrome.options import Options

import shutil
import os
import os.path
import cv2
import time


# Display creates a virtual frame buffer and manages it for you
with Display(visible=False, size=(1200, 1500)):
    camnm='pier_house.png'

    pre='/media/pi/D608-D7E6/scottish_winter/glencoe/'
    curr_time = time.strftime('%Y-%m-%d_%H%M',time.localtime())
    yr = time.strftime('%Y',time.localtime())
    mon = time.strftime('%m',time.localtime())
    day = time.strftime('%d',time.localtime())
    gub = yr+'/'+mon+'/'+day+'/'
    pat2 = '/media/pi/D608-D7E6/scottish_winter/glencoe/'+ gub + curr_time + '/'

    options = Options()
    options.BinaryLocation = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
    #driver.set_window_size(1024, 768) # set the window size that you need 
    driver.get('https://g0.ipcamlive.com/player/player.php?alias=5835e7da84105')
    time.sleep(2)
   # driver.save_screenshot('/media/pi/D608-D7E6/scottish_winter/glencoe/current/'+camnm)
    driver.save_screenshot('/home/pi/Pictures/pier_house1.png')
    print(pat2+camnm)
    driver.close()

    path3 = pat2

    if os.path.isdir(pat2) ==False:
        os.makedirs(pat2)
        print('making directory')
    else:
        print('no need to make dirs')

    ph = cv2.imread('/home/pi/Pictures/pier_house1.png')
    crop_ph = ph[390:960, :]
    #c2= curr_time.replace('_',' ')
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(crop_morlich,c2,(0,470),font, 1, (0,0,0),2,cv2.LINE_AA)
    cv2.imwrite('/media/pi/D608-D7E6/scottish_winter/glencoe/current/'+camnm,crop_ph)
 #   shutil.copyfile('/media/pi/D608-D7E6/scottish_winter/cairngorm/current/'+camnm, pat2+camnm)


    shutil.copyfile('/media/pi/D608-D7E6/scottish_winter/glencoe/current/'+camnm, pat2+camnm)

