import math
import pyautogui
import requests
import time
import json
from numpy import interp

pyautogui.FAILSAFE = False
IP = 'http://' + input("Enter IP Adress from PhyPhox: ")
IP_pos = ['accX', 'accY']
dt = 14
i = 1
k=1

def myround(x, base):
    return base * round(float(x) / base)



def move(x, y, t):
    pyautogui.moveRel(x, y, t)

while 1 == 1:
    i=1
    posXvals = [0]
    posYvals = [0]
    accXvals=[]
    accYvals=[]
    while i <= 1:
        url = IP + '/get?' + '&'.join(IP_pos)
        data_json = requests.get(url=url, timeout=5).json()
        acc_x_str = json.dumps(data_json['buffer']['accX']['buffer'])
        acc_y_str = json.dumps(data_json['buffer']['accY']['buffer'])
        acc_x_str = acc_x_str[1:-1]
        acc_y_str = acc_y_str[1:-1]
        acc_x_new = ''.join(acc_x_str)
        acc_y_new = ''.join(acc_y_str)
        acc_x_float_m = -1 * float(acc_x_new)
        acc_y_float_m = float(acc_y_new)

        myround(acc_x_float_m,0.25)
        myround(acc_y_float_m,0.5)

        if abs(acc_x_float_m) <0.525:
            acc_x_float_m = 0
        if abs(acc_y_float_m) < 0.525:
            acc_y_float_m = 0
        
        acc_x_float_px = acc_x_float_m * k
        acc_y_float_px = acc_y_float_m * k
        accXvals.append(acc_x_float_px)
        accYvals.append(acc_y_float_px)
        i+=1

    for a in accXvals:
        posXvals.append(posXvals[-1] + 0.5 * a * dt ** 2)

    for b in accYvals:
        posYvals.append(posYvals[-1] + 0.5 * b * dt ** 2)
    print(posXvals)
    print(posYvals)
    
    absPosition = math.sqrt(posXvals[len(posXvals)-1]**2 + posYvals[len(posYvals)-1]**2)
    move(posXvals[len(posXvals)-1],posYvals[len(posYvals)-1],interp(absPosition,[0,1768],[0,0.68]))

