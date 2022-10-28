#! env python3
##############################################
#
# Name: networker_uebung3_CBS250.py
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

# Verbindung herstellen mit key-File
#network_device={"host":"192.168.1.252", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios","secret":"Cisco123"}

# Verbindung herstellen mit Passwort
network_device={"host":"192.168.1.252", "username":"python", "password":"python12", "device_type":"cisco_ios",'secret':"Cisco123"}

connect=ConnectHandler(**network_device)

# Kommandos ausführen und Resultat anzeigen
connect.enable()
connect.config_mode()
connect.send_command("interface Gi1",expect_string="switchaafe60.*")
connect.send_command("description \"PC Test Port 1\"",expect_string="switchaafe60.*")
connect.send_command("end",expect_string="switchaafe60.*")
cmd="wr"+"\ny\n"
print(connect.send_command_timing(cmd,delay_factor=2.0))

