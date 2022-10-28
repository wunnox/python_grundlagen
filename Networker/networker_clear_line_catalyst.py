#! env python3
##############################################
#
# Name: networker_clear_line_catalyst.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 26.08.2022 1.0
#
# Purpose: Macht die Verbindungen frei, wenn mehr als 10 belegt sind
#
##############################################

# Modul importieren
from netmiko import ConnectHandler
import logging
import time
import re

#Logging aktivieren
logging.basicConfig(filename='netmiko.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Verbindung herstellen mit key-File
#network_device={"host":"192.168.1.252", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios","secret":"Cisco123"}

# Verbindung herstellen mit Passwort
network_device={"host":"192.168.1.252", "username":"python", "password":"python12", "device_type":"cisco_ios",'secret':"Cisco123"}

connect=ConnectHandler(**network_device)
connect.enable()

connect.enable()

# Auf belegte Lines prüfen
stars=0
sl=connect.send_command("show line")
zeilen=sl.split("\n")
for zeile in zeilen:
   if re.findall("^\*",zeile):
      stars+=1

# Nötigenfalls belegte Lines frei machen
if stars>10:
   print(f"{stars} stars found, starting a cleanup")
   for i in range(1,16):
      cmd="clear line vty "+str(i)
      print(i,":",end='')
      print(connect.send_command_timing(cmd))
      print(connect.send_command("\n"))
      time.sleep(0.2)
   print(connect.send_command("show line"))
else:
   print(f"Only {stars} stars found, no cleanup needed")

