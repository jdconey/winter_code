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

days_ago = 5
first_day_to_del = time.strftime('%d',time.localtime(time.time()-days_ago*86400))
month_to_del = time.strftime('%m',time.localtime(time.time()-days_ago*86400))
year_to_del = time.strftime('%Y',time.localtime(time.time()-days_ago*86400))
print(year_to_del,month_to_del,first_day_to_del)

days=[]
int_d=int(first_day_to_del)
i=1
while i<=int_d:
    if i<10:
        days.append('0'+str(i))
    else:
        days.append(str(i))
    i=i+1
print(days)
   
dirs=['ben_nevis','cairngorm','glencoe','nevis_range']
path1 = '/media/pi/D608-D7E6/scottish_winter/'

for day_to_del in days:
    for k in dirs:
      #  print(path1+k)
        path2=os.path.join(path1,k)
        files = os.listdir(path2)
        if year_to_del in files:
            path2 = os.path.join(path2,year_to_del)
            files = os.listdir(path2)
            if month_to_del in files:
                path2 = os.path.join(path2,month_to_del)
              #  print(path2)
                original = os.path.join(path2,day_to_del)
                files = os.listdir(path2)
                if day_to_del in files:
                    target = os.path.join('/media/pi/D608-D7E6/archive',k,year_to_del,month_to_del,day_to_del)
                    print('archiving '+original+ ' to '+target)
                    shutil.move(original,target)
                else:
                    print('could not find '+original+' in files')

            
#        print(files)
        
    

