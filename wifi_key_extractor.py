#!usr/bin/python3
import subprocess as sp
import re
cmd_output = sp.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
profile_names = re.findall("All User Profile     : (.*)\r", cmd_output)
wifi_list=list()
if profile_names:
    for name in profile_names:
        profile = dict()
        key_output = sp.run(["netsh", "wlan", "show", "profiles", name], capture_output=True).stdout.decode()
        key_check = re.findall("Security key           : Present", key_output)
        profile["ssid"] = name
        if key_check:
            see_key = sp.run(["netsh", "wlan", "show", "profiles", name,"key=clear"], capture_output=True).stdout.decode()
            key = re.findall("Key Content            : (.*)\r",see_key)
            profile["password"] = key[0]
        else:
            profile["password"] = "None"
        wifi_list.append(profile)
    print("{0:30}\t{1:20}".format("SSID", "PASSWORD"))
    for x in wifi_list:
        ssid=x["ssid"]
        password= x["password"]
        print("{0:30}\t{1:20}".format(ssid, password))
    prompt=str(input("Enter 'y' To Save To File: "))
    if prompt=='y':
        fname=str(input("Enter Name To Save As: "))
        file=open(fname+".txt", "w")
        file.write("{0:30}\t{1:20}\n\n".format("SSID", "PASSWORD"))
        for x in wifi_list:
            ssid = x["ssid"]
            password = x["password"]
            file.write("{0:30}\t{1:20}\n".format(ssid, password))
        file.close();
    else:
        print("GoodBye")
else:
    print("[==========]No Wifi Profile Found[==========]")
