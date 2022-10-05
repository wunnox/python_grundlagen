#! env python3
##############################################
#
# Name: networker_uebung2_cbs250.py
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

#Funktionen
def read_description():
   '''Anzeigen der Interface Description'''
   cmd="show interface description"
   output=connect.send_command_timing(cmd)
   return output

def read_status():
   '''Anzeigen des Interface Status'''
   cmd="show interface status"
   output=connect.send_command_timing(cmd)
   return output

# Verbindung herstellen
#network_device={"host":"192.168.1.146", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios"}
#network_device={"host":"192.168.1.146", "username":"peter", "password":"Cisco123", "device_type":"cisco_ios",'timeout':5}
network_device={"host":"192.168.1.252", "username":"peter", "password":"Cisco123", "device_type":"cisco_ios",'secret':"Cisco123"}
connect=ConnectHandler(**network_device)

connect.enable()

# Kommando ausführen und Resultat anzeigen
if __name__=='__main__':
   # Kommando ausführen und Resultat anzeigen
   print("# Show Inteface #########################")
   print(read_description())
   print("\n# Show Status #########################")
   print(read_status())

