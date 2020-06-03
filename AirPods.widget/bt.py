#!/usr/bin/python3

import json
import os
import plistlib
import sys

# for debugging purpose defaults read /Library/Preferences/com.apple.Bluetooth


def airpod_battery_status(device_name):
    with open("/Library/Preferences/com.apple.Bluetooth.plist", "rb") as f:
        pl = plistlib.load(f)
    devices = pl.get("DeviceCache")
    ret = ""
    for d, v in devices.items():
        if v.get("Name") and device_name in v.get("Name"):
            right = v.get("BatteryPercentRight")
            left = v.get("BatteryPercentLeft")
            ret = '<br><span style="font-size: 8pt">L{0}% R{1}%</span>'.format(left, right)
            break
    return ret


HR = '<hr style="border:none;height:1px;background-color:lightgrey">'
BT_IMG = '<img src = "AirPods.widget/airpod.png">'
NO_BT_IMG = '<img src="AirPods.widget/noairpod.png">'
jsn = json.loads(os.popen('/usr/local/bin/blueutil --paired --format json').read())

#connected_list = ["{0} {1}".format(i.get('name'), airpod_battery_status(i.get('name'))) for i in jsn if i.get('connected') and "AirPods" in i.get('name')]
# connected_list = [i.get("name") for i in jsn if i.get('connected') and "AirPods" in i.get('name')]
connected_list = list()
for v in jsn:
    if v.get('connected') and "AirPods" in v.get('name'):
        name = v.get('name')
        ap_status = airpod_battery_status(name)
        connected_list.append("{0} {1}".format(name, ap_status))
connected = '<span style="color: grey">{0}AirPods not connected</span>'.format(NO_BT_IMG)
if len(connected_list) > 0:
    connected = "<br>".join(connected_list)
    connected = BT_IMG + connected
sys.stdout.write(connected)
