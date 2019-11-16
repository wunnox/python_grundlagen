#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import urllib

# Eingabedaten
pnn = raw_input("Bitte den Nachnamen eingeben: ")
pvn = raw_input("Bitte den Vornamen eingeben: ")

# sendet Daten
u = urllib.urlopen("http://www.cssgmbh.ch/cssgmbh/Beispiele/senden_get.php?nn="
                           + pnn + "&vn=" + pvn)

# Empfang der Antwort und Ausgabe
li = u.readlines()
u.close()
ausgabe = ""
for element in li:
    ausgabe += str(element)
print(ausgabe)
