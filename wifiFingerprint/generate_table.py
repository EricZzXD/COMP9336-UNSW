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


# Join the Path - Get Full Pathway
filename = listdir[0]
pathJoin1 = os.path.join(path, filename)
f = open(pathJoin1, 'r')
read_file1 = f.read()
result = Pre_Analysis(read_file1)


# Join the Path - Get Full Pathway
filename2 = listdir[1]
pathJoin2 = os.path.join(path, filename2)
f = open(pathJoin2, 'r')
read_file2 = f.read()
result2 = Pre_Analysis(read_file2)

#
# # Print Table
# Table_head = ["SSID", "BSSID", "Frequency", "Channel", "Est. Distance (m)"]
# print(tabulate(result, headers=Table_head, tablefmt='orgtbl'))
#
# print(tabulate(result2, headers=Table_head, tablefmt='orgtbl'))

temp_arr1 = []
temp_arr2 = []

distance1 = []
distance2 = []

#
for i in range(len(result)):
    for j in range(len(result2)):
        if result[i][1] == result2[j][1] and abs(result2[j][4]-result[i][4]) < 10:
            distance1.append(result[i][4])
            distance2.append(result2[j][4])
            temp_arr1.append(result[i])
            temp_arr2.append(result2[j])

print(NDD(distance1, distance2))

print(result)
print(result2)

#
# for i in range(len(result)):
#     for j in range(len(result2)):
#         if result[i][0] == result2[j][0]:
#             print(abs(result2[j][4]-result[i][4]))
#             print(result[i])
#             print(result2[j])








