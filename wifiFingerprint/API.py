import math

# Split SSID
def split_ssids(netsh_Result):
    SplitSSID = netsh_Result.split("\nSSID ")

    # Remove the First Array (Netsh Intro)
    SplitSSID.pop(0)

    # Splited (removed) SSID, need to add back
    for i in range(len(SplitSSID)):
        SplitSSID[i] = "SSID " + SplitSSID[i]

    return SplitSSID


# Get SSID Info
def get_SSID_Info(ssid_array_splited):
    # Split the String base on ":" and clean all the spacing
    ssid_Split_Space = ssid_array_splited.split("\n")
    ssid_array = []
    for i in ssid_Split_Space:
        temp = i.split(" : ")
        if len(temp) == 2:
            temp[0] = temp[0].strip()
            temp[1] = temp[1].strip()
            ssid_array.append(temp)

    # Initial a Dictionary to store info
    dic = {}
    ssid_dic = {}
    temp_arr = []
    bssid_arr = []

    # Loop each array to store the information accordingly
    for ac in range(len(ssid_array)):
        # Get SSID and store in dic
        if ssid_array[ac][0].find("SSID") != -1 & ssid_array[ac][0].find("BSSID") != 0:
            dic["SSID"] = ssid_array[ac][1]

        # Get SSID and store in dic
        elif ssid_array[ac][0].find("Network type") != -1:
            ssid_dic.update({"NetworkType": ssid_array[ac][1]})
            dic["SSID_Info"] = ssid_dic

        # Get SSID and store in dic
        elif ssid_array[ac][0].find("Authentication") != -1:
            ssid_dic.update({"Authentication": ssid_array[ac][1]})
            dic["SSID_Info"] = ssid_dic

        # Get SSID and store in dic
        elif ssid_array[ac][0].find("Encryption") != -1:
            ssid_dic.update({"Encryption": ssid_array[ac][1]})
            dic["SSID_Info"] = ssid_dic

        # Get BSSID info and store as Array
        elif ssid_array[ac][0].find("BSSID") == 0:
            if len(temp) > 0:
                bssid_arr.append(temp_arr)
                temp_arr = []
                temp_arr.append(ssid_array[ac][1])

                # when Counter reach to the end,
        elif ac == len(ssid_array) - 1:
            # Update array List
            temp_bssid = []
            bssid_arr.append(temp_arr)

            # Clean the List
            for l in bssid_arr:
                if len(l) != 0:
                    temp_bssid.append(l)

            # Write the List to Dictionary
            bssid_arr = temp_bssid
            ssid_dic.update({"BSSID_Info": bssid_arr})

        else:
            temp_arr.append(ssid_array[ac][1])

    return dic


# Get Distance
def get_estDistance(Frequency, Channel, SignalStrength):
    # Info Link: https://en.wikipedia.org/wiki/List_of_WLAN_channels
    # Frequency Table 2.4Ghz & 5GHz
    FT_2_4 = [[1, 2412], [2, 2417], [3, 2422], [4, 2427], [5, 2432], [6, 2437], [7, 2442], [8, 2447], [9, 2452],
              [10, 2457], [11, 2462], [12, 2467], [13, 2472], [14, 2484]]
    FT_5 = [[32, 5160], [34, 5170], [36, 5180], [38, 5190], [40, 5200], [42, 5210], [44, 5220], [46, 5230], [48, 5240], [50, 5250], [52, 5260], [54, 5270], [56, 5280], [58, 5290], [60, 5300], [62, 5310], [64, 5320], [68, 5340], [96, 5480], [100, 5500], [102, 5510], [104, 5520], [106, 5530], [108, 5540], [110, 5550], [112, 5560], [114, 5570], [116, 5580], [118, 5590], [120, 5600], [122, 5610], [124, 5620], [126, 5630], [128, 5640], [132, 5660],
            [134, 5670], [136, 5680], [138, 5690], [140, 5700], [142, 5710], [144, 5720], [149, 5745], [151, 5755], [153, 5765], [155, 5775], [157, 5785], [159, 5795], [161, 5805], [163, 5815], [165, 5825], [167, 5835], [169, 5845], [171, 5855], [173, 5865], [175, 5875], [177, 5885], [182, 5910], [183, 5915], [184, 5920], [187, 5935], [188, 5940], [189, 5945], [192, 5960], [196, 5980]]

    SignalStrength = abs(float(SignalStrength))
    Channel_Freq = 0

    if Frequency == "2.4 GHz":
        for i in FT_2_4:
            if i[0] == int(Channel):
                Channel_Freq = i[1]
                break
    else:
        for i in FT_5:
            if i[0] == int(Channel):
                Channel_Freq = i[1]
                break

    result = 10 ** ((27.55 - (20 * math.log10(Channel_Freq)) + SignalStrength) / 20)
    return result


# Get Signal Strength
def get_SignalStrength(rssi):
    if (float(rssi<=0)):
        dbm = 100
    elif (float(rssi)>100):
        dbm = -50
    else:
        dbm = float(rssi)/2-100
    return dbm


# Get Frequency
def get_frequency(Channel):
    if int(Channel) <= 14:
        ssid_frequency = "2.4 GHz"
    else:
        ssid_frequency = "5 GHz"

    return ssid_frequency


def Pre_Analysis(content):
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

    return table_Array


# https://hlab.stanford.edu/brian/euclidean_distance_in.html#:~:text='n'%2DDimensional%20Euclidean%20Distance&text=Euclidean%20distance%20is%20a%20measure,two%20points%20in%20Euclidean%20space.&text=In%20an%20example%20where%20there,is%20only%201%20Dimensional%20space.
# Multi N Dimensional Distance
def NDD(arr1, arr2):

    # If the Array size are not match, then return error
    if len(arr1) != len(arr2):
        return "ERROR"

    # Calculate the Sum
    tempsum = 0
    for i in range(len(arr1)):
        tempsum = tempsum + (arr1[i]-arr2[i])**2

    # Calculate the Result
    distance = math.sqrt(tempsum)

    return distance
