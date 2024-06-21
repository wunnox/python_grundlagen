#!/usr/bin/python3
###################################################################
#
# Uebung:
# Erstellen Sie eine JSON Datei mit folgendem Inhalt
#    Artikelnummer: 12-3467-9
#    Artikel: Schraube
#    Typ: M10
#
# Lesen Sie danach die JSON Datei wieder ein und geben Sie nur den Namen des Artikels aus
# 
#  Sie kriegen folgende Ausgabe:
#
#    Schraube
#
###################################################################

#### Lösung: ####

import json

# Dictionary erstellen
data={"Artikelnummer":"12-3467-9","Artikel":"Schraube","Typ":"M10"}

# Daten in Datei schreiben
with open("Datei.json", 'w') as d:
   json.dump(data, d)

# Datei einlesen
data = json.load(open("Datei.json"))

# Nur Artikelname ausgeben
print("Artikel")
print(data["Artikel"])

