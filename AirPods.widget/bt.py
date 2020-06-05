#!/usr/bin/python3

import json
import os
import plistlib
import sys


class AirPod(object):
    def __init__(self, address: str, name: str, left: str, right: str, case: str):
        self.address = address
        self.name = name
        self.left = left
        self.right = right
        self.case = case


# for debugging purpose defaults read /Library/Preferences/com.apple.Bluetooth
def airpod_battery_status(device_id: str) -> tuple:
    """
    Get device status with a given address (MAC)

    Args:

        device_id (str): MAC address of the Device to search


    Returns:

        dict: Left/Right battery status

    """
    with open("/Library/Preferences/com.apple.Bluetooth.plist", "rb") as f:
        pl = plistlib.load(f)
    devices: dict = pl.get("DeviceCache")
    ret: tuple = tuple()
    for d, v in devices.items():
        if device_id in d:
            right: str = v.get("BatteryPercentRight") if v.get("BatteryPercentRight") else None
            left: str = v.get("BatteryPercentLeft") if v.get("BatteryPercentLeft") else None
            case: str = v.get("BatteryPercentCase") if v.get("BatteryPercentCase") else None
            ret = (left, right, case)
            break
    return ret


def airpods_connected() -> list:
    """
    Get Connected Airpods

    Returns:

        list: Return AirPod Device Object-list with address, name, left/right battery

    """
    jsn = json.loads(os.popen('/usr/local/bin/blueutil --paired --format json').read())
    connected_aps: list = list()
    for v in jsn:
        name: str = v.get('name')
        address: str = v.get('address')
        if v.get('connected') and "AirPods" in v.get('name'):
            left, right, case = airpod_battery_status(address)
            ap = AirPod(address, name, left, right, case)
            connected_aps.append(ap)
    return connected_aps


def device_strings() -> list:
    """
    Generates list of devices incl name and battery status of Airpods

    Returns:

        list: List of HTML strings

    """
    aps: list = airpods_connected()
    devices = list()
    for ap in aps:
        left: str = f"L {ap.left}%" if ap.left else ""
        right: str = f"R {ap.right}%" if ap.right else ""
        case: str = f"C {ap.case}%" if ap.case else ""
        name: str = ap.name
        d_str = name
        if left is not "" or right is not "":
            d_str = f'{name}<br><span style="font-size: 8pt">{left} {right} {case}</span>'
        devices.append(d_str)
    return devices


BT_IMG = '<img src = "AirPods.widget/airpod.png">'
NO_BT_IMG = '<img src="AirPods.widget/noairpod.png">'

connected_list = device_strings()
connected = f'<span style="color: grey">{NO_BT_IMG}AirPods not connected</span>'
if len(connected_list) > 0:
    connected = "<br>".join(connected_list)
    connected = f"{BT_IMG}{connected}"
sys.stdout.write(connected)
