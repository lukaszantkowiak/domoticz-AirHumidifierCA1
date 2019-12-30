#!/usr/bin/python3

import sys
import argparse
import site
path=''
path=site.getsitepackages()
for i in path:
    sys.path.append(i)

import miio.airhumidifier
import Domoticz

Domoticz.Log("My Air")

parser = argparse.ArgumentParser(description='Script which comunicate with AirPurfier.')
parser.add_argument('IPaddress', help='IP address of AirPurfier' )
parser.add_argument('token', help='token to login to device')
parser.add_argument('--mode', choices=['Auto', 'Favorite', 'Idle', 'Silent'], help='choose mode operation')
parser.add_argument('--favoriteLevel', type=int, choices=range(0, 11), help='choose mode operation')
parser.add_argument('--power', choices=['ON', 'OFF'], help='power ON/OFF')
parser.add_argument('--debug', action='store_true', help='if define more output is printed')

# MyAir.set_mode(miio.airhumidifier.OperationMode.Silent)

Domoticz.Log("My Air2")

args = parser.parse_args()
if args.debug:
    print(args)
MyAir = miio.airhumidifier.AirHumidifierCA1(args.IPaddress, args.token)

Domoticz.Log("My Air3")

if args.mode:
    if args.mode == "Auto":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Auto)
    elif args.mode == "Favorite":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Favorite)
    elif args.mode == "Idle":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Idle)
    elif args.mode == "Silent":
            MyAir.set_mode(miio.airhumidifier.OperationMode.Silent)

Domoticz.Log("My Air4")

if args.favoriteLevel:
    MyAir.set_favorite_level(args.favoriteLevel)

Domoticz.Log("My Air5")

if args.favoriteLevel:
    MyAir.set_favorite_level(args.favoriteLevel)

Domoticz.Log("My Air6")

if args.power:
    if args.power == "ON":
        MyAir.on()
    elif args.power == "OFF":
        MyAir.off()

Domoticz.Log("My Air7")
Domoticz.Log(MyAir.status())

print(MyAir.status())