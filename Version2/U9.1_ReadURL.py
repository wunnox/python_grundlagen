#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
###################################################################
#
# Uebung:
# Lesen Sie die URL "http://www.cssgmbh.ch/cssgmbh/Beispiele/url_lesen.htm" ein
# Prüfen Sie, ob die Seite den Text "Hallo Python" beinhaltet
# Wenn ja, geben Sie den Text aus: "Seite ist ok"
# Ansonsten geben Sie den Text aus: "Seite ist nicht ok"
#
###################################################################

#### Lösung: ####

import urllib

# URL einlesen
u = urllib.urlopen(
    "http://www.cssgmbh.ch/cssgmbh/Beispiele/url_lesen.htm")
li = u.readlines()
u.close()

# Prüfe auf spezifischen Inhalt
e = "Seite ist nicht ok"
for element in li:
    if b"Hallo Python" in element:
        e = "Seite ist ok"

print(e)
