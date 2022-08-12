#!/usr/bin/python3

import urllib.request
import urllib.parse
import urllib.error

# Eingabedaten
pnn = input("Bitte den Nachnamen eingeben: ")
pvn = input("Bitte den Vornamen eingeben: ")

# sendet Daten
u = urllib.request.urlopen("http://www.cssgmbh.ch/cssgmbh/Beispiele/senden_get.php?nn="
                           + pnn + "&vn=" + pvn)

# Empfang der Antwort und Ausgabe
li = u.readlines()
u.close()
ausgabe = ""
for element in li:
    ausgabe += str(element)
print(ausgabe)
