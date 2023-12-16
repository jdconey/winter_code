#!/bin/bash
TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/gunbarrel-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/cottomsway-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/fiacaillridge-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/morlich-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/lowercarpark-full.jpg --no-check-certificate

#wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/maincarpark-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/zigzags-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/whitelady-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/sunkid-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/BaseStation-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://www.cairngormmountain.co.uk/wp-content/uploads/webcams/PtarmiganStation-full.jpg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://winterhighland.info/cams/aviemore/cairngorm@2.jpeg --no-check-certificate

wget -P /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD http://winterhighland.info/cams/aviemore/lairig-ghru@2.jpeg --no-check-certificate

cp /media/pi/D608-D7E6/scottish_winter/cairngorm/$YR/$MON/$DAY/$TOD/* /media/pi/D608-D7E6/scottish_winter/cairngorm/current

wget -P /media/pi/D608-D7E6/scottish_winter/ben_nevis/$YR/$MON/$DAY/$TOD https://api.holfuy.com/cam/s1746.jpg --no-check-certificate

cp /media/pi/D608-D7E6/scottish_winter/ben_nevis/$YR/$MON/$DAY/$TOD/s1746.jpg /media/pi/D608-D7E6/scottish_winter/ben_nevis/current/

#wget -P /media/pi/D608-D7E6/scottish_winter/ben_nevis/current https://api.holfuy.com/cam/s1746.jpg --no-check-certificate

#wget -p /media/pi/D608-D7E6/scottish_winter/ben_nevis/$YR/$MON/$DAY/$TOD https://api.holfuy.com/cam/s1746.jpg --no-check-certificate

