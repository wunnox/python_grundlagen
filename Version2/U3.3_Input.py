#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
###################################################################
#
# Uebung:
# Lesen Sie eine Zahl ein mit der input-Funktion
# Erstellen Sie eine Bedingung, welche für Zahlen grösser als 50 einen Text
# und für alle anderen Zahlen einen anderen Text schreibt.
#
###################################################################

#### Lösung: ####

# Eingabe einer Zahl
print("Bitte eine Zahl eingeben")
x = raw_input("-> ")

# Auswertung
if int(x) > 50:
    print("Die Zahl", x, "ist grösser als 50")
else:
    print("Die Zahl", x, "ist nicht grösser als 50")
