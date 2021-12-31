
import pyautogui
import requests
import time
import json

from numpy import interp

IP = "http://192.168.1.134"
IP_pos = ['gyrX', 'gyrY']
t=0.1
kx = 1600
ky = 1000
def move(x, y, t):
    pyautogui.moveRel(x, y, t)

while 1 == 1:
        url = IP + '/get?' + '&'.join(IP_pos)
        data_json = requests.get(url=url, timeout=5).json()

        gyr_x_str = json.dumps(data_json['buffer']['gyrX']['buffer'])
        gyr_y_str = json.dumps(data_json['buffer']['gyrY']['buffer'])
        gyr_x_str = gyr_x_str[1:-1]
        gyr_y_str = gyr_y_str[1:-1]
        gyr_x_new = ''.join(gyr_x_str)
        gyr_y_new = ''.join(gyr_y_str)
        gyr_x_float_m = float(gyr_x_new)
        gyr_y_float_m = float(gyr_y_new)

    #    while keyboard.is_pressed('space')== False:
        pos_y = gyr_x_float_m * t * ky
        pos_x = gyr_y_float_m * t * kx
        move(pos_x,pos_y,t)
