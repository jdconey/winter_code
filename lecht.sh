#!/bin/bash
TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.trinum.com/ibox/ski-scotland/images/the-lecht/the-lecht1.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.trinum.com/ibox/ski-scotland/images/the-lecht/the-lecht2.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.trinum.com/ibox/ski-scotland/images/the-lecht/the-lecht3.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.trinum.com/ibox/ski-scotland/images/the-lecht/the-lecht4.jpg --no-check-certificate

cp /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD/* /media/pi/D608-D7E6/scottish_winter/cairngorm/current
