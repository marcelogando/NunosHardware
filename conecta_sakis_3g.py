#!/bin/bash
sleep 5

echo "18" > /sys/class/gpio/export                  

echo "out" > /sys/class/gpio/gpio18/direction

echo "1" > /sys/class/gpio/gpio18/value

sleep 15

sudo /home/pi/raspberry/NunosHardware/umtskeeper/sakis3g connect --console --nostorage --pppd "APN=CUSTOM_APN" "CUSTOM_APN=m2m.arqia.br" "BAUD=9600" "CUSTOM_TTY=/dev/ttyAMA0" "MODEM=OTHER" "OTHER=CUSTOM_TTY" "APN_USER=blank" "APN_PASS=blank" --noprobe
