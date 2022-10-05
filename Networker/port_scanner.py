#! env python3
##############################################
#
# Name: port_scanner.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Prüfen von Port-Verfügbarkeit auf Remote Server mit nc
#
##############################################

import os

#Variabeln
host="192.168.1.150"
ports=[22,80]

#Verbindung testen
for port in range(ports[0],ports[1]+1):
   nc = os.system("nc -w 1 " + host + " " + str(port))

   #Auswerten des Resultates
   if nc==0:
      print ("Port", port, "zu Host", host, "ist offen")
   else:
      print ("Port", port, "zu Host", host, "ist gesperrt")
