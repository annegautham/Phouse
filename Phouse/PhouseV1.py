import urllib.request
import time
import webbrowser  


IPAddress = '192.168.1.132'  #IP address and port This is different for each person and specified by the phyphox app
num_data = 5 #Take 5 data chunks
pause_tm = 2 #The amount of time to wait in between data collections


save_dat = 'http://' + IPAddress + '/export?format=0'  #Saving data
clear_dat = 'http://' + IPAddress + '/control?cmd=clear'  #Clearing a data collection
start_dat = 'http://' + IPAddress + '/control?cmd=start'  #Starting a data collection


# Here is where the program actually starts, everything beforehand was just prep

urllib.request.urlopen(start_dat) #Start collecting data!!

for v in range(0,num_data):
   webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(save_dat) #Open a chrome window (note if your not on windows you need to change the location of chrome) and save data!
   time.sleep(pause_tm) #Wait a bit before collecting data again

urllib.request.urlopen(clear_dat)  #Clear the data Collection
urllib.request.urlopen(start_dat) #Restart the data collection

#Collect data again, for fun, why not
for v in range(0,num_data):
   webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(save_dat)
   time.sleep(pause_tm)

urllib.request.urlopen(clear_dat)  #Clear the data Collection

