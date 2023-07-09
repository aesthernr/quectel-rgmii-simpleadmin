# Simple Web Admin Interface for Quectel Modem using RJ45 Boards 
Simple Admin / Monitoring web UI for Quectel modems that are connected via a RGMII Ethernet interface (aka a "RJ45 to M.2" or "Ethernet to M.2" adapter board). 

This heavily relies on the work of <a href="https://github.com/natecarlson/">Nate</a> building on top of <a href="https://github.com/natecarlson/quectel-rgmii-at-command-client/tree/main/at_telnet_daemon">at_telnet_daemon</a> which is required prerequisite install before this will work. 

## Requirements
* ADB access to your modem 
* Installing Nate's at_telnet_daemon


## Installation
```bash
adb push quectel-rgmii-simpleadmin /usrdata/simpleadmin
adb shell chmod +x /usrdata/simpleadmin/scripts /usrdata/simpleadmin/www/cgi-bin
adb shell mount -o remount,rw /
adb shell cp /usrdata/simpleadmin/systemd/* /lib/systemd/system
adb shell systemctl daemon-reload
adb shell ln -s /lib/systemd/system/simpleadmin_httpd.service /lib/systemd/system/multi-user.target.wants/
adb shell ln -s /lib/systemd/system/simpleadmin_generate_status.service /lib/systemd/system/multi-user.target.wants/
adb shell ln -s /lib/systemd/system/simpleadmin_generate_status.timer /lib/systemd/system/timers.target.wants/
adb shell mount -o remount,ro /
adb shell systemctl start simpleadmin_generate_status
adb shell systemctl start simpleadmin_generate_status.timer
adb shell systemctl start simpleadmin_httpd
```

## Access Simple Admin
This will launch on port 8080 by default, you are welcome to change that if you do not desire to use the QCMAP_CLI in the simpleadmin_generate_status.service file. 

Launch your browser to http://192.168.225.1:8080 

## Acknowledgements
This heavily uses the AT Command Parsing Scripts (Basically a copy with minor tweaks) of Dairyman's Rooter Source https://github.com/ofmodemsandmen/ROOterSource2203
