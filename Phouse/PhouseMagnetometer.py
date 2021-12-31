import pyautogui
import requests
import time
import json

pyautogui.FAILSAFE = False
IP = "http://192.168.1.134"
IP_pos = ['magX', 'magY']
k=10
t=0.1
def move(x, y, t):
    pyautogui.moveRel(x, y, t)

while 1 == 1:
        url = IP + '/get?' + '&'.join(IP_pos)
        data_json = requests.get(url=url, timeout=5).json()

        gyr_x_str = json.dumps(data_json['buffer']['magX']['buffer'])
        gyr_y_str = json.dumps(data_json['buffer']['magY']['buffer'])
        gyr_x_str = gyr_x_str[1:-1]
        gyr_y_str = gyr_y_str[1:-1]
        gyr_x_new = ''.join(gyr_x_str)
        gyr_y_new = ''.join(gyr_y_str)
        gyr_x_float_m = float(gyr_x_new)-27.75
        gyr_y_float_m = -1* (float(gyr_y_new)+8)

        if abs(gyr_x_float_m)<12:
            gyr_x_float_m = 0
        if abs(gyr_y_float_m)<20:
            gyr_y_float_m =0
    

    #    while keyboard.is_pressed('space')== False:
        pos_x = gyr_x_float_m * k
        pos_y = gyr_y_float_m * k
        move(pos_x,pos_y,t)
