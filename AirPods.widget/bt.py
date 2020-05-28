#!/usr/bin/python

import json
import os
import sys

HR = '<hr style="border:none;height:1px;background-color:lightgrey">'
BT_IMG = '<img src = "AirPods.widget/airpod.png">'
NO_BT_IMG = '<img src="AirPods.widget/airpod.png">'
jsn = json.loads(os.popen('/usr/local/bin/blueutil --paired --format json').read())

connected_list = [i.get('name') for i in jsn if i.get('connected') and "AirPods" in i.get('name')]
connected = '<span style="color: grey">{0}AirPods not connected</span>'.format(NO_BT_IMG)
if len(connected_list) > 0:
    connected = "<br>".join(connected_list)
    connected = BT_IMG + connected
sys.stdout.write(connected)
