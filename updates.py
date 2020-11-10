# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:20:11 2020

@author: Owner
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


fileloc='/media/pi/D608-D7E6/scottish_winter/'

text_file = open(fileloc+'upd.txt', "r")
text = text_file.read()
text_file.close() 

img = 255 * np.ones(shape=[40, 370, 3], dtype=np.uint8)



cv2.putText(img, text=text, org=(0,30),
            fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),
            thickness=2, lineType=cv2.LINE_AA)

#cv2.imshow("White Blank", blank_image2)
cv2.imwrite(fileloc+'upd.jpg',img)


text_file = open(fileloc+'ben_nevis/ben.txt', "r")
ben_text = text_file.read()
text_file.close() 

ben = cv2.imread(fileloc+'ben_nevis/current/cic.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(ben,ben_text,(0,30),font, 1, (0,0,0),2,cv2.LINE_AA)
cv2.imwrite(fileloc+'ben_nevis/current/cic_time.jpg',ben)

text_file = open(fileloc+'ben_nevis/ben_zoom.txt', "r")
benz_text = text_file.read()
text_file.close() 

benz = cv2.imread(fileloc+'ben_nevis/current/cic_zoom.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(benz,benz_text,(0,30),font, 1, (0,0,0),2,cv2.LINE_AA)
cv2.imwrite(fileloc+'ben_nevis/current/cic_zoom_time.jpg',benz)

    
