#!/usr/bin/python3

import sys
import argparse
import site
path=''
path=site.getsitepackages()
for i in path:
    sys.path.append(i)

import miio.airhumidifier

parser = argparse.ArgumentParser(description='Script which comunicate with AirHumidifier.')
parser.add_argument('IPaddress', help='IP address of AirHumidifier' )
parser.add_argument('token', help='token to login to device')
parser.add_argument('--mode', choices=['Auto', 'Favorite', 'Idle', 'Silent'], help='choose mode operation')
parser.add_argument('--favoriteLevel', type=int, choices=range(0, 11), help='choose mode operation')
parser.add_argument('--power', choices=['ON', 'OFF'], help='power ON/OFF')
parser.add_argument('--debug', action='store_true', help='if define more output is printed')

# MyHumidify.set_mode(miio.airhumidifier.OperationMode.Silent)

args = parser.parse_args()
if args.debug:
    print(args)
MyHumidify = miio.airhumidifier.AirHumidifierCA1(args.IPaddress, args.token)

if args.mode:
    if args.mode == "Auto":
            MyHumidify.set_mode(miio.airhumidifier.OperationMode.Auto)
    elif args.mode == "Favorite":
            MyHumidify.set_mode(miio.airhumidifier.OperationMode.Favorite)
    elif args.mode == "Idle":
            MyHumidify.set_mode(miio.airhumidifier.OperationMode.Idle)
    elif args.mode == "Silent":
            MyHumidify.set_mode(miio.airhumidifier.OperationMode.Silent)

if args.favoriteLevel:
    MyHumidify.set_favorite_level(args.favoriteLevel)

if args.favoriteLevel:
    MyHumidify.set_favorite_level(args.favoriteLevel)

if args.power:
    if args.power == "ON":
        MyHumidify.on()
    elif args.power == "OFF":
        MyHumidify.off()

print(MyHumidify.status())