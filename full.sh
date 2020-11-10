
#!/bin/sh

eval `keychain --noask --eval id_ed25519`

TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)

cd /media/pi/D608-D7E6/scottish_winter

git pull

. /home/pi/winter_code/cairngorm.sh
. /home/pi/winter_code/glencoe.sh
. /home/pi/winter_code/nevis_range.sh
python3 /home/pi/winter_code/bennevis.py
python3 /home/pi/winter_code/updates.py

git add *
git commit -m pi_$TOD
git push
