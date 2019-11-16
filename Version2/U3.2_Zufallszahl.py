#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
###################################################################
#
# Uebung:
# Generieren Sie eine Zufallszahl zw. 100 und 1000 und schreiben Sie
# diese in die Variable z
# Geben Sie den Inhalt der Variable z auf dem Bildschirm aus.
#
###################################################################

#### Lösung: ####

# Modul random importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Zufallswerte und Berechnung
z = random.randint(100, 1000)

# Ausgabe
print("Zufallszahl:", z)
