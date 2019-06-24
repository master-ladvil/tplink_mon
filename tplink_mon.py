#!/usr/bin/env python
import subprocess
import os
import time

def note():
    subprocess.call("clear")
    print("before running the script please verify that you have plugged in the network adaptor ")
    time.sleep(5)
    print("if you still got error type iwconfig and check weather the device is showing")
    time.sleep(5)
    subprocess.call("clear")
    print("if everything set we are good to go")
    print("tested on tp-link wn722n in kali and parrot")
    time.sleep(2)
    subprocess.call("clear")
    print("##########################################################")
    print("author -> master_ladvil")
    print("##########################################################")
    time.sleep(2)
    subprocess.call("clear")

def installing_drive():
    subprocess.call(["git", "clone", "https://github.com/kimocoder/rtl8188eus.git"])
    os.chdir("rtl8188eus")
    subprocess.call(["cp", "realtek_blacklist.conf", "/etc/modprobe.d"])
    subprocess.call("make")
   # subprocess.call("make install")

def net_man_restart():
    subprocess.call(["service", "network-manager", "restart"])
    print("please wait program is running....................")
    time.sleep(2)
    print("YOU LOOKING GOOD TODAY KIDDO")
    time.sleep(2)
    print("spennd time with your family too enjoy your life ")
    time.sleep(2)
    print("have a smile and wait your adaptor is forging to be a hackers device")
    time.sleep(2)
    print("your adaptor is in the process of converting from a cat to a beast process .....90%")
    time.sleep(3)

def turning_mon_mode_on():


    subprocess.call(["ifconfig", "wlan0", "down"])
    subprocess.call(["iwconfig", "wlan0", "mode", "monitor"])
    subprocess.call(["ifconfig", "wlan0", "up"])

def finishing():
    subprocess.call("clear")
    print("process completed ROCK-ON.....")
    print("am your friend so i will clean my mess on your terminal start fresh..............")
    time.sleep(5)
    subprocess.call("clear")

note()
installing_drive()
net_man_restart()
turning_mon_mode_on()
finishing()



