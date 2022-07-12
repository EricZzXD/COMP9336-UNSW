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
path = "DataCollection"
listdir = os.listdir("DataCollection/")


# Join the Path - Get Full Pathway
filename = listdir[0]
print(filename)
pathJoin1 = os.path.join(path, filename)
f = open(pathJoin1, 'r')
read_file1 = f.read()
result = Pre_Analysis(read_file1)


# Join the Path - Get Full Pathway
filename2 = listdir[1]
print(filename2)
pathJoin2 = os.path.join(path, filename2)
f = open(pathJoin2, 'r')
read_file2 = f.read()
result2 = Pre_Analysis(read_file2)


temp_arr1 = []
temp_arr2 = []

distance1 = []
distance2 = []

# #
for i in range(len(result)):
    for j in range(len(result2)):
        if result[i][1] == result2[j][1] and result[i][2] == result2[j][2] and result[i][3] == result2[j][3] and abs(result2[j][4]-result[i][4]) < 5:
            distance1.append(result[i][4])
            distance2.append(result2[j][4])
            temp_arr1.append(result[i])
            temp_arr2.append(result2[j])

print(NDD(distance1, distance2))





