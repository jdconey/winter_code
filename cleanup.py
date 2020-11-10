# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:57:49 2020

@author: Owner
"""
#Make sure you pull everything first, then push once this is done.

import time 
import datetime
import shutil
import os

month=time.strftime('%m',time.gmtime())
year=time.strftime('%Y',time.gmtime())

if month in ['01','02']:
    mnthtodel=str(eval(month.replace('0',''))+10)
    yrtodel=str(eval(year)-1)
else:
    if month not in ['10','11','12']:
        gub = month.replace('0','')
        mnthtodel1 = eval(gub)-2
    else:
        mnthtodel1=eval(month)-2
    if mnthtodel1<10:
        monthtodel = '0'+str(mnthtodel1)
    else:
        monthtodel = str(mnthtodel1)
        
    yrtodel=year
    
    
dirs=['ben_nevis','cairngorm','glencoe','nevis_range']
path1 = 'C:/Users/Owner/Documents/GitHub/jdconey.github.io/'
for k in dirs:
  #  print(path1+k)
    path2=os.path.join(path1,k)
    files = os.listdir(path2)
    if yrtodel in files:
        path2 = os.path.join(path2,yrtodel)
        files = os.listdir(path2)
        if monthtodel in files:
            original = os.path.join(path2,monthtodel)
            target = os.path.join('C:/Users/Owner/Documents/Scottish_Winter_Webcam_Archive/',k,yrtodel,monthtodel)

            shutil.move(original,target)
#        print(files)
        
    

