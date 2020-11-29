from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import shutil
import os
import os.path

import time

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
driver.save_screenshot('/media/pi/D608-D7E6/scottish_winter/glencoe/current/'+camnm)
print(pat2+camnm)
driver.close()

path3 = pat2

if os.path.isdir(pat2) ==False:
    os.makedirs(pat2)
    print('making directory')
else:
    print('no need to make dirs')
shutil.copyfile('/media/pi/D608-D7E6/scottish_winter/glencoe/current/'+camnm, pat2+camnm)