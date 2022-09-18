#!/usr/bin/python3
###################################################################
#
# Uebung:
# Generieren Sie eine Zufallszahl zwischen 10 und 100 (inklusive), 
# schreiben Sie diese in die Variable „z“
# Addieren Sie 5 zur Variable „z“ hinzu und multiplizieren sie den Wert mit 2
# Geben Sie nun das Resultat einmal mit einer ganzzahligen und einmal 
# mit einer Modulo Division auf dem Bildschirm aus
#
###################################################################

#### Lösung: ####

# Modul random importieren
import random

# Zufallswerte und Berechnung
z = random.randint(100, 1000)

# Zufallswerte und Berechnung
z=(z+5)*2

# Ausgabe
print(f"Resultat ganzzahlig: {z//3}, modulo: {z%3}")
