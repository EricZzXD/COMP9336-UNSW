# Import Lib
import sys
import subprocess
import os
from tabulate import tabulate
import math
# from API.py import *
from API import *

# netshData

# Pre-Requirement
path = "netshData"
listdir = os.listdir("netshData/")
filename = listdir[0]

# Join the Path - Get Full Pathway
pathJoin = os.path.join(path, filename)
f = open(pathJoin, 'r')
content = f.read()

overall_dic = []
Splited_SSID = split_ssids(content)

for i in range(len(Splited_SSID)):
    SSID_Info = get_SSID_Info(Splited_SSID[i])
    overall_dic.append(SSID_Info)

table_Array = []
for i in range(len(overall_dic)):
    ssid = overall_dic[i]["SSID"]
    for j in range(len(overall_dic[i]["SSID_Info"]["BSSID_Info"])):
        BSSID = overall_dic[i]["SSID_Info"]["BSSID_Info"][j][0]
        Signal = overall_dic[i]["SSID_Info"]["BSSID_Info"][j][1]
        Channel = overall_dic[i]["SSID_Info"]["BSSID_Info"][j][3]
        ssid_frequency = get_frequency(Channel)
        ssid_SignalStrength = get_SignalStrength(float(Signal.replace("%", "")))
        est_Distance = get_estDistance(ssid_frequency, Channel, ssid_SignalStrength)
        temp = [ssid, BSSID, ssid_frequency, Channel, est_Distance]
        table_Array.append(temp)

# Print Table
Table_head = ["SSID", "BSSID", "Frequency", "Channel", "Est. Distance (m)"]
print(tabulate(table_Array, headers=Table_head, tablefmt='orgtbl'))

