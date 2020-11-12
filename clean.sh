
#!/bin/sh

eval `keychain --noask --eval id_ed25519`

STAMP=`date --date="5 days ago" +%Y-%m-%d`
echo $STAMP

TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)

cd /media/pi/D608-D7E6/scottish_winter

git pull

python3 /home/pi/winter_code/cleanup2.py

git add *
git commit -m pi__archiving_images_from_$STAMP
git push
