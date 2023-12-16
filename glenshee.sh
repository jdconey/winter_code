#!/bin/bash
TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.snowgatecameras.co.uk/braemar/image.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.snowgatecameras.co.uk/glenshee/image00003.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://localapps.pkc.gov.uk/RoadsCameraImages/Images/8781_cam1.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://localapps.pkc.gov.uk/RoadsCameraImages/Images/8781_cam2.jpg --no-check-certificate

#wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.webcam-hd.com/images/ski-scotland_glenshee/zooms/ski-scotland_glenshee8.jpg --no-check-certificate

#wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.webcam-hd.com/images/ski-scotland_glenshee/zooms/ski-scotland_glenshee1.jpg --no-check-certificate

#wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.webcam-hd.com/images/ski-scotland_glenshee/zooms/ski-scotland_glenshee13.jpg --no-check-certificate

#wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.webcam-hd.com/images/ski-scotland_glenshee/zooms/ski-scotland_glenshee5.jpg --no-check-certificate

cp /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD/* /media/pi/D608-D7E6/scottish_winter/cairngorm/current
