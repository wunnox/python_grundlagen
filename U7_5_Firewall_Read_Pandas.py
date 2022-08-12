#!/usr/bin/python3
##############################################
#
# Name: U7_5_Firewall_Read_Pandas.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.10.2021 V1.0
#
# Purpose: Liest ein xlsx-File mit Pandas ein und schreibt Daten auf Bildschirm
#
##############################################

import pandas as pd
import sys

# Auf Fileangaben prüfen
l = len(sys.argv)
if l == 1:
    sourcefile = 'U7_5_Firewall_Log_Auszug.xlsx'
else:
    sourcefile = sys.argv[1]

#xlsx-File einlesen
data=pd.read_excel(sourcefile)

#Daten ausgeben
print(data.columns)
print('###################################################################################')
for i in data.index:
   print(data['Source IP'][i],data['Destination IP'][i], data['Port'][i], data['Protocol'][i], data['Count'][i])

print("\n", i, "Zeilen eingelesen")
