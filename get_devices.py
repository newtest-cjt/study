#coding=utf-8
import os
import re

def get_deviceid():                            #get设备id
    devices = []
    readDeviceId = list(os.popen('adb devices').readlines())
    for i in range(1,len(readDeviceId)-1):
        deviceId = re.findall(r'\w*', readDeviceId[i])[0]
        devices.append(deviceId)
    print(devices)
    return devices
get_deviceid()
# def main():
#     for i in range(2):
#         p1='adb -s '+dev_id[i]+' shell input tap 1 1'
#         print('设备号 %s 点击坐标（1,1）'%(dev_id[i]))
#         os.system(p1)
#main()