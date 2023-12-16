# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:13:06 2020

@author: Owner
"""
from bs4 import BeautifulSoup
import requests
import shutil
import os
import time
import wget

webcams={#'lochlinne':'http://ah.cdn.licr.co.uk/images/webcams/ben-nevis-and-fort-william-static.jpg'
         #'corran':'http://www.lochaberwx.co.uk/jpgwebcam.jpg'
        }
webcams2={ #'cic':['https://www.smc.org.uk/cicwebcam/cic_weather',1],
         #'cic_zoom':['https://www.smc.org.uk/cicwebcam/cic_weather',2],
          'torlundy':["https://visitfortwilliam.co.uk/webcam_images",1]
        }

for cam in webcams2:
    url = webcams2[cam][0]
    content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    image_tags = soup.findAll('img')
    onewewant = image_tags[webcams2[cam][1]].get('src')
    webcams[cam]=onewewant
    if cam.startswith('cic'):
        webcams[cam]='https://www.smc.org.uk'+webcams[cam]
        #print(webcams[cam][-23:-4])
        tt1 = webcams[cam][-23:-13]
        tt2 = webcams[cam][-12:-4]
        tt1=tt1.replace('_','-')
        tt2=tt2.replace('_',':')
        tt=tt1+' '+tt2
        print(tt)
        c2=cam.replace('cic','ben')
        file = open('/media/pi/D608-D7E6/scottish_winter/ben_nevis/'+c2+'.txt', 'r+')
        file.write(tt)
        file.close()
        
  #  print(onewewant)
  #  pre='/media/pi/D608-D7E6/scottish_winter/ben_nevis/'
  #  curr_time = time.strftime('%Y-%m-%d_%H%M',time.localtime())
  #  yr = time.strftime('%Y',time.localtime())
  #  mon = time.strftime('%m',time.localtime())
  #  day = time.strftime('%d',time.localtime())
  #  gub = yr+'/'+mon+'/'+day+'/'
  #  pat2 = '/media/pi/D608-D7E6/scottish_winter/ben_nevis/'+ gub + curr_time + '/'
   # filename = wget.download(onewewant, out=pat2)
        
    #url = "https://aboutfortwilliam.com/webcams/ben-nevis-and-fort-william"
#url="https://visitfortwilliam.co.uk/webcam_images"
# get contents from url
#content = requests.get(url).content
# get soup
#soup = BeautifulSoup(content,'lxml') # choose lxml parser
# find the tag : <img ... >
#image_tags = soup.findAll('img')
# print out image urls

#onewewant=image_tags[1].get('src')

#webcams['torlundy']=onewewant

pre='/media/pi/D608-D7E6/scottish_winter/ben_nevis/'
curr_time = time.strftime('%Y-%m-%d_%H%M',time.localtime())
yr = time.strftime('%Y',time.localtime())
mon = time.strftime('%m',time.localtime())
day = time.strftime('%d',time.localtime())
gub = yr+'/'+mon+'/'+day+'/'
pat2 = '/media/pi/D608-D7E6/scottish_winter/ben_nevis/'+ gub + curr_time + '/'
#download(onewewant,pat2)
#filename = wget.download(onewewant, out=pat2)
# Set up the image URL and filename
#filename = 'torlundy.jpg'

# Open the url image, set stream to True, this will return the stream content.
for cam in webcams:
    camnm=cam+'.jpg'
    if not os.path.isdir(pat2):
            os.makedirs(pat2)
    r = requests.get(webcams[cam], stream = True)
    
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(pat2+camnm,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        shutil.copyfile(pat2+camnm, '/media/pi/D608-D7E6/scottish_winter/ben_nevis/current/'+camnm)
        
        print('Image sucessfully Downloaded: ',camnm)
        #print(pat2)
    else:
        print('Image Couldn\'t be retreived',camnm)
        
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
file = open('/media/pi/D608-D7E6/scottish_winter/upd.txt', 'r+')
# write() - it used to write direct text to the file
# writelines() - it used to write multiple lines or strings at a time, it takes iterator as an argument
# writing data using the write() method
file.write(now)
# closing the file
file.close()



