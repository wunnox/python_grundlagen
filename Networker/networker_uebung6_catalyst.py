#! env python3
##############################################
#
# Name: networker_uebung6_catalyst.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 04.10.2022
#
# Purpose: Eingestellter Speed und IO-Errors der Interfaces anzeigen
#
##############################################

# Modul importieren
from netmiko import ConnectHandler

# Verbindung herstellen mit key-File
#network_device={"host":"192.168.1.252", "username":"peter", 'use_keys':True, 'key_file':'/Users/peter/.ssh/id_rsa.pub', "device_type":"cisco_ios","secret":"Cisco123"}

# Verbindung herstellen mit Passwort
network_device={"host":"192.168.1.252", "username":"python", "password":"python12", "device_type":"cisco_ios",'secret':"Cisco123"}

connect=ConnectHandler(**network_device)

connect.enable()

# Modul importieren
import networker_uebung2_catalyst as cu2

#Variablen
interfaces=[]

#Daten aus Funktion einlesen
data=cu2.read_status()

#Daten nach new line aufspliten
allezeilen=data.rstrip(None).split("\n")

#Alle vorhandenen Interfaces auflisten
for zeile in allezeilen:
   words=zeile.split()
   if "Gi1" in zeile:
      interfaces.append(words[0])

#Switch-Daten auslesen
#Switch Name 
output=connect.find_prompt()
switchname=output.rstrip("#")

#Switch runtime Daten
cmd="show logging onboard"
output=connect.send_command(cmd)
for zeile in output.split("\n"):
   if "PID:" in zeile:
      switchtype=zeile.split()[1]
      switchsn=zeile.split()[7].rstrip()
   elif "Current uptime" in zeile:
      switchuptime=zeile.rstrip()
      
#Daten auslesen
#Header Daten
print("#"*70)
print(f"Angaben zu Switch {switchname}")
print("#"*70)
print(f"Switch Typ   : {switchtype}")
print(f"Switch SN    : {switchsn}")
print(f"Switch Uptime: {switchuptime[26:]}")
print("#"*70)
print()

#Interface Daten
fm="{0:<10}{1:<10}{2:>15}{3:>10}{4:>10}"
print(fm.format("Interface","Status","Speed","I-Err","O-Err"))
print("="*60)

for i in interfaces:
   cmd="show interfaces "+i
   output=connect.send_command(cmd)
   zeile=output.split('\n')
   if "notconnect" in zeile[0]:
      print(fm.format(i,"Not Connected", '', '', ''))
   else:
      for z in zeile:
         if "media type" in z:
            speed=z.split()[1].replace(",","")
         elif "input errors" in z:
            inputerror=int(z.split()[0])
         elif "output errors" in z:
            outputerror=int(z.split()[0])

      print(fm.format(i,"Connected", speed, inputerror, outputerror))
