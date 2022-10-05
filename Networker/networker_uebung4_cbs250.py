#! env python3
##############################################
#
# Name: networker_uebung4_cbs250.py
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

# Verbindung herstellen
network_device={"host":"192.168.1.146", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios"}
#network_device={"host":"192.168.1.146", "username":"peter", "password":"Cisco123", "device_type":"cisco_ios",'timeout':5}
connect=ConnectHandler(**network_device)

connect.enable()
connect.config_mode()

#Interface Description setzen
for i in ("2","3","4","5","6"):
   cmd="interface "+"gi"+i
   connect.send_command(cmd,expect_string="switchaafe60.*")
   cmd=f"description \"Test Port {i}\""
   connect.send_command(cmd,expect_string="switchaafe60.*")

#Änderungen speichern
connect.send_command("end",expect_string="switchaafe60.*")
cmd="wr"+"\ny\n"
connect.send_command_timing(cmd,delay_factor=3.0)
