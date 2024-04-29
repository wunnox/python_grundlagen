#!/usr/bin/python3
###################################################################
#
# Uebung:
# Erstellen Sie eine CSV Datei mit folgendem Inhalt
#    Artikelnummer: 12-3467-9
#    Artikel: Schraube
#    Typ: M10
#
# Lesen Sie danach die CSV Datei wieder ein und geben Sie nur den Namen des Artikels aus
# 
#  Sie kriegen folgende Ausgabe:
#
#    Schraube
#
###################################################################

#### Lösung: ####

import csv

# Daten in Variable schrieben
data='"12-3467-9","Schraube","M10"\n'

# Daten in Datei schreiben
with open("Datei.csv", 'w') as d:
   d.write(data)

# Datei einlesen
with open('Datei.csv', 'r') as c:
   data = csv.reader(c, delimiter=',',quotechar='"')

   # Nur Artikelname ausgeben
   for zeile in data:
      print(zeile[1])

