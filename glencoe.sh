#!/bin/bash
TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)




wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.benmorewebcam.co.uk/webcam/private/benmore_720p.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/base1200.jpeg --no-check-certificate



wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/mainbasin.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/flypaper.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/dryslope.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/mid.jpeg --no-check-certificate



wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/access2200.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/pollach.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/sledge.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/glencoe/summit.jpeg --no-check-certificate









cp /media/pi/D608-D7E6/scottish_winter/glencoe/$YR/$MON/$DAY/$TOD/* /media/pi/D608-D7E6/scottish_winter/glencoe/current
