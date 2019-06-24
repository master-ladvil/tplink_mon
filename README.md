# tplink_mon
# tplink-mon
an ultimate tool that fixes all the errors changes your wifi adaptor to monitor mode. 
best tool to fix the common error in setting monitor mode for the device 
TP-LINK TL-WN722N

error:

Error for wireless request "Set Mode" (8B06) :
     SET failed on the device wlan0 :operation not permitted

this script will 100% work for this error
requirements:

check wheather you have connected your wifi adaptor before running the script
go to devices -> usb -> and check wheather there is a tick mark in your adaptor
or type "lsusb" and check wheather it has the name of your wifi adaptor
type "iwconfig" and verify you have your wifi adaptor mentioned

after finishing the script do "iwconfig" and vola yu can see it has changed to mon mode


nothing more to do just plugin and run the script to change tomon mode

if you copy this code please give credits to the author

author -> master_ladvil 


USAGE:
git clone this repository
type "git clone" followed by th link of thi repository
cd tp-link_mon
chmod 777 tplink_mon.py
./tplink_mon.py
(or)
python tplink_mon.py
