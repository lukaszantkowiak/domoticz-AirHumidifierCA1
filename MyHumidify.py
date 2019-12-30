#!/usr/bin/python3

import sys
import argparse
import site

path=''
path=site.getsitepackages()

for i in path:
    sys.path.append(i)

file = open("/home/pi/domoticz/plugins/domoticz-AirHumidifierCA1/testfile1.txt", "w")
file.write("A")
file.close()

import miio

file = open("/home/pi/domoticz/plugins/domoticz-AirHumidifierCA1/testfile2.txt", "w")
file.write("A")
file.close()

import miio.airhumidifier

file = open("/home/pi/domoticz/plugins/domoticz-AirHumidifierCA1/testfile3.txt", "w")
file.write("A")
file.close()

parser = argparse.ArgumentParser(description='Script which comunicate with AirPurfier.')
parser.add_argument('IPaddress', help='IP address of AirPurfier' )
parser.add_argument('token', help='token to login to device')
parser.add_argument('--mode', choices=['Auto', 'Favorite', 'Idle', 'Silent'], help='choose mode operation')
parser.add_argument('--favoriteLevel', type=int, choices=range(0, 11), help='choose mode operation')
parser.add_argument('--power', choices=['ON', 'OFF'], help='power ON/OFF')
parser.add_argument('--debug', action='store_true', help='if define more output is printed')

# MyAir.set_mode(miio.airhumidifier.OperationMode.Silent)

args = parser.parse_args()

if args.debug:
    print(args)

try:
    file = open("/home/pi/domoticz/plugins/domoticz-AirHumidifierCA1/testfile10.txt", "w")
    file.write(args.IPaddress + "\n")
    file.write(args.token + "\n")
    file.write(str(dir(miio)) + "\n")
    file.write(str(dir(miio.airhumidifier)) + "\n")
    file.close()
except Exception as e:
    file = open("/home/pi/domoticz/plugins/domoticz-AirHumidifierCA1/error_file2.txt", "w")
    file.write(str(e))
    file.close()

try:
    MyAir = miio.airhumidifier.AirHumidifierCA1(args.IPaddress, args.token)
except Exception as e:
    file = open("/home/pi/domoticz/plugins/domoticz-AirHumidifierCA1/error_file.txt", "w")
    file.write(str(e))
    file.close()



file = open("/home/pi/domoticz/plugins/domoticz-AirHumidifierCA1/testfile11.txt", "w")
file.write("a")
file.close()

if args.mode:
    if args.mode == "Auto":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Auto)
    elif args.mode == "Favorite":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Favorite)
    elif args.mode == "Idle":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Idle)
    elif args.mode == "Silent":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Silent)

if args.favoriteLevel:
    MyAir.set_favorite_level(args.favoriteLevel)

if args.favoriteLevel:
    MyAir.set_favorite_level(args.favoriteLevel)

if args.power:
    if args.power == "ON":
        MyAir.on()
    elif args.power == "OFF":
        MyAir.off()

print(MyAir.status())