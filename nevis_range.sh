#!/bin/bash
TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)










wget -P /media/pi/D608-D7E6/scottish_winter/nevis_range/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/nevisrange/summit.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/nevis_range/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/nevisrange/lowergoose.jpeg --no-check-certificate


wget -P /media/pi/D608-D7E6/scottish_winter/nevis_range/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/nevisrange/goosegully.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/nevis_range/$YR/$MON/$DAY/$TOD http://www.winterhighland.info/cams/nevisrange/base.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/ben_nevis/$YR/$MON/$DAY/$TOD http://www.lochaberwx.co.uk/jpgwebcam.jpg --no-check-certificate

cp /media/pi/D608-D7E6/scottish_winter/nevis_range/$YR/$MON/$DAY/$TOD/*.jpeg /media/pi/D608-D7E6/scottish_winter/nevis_range/current/

cp /media/pi/D608-D7E6/scottish_winter/ben_nevis/$YR/$MON/$DAY/$TOD/jpgwebcam.jpg /media/pi/D608-D7E6/scottish_winter/ben_nevis/current/Sgurr_na_h-Eanchainne.jpg
