#!/usrdata/micropython/micropython

import sys
# Remove the home directory from sys.path.
if "~/.micropython/lib" in sys.path:
    sys.path.remove("~/.micropython/lib")
sys.path.append("/usrdata/micropython")
import serial
import uos

# Do not put AT in front. The System place it for you
statusCommands=[
    "+QSPN",
    "+CEREG=2;+CEREG?;+CEREG=0",
    "+C5GREG=2;+C5GREG?;+C5GREG=0",
    "+CSQ",
    "+QENG=\"servingcell\"",
    "+QRSRP",
    "+QCAINFO",
    "+QNWPREFCFG=\"mode_pref\"",
    "+QTEMP"
]

# Build AT Command by joining together calls
cmd = 'AT' + ';'.join(statusCommands) + "\r\n"

# Open Serial & Fire Command
ser = serial.Serial("/dev/ttyOUT", baudrate=115200)
ser.write(cmd)

uos.system("sleep 0.025s")

# Write out serial data
out=b''
while ser.in_waiting > 0:
    out += ser.read(1)


f = open('/tmp/modemstatus.txt', 'w')
f.write(out)
f.close()
ser.close()