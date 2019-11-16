#!/usr/local/bin/python3
####################################################
#
# Uebung UT1_Liste_mit_Zufallszahlen
# Schreiben Sie ein Programm, das fünfzig Zufallszahlen von
# 0 bis 9999 in einer zufälliger Reihenfolge aus gibt.
# Jede Zahl darf in der Liste am Schluss nur einmal vorkommen.
#
####################################################

import random

# Variabeln
zahlen = set()

# Liste erzeugen
while len(zahlen) < 50:
    zahl = random.randint(0, 9999)
    zahlen.add(zahl)

# Liste ausgeben
for i in zahlen:
    print(i)
