# This is used for Data collection and store at a folder for furtehr analysis
import subprocess
import sys
import os

# You may want to to run code: (Can change name here)
filename = "data0"

# Path name and join (Dont modify)
path = "netshData"
fileType = ".txt"
fileall = filename + fileType
pathJoin = os.path.join(path, fileall)

# Run the command to search the SSID nearby and save txt file
results = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=BSSID"])

# Open and write Byte to txtx file
text_file = open(pathJoin, "wb")
text_file.write(results)
text_file.close()
