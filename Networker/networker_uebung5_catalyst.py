#! env python3
##############################################
#
# Name: networker_uebung5_catalyst.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 04.09.2022
#
# Purpose: Auf den Status "up" prüfen der Interfaces
#
##############################################

# Modul importieren
import networker_uebung2_catalyst as cu2

#Daten aus Funktion einlesen
data=cu2.read_description()

#Daten nach new line aufspliten
allezeilen=data.rstrip(None).split("\n")

print("{0:<10}{1:<10}{2:<10}{3:<15}{4:<4}".format("Interface","Linkstat.","Protocol","Description","Status"))
fm = "{0:<10}{1:<10}{2:<10}{3:<15}{4:<4}"

for zeile in allezeilen:
   feld=zeile.split()
   status="ok"
   if "Gi1" in feld[0]:
      if feld[1]!="up": status="nok"
      if feld[2]!="up": status="nok"
      if len(feld)>3:
          desc=" ".join(feld[3:])
      else:
         desc=""
      
      if status=="ok":
         print(fm.format(feld[0],feld[1],feld[2],desc,'\033[{}m'.format(92)+status+'\033[0m'))
      else:
         print(fm.format(feld[0],feld[1],feld[2],desc,'\033[{}m'.format(91)+status+'\033[0m'))

