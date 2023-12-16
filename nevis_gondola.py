from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import cv2
import numpy as np
import matplotlib.pyplot as plt

import shutil
import os
import os.path

import time

camnm='gondola.png'

pre='/media/pi/D608-D7E6/scottish_winter/nevis_range/'
curr_time = time.strftime('%Y-%m-%d_%H',time.localtime())
mins = time.strftime('%M',time.localtime())
if mins[1]!='0':
    mins=mins.replace('1','0')
curr_time = curr_time+mins
yr = time.strftime('%Y',time.localtime())
mon = time.strftime('%m',time.localtime())
day = time.strftime('%d',time.localtime())
gub = yr+'/'+mon+'/'+day+'/'
pat2 = '/media/pi/D608-D7E6/scottish_winter/nevis_range/'+ gub + curr_time + '/'

options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
#driver.set_window_size(1024, 768) # set the window size that you need 
driver.get('https://www.nevisrange.co.uk/webcams/')

time.sleep(2)

elem = driver.find_element_by_xpath('//*[@id="sub-content-wrapper"]/div[1]/div/div[1]/iframe')
#elem = driver.find_element_by_tag_name("h3")
print(elem)
#ac = ActionChains(driver)
elem.click()
#driver.save_screenshot('/media/pi/D608-D7E6/scottish_winter/cairngorm/current/'+camnm)
#ac.move_to_element(elem).move_by_offset(0, 200).click().perform()
time.sleep(2)
elem.click()
driver.execute_script("window.scrollTo(0,300);")
time.sleep(1)
driver.save_screenshot('/home/pi/Pictures/gondola.png')
print(pat2+camnm)
driver.close()

#if os.path.isdir(pat2) ==False:
#    os.makedirs(pat2)
#    print('making directory')
#else:
#    print('no need to make dirs')
    
gondola = cv2.imread('/home/pi/Pictures/gondola.png')
crop_gondola = gondola[214:618, 105:824]
#c2= curr_time.replace('_',' ')
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(crop_morlich,c2,(0,470),font, 1, (0,0,0),2,cv2.LINE_AA)
#cv2.imwrite('/home/pi/Pictures/gondola_crop.png',crop_gondola)
#cv2.imwrite('/media/pi/D608-D7E6/scottish_winter/nevis_range/current/'+camnm,crop_gondola)
#shutil.copyfile('/media/pi/D608-D7E6/scottish_winter/nevis_range/current/'+camnm, pat2+camnm)