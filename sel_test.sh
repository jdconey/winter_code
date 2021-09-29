
#!/bin/sh
source . /.bash_profile

eval `keychain --noask --eval id_ed25519`

TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)

cd /media/pi/D608-D7E6/scottish_winter

git pull

#. /home/pi/winter_code/cairngorm.sh
#. /home/pi/winter_code/glencoe.sh
#. /home/pi/winter_code/nevis_range.sh
#python3 /home/pi/winter_code/bennevis.py
DISPLAY=:0.0 python3 /home/pi/winter_code/screengrab2.py > /home/pi/sel1.txt
DISPLAY=:0.0 python3 /home/pi/winter_code/morlich.py > /home/pi/sel2.txt
DISPLAY=:0.0 python3 /home/pi/winter_code/nevis_gondola.py >/home/pi/sel3.txt

python3 /home/pi/winter_code/updates.py > /home/pi/sel4.txt

git add *
git commit -m pi_$TOD
git push
