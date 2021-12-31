import pyautogui
import requests
import time
import json

pyautogui.FAILSAFE = False
IP = "http://143.195.43.203"
IP_pos = ["accX","accY"]
dt=0.3
k = 1
def move(x,y):
    pyautogui.moveRel(x,y)


while 1==1:
    url = IP + "/get?" + ("&".join(IP_pos))
    data_json = requests.get(url=url,timeout = 5).json()
    acc_x_str = json.dumps(data_json["buffer"]["accX"]["buffer"])
    acc_y_str = json.dumps(data_json["buffer"]["accY"]["buffer"])
    acc_x_str = acc_x_str[1:-1]
    acc_y_str = acc_y_str[1:-1]
    
    acc_x_new = ''.join(acc_x_str)
    acc_y_new = ''.join(acc_y_str)

    acc_x_float_m = -1*float(acc_x_new)
    acc_y_float_m = float(acc_y_new)
    
##    print(str(acc_x_float_m) + " , " + str(acc_y_float_m))
    if abs(acc_x_float_m) <0.2:
        acc_x_float_m = 0
    if abs(acc_y_float_m) < 0.2:
        acc_y_float_m = 0

    print(str(acc_x_float_m) + " , " + str(acc_y_float_m))
    
    acc_x_float_px = acc_x_float_m * 3779.5275590551
    acc_y_float_px = acc_y_float_m * 3779.5275590551

    pos_x = (0.5*acc_x_float_px*dt**2)
    pos_y = (0.5*acc_y_float_px*dt**2)
    
    move(pos_x,pos_y)
    
