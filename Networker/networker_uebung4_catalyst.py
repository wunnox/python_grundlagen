#! env python3
##############################################
#
# Name: networker_uebung4_catalyst.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 26.08.2022 1.0
#
# Purpose: Setzen von mehreren Interface Description auf einem Switch
#
##############################################

# Modul importieren
from netmiko import ConnectHandler
import logging

#Logging aktivieren
logging.basicConfig(filename='netmiko.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Verbindung herstellen mit key-File
#network_device={"host":"192.168.1.252", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios","secret":"Cisco123"}

# Verbindung herstellen mit Passwort
network_device={"host":"192.168.1.252", "username":"python", "password":"python12", "device_type":"cisco_ios",'secret':"Cisco123"}

connect=ConnectHandler(**network_device)
connect.enable()

#Interface Description setzen
for i in ("2","3","4","5","6"):
   cmd=["int Gi1/0/"+i,"description PC Test Port "+i]
   print(connect.send_config_set(cmd))

#Änderungen speichern
cmd=["end","wr"]
print(connect.send_config_set(cmd))
