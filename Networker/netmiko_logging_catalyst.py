#! env python3
##############################################
#
# Name: netmiko_logging_catalyst.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 26.08.2022 1.0
#
# Purpose: Fragt die Interface Description auf einen Switch ab
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

# Kommando ausführen und Resultat anzeigen
cmd="show interface description"
print(connect.send_command(cmd))

