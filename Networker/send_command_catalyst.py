#! env python3
##############################################
#
# Name: send_command.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 26.08.2022 1.0
#
# Purpose: Fragt die aktiven ssh-Sessions auf einem Switch ab
#
##############################################

# Modul importieren
from netmiko import ConnectHandler

# Verbindung herstellen
#network_device={"host":"192.168.1.252", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios"}
network_device={"host":"192.168.1.252", "username":"peter", "password":"Cisco123", "device_type":"cisco_ios",'secret':"Cisco123"}

connect=ConnectHandler(**network_device)
connect.enable()

# Kommando ausführen und Resultat ausgeben
cmd="show ip ssh"
print(connect.send_command(cmd))
