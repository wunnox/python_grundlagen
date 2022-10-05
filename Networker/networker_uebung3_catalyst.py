#! env python3
##############################################
#
# Name: networker_uebung3_catalyst.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 26.08.2022 1.0
#
# Purpose: Setzen einer Interface Description auf einem Switch
#
##############################################

# Modul importieren
from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='netmiko.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Verbindung herstellen
#network_device={"host":"192.168.1.252", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios"}
network_device={"host":"192.168.1.252", "username":"peter", "password":"Cisco123", "device_type":"cisco_ios",'secret':"Cisco123"}

connect=ConnectHandler(**network_device)
connect.enable()

# Kommandos ausführen und Resultat anzeigen
cmd=["int Gi1/0/1","description Test Port 1","end","wr"]
output= connect.send_config_set(cmd)
print(output)

