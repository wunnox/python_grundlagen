#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
##############################################
#
# Name: OO_Beispiel.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Beispiel eines Object Oriented Python Scripts
#
##############################################

# Variablen
auto = {}

# Classes


class Auto:
    def __init__(self, marke):
        self.marke = marke
        self.sitze = 0
        self.speed = 0

# Functions


def ErsteAuswahl():
    print("Treffen sie Eine Auswahl:")
    print("Neues Fahrzeug erfassen:     n")
    print("Fahrtzeit berechnen:         f")
    print("Ende:                        e")
    q = raw_input('-> ')
    return q


# Basis Fahrzeuge erfassen
auto['Opel'] = Auto('Opel')
auto['Opel'].speed = 150
auto['Opel'].sitze = 4
auto['VW Bus'] = Auto('VW Bus')
auto['VW Bus'].speed = 130
auto['VW Bus'].sitze = 8
auto['Topolino'] = Auto('Topolino')
auto['Topolino'].speed = 80
auto['Topolino'].sitze = 4

# Text
print("#######################################################################################################")
print("Hier können Sie Fahrzeiten mit verschiedenen Fahrzeugen und einer bestimmten Anzahl Personen berechnen")
print("Verwendung:")
print("  - Mit n können neue Fahrzeuge erfasst werden")
print("  - Mit f kann die Fahrzeit für eine bestimmte Distanz angezeigt werden. ")
print("    Die Fahrzeuge werden je nach Personenzahl vorgeschlagen")
print("#######################################################################################################")
print()

# Berechnung erstellen
a = {}
while True:
    q1 = ErsteAuswahl()
    if q1 == 'n':
        m = raw_input('Marke: ')
        s = raw_input('Speed: ')
        p = raw_input('Sitze: ')
        auto[m] = Auto(m)
        auto[m].speed = int(s)
        auto[m].sitze = int(p)
    elif q1 == 'f':
        ap = eval(raw_input('Anzahl Personen: '))
        distanz = eval(raw_input('Distanz in Kilometer: '))
        print("Verfügbare Fahrzeuge:")
        for i in list(auto.keys()):
            if auto[i].sitze >= ap:
                print(i, "->", i[0])
                auswahl = i[0]
                a[auswahl] = i

        m = raw_input('Ihre Auswahl: ')
        if m in list(a.keys()):
            wahl = a[m]
            print()
            print(
                "Die Fahrt mit dem",
                auto[wahl].marke,
                "dauert für die",
                distanz,
                "Kilometer",
                60 *
                distanz /
                auto[wahl].speed,
                "Minuten")
            print()
            print()
        else:
            print("Fahrzeug gibt es nicht")
    else:
        quit()
