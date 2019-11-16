#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
###################################################################
#
# Uebung:
# Lesen Sie mit der Funktion raw_input() eine Zahl in eine Variable.
# Addieren Sie den Wert 5 und geben Sie die Summe aus.
# Stellen Sie sicher, dass eine falsche Eingabe kein Programmabbruch
# bewirkt, sonder eine entsprechende Meldung ausgegeben wird.
#
###################################################################

#### Lösung: ####

# Eingabe
print("Bitte geben Sie eine ganze Zahl ein")
z = raw_input("-> ")

# Versuch der Berechnung
try:
    print(z + 5)

# Fehler bei Umwandlung
except BaseException:
    print(z, "ist keine Zahl")
