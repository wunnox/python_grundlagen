#!/usr/bin/python3
##############################################
#
# Name: U6_OO_Beispiel.py
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
    '''Klasse zum Erfassen und Verwalten von Fahrzeugen'''

    def __init__(self, marke):
        self.marke = marke
        self.sitze = 0
        self.speed = 0

# Functions
def ErsteAuswahl():
    '''Erste Auswahl zum Fahrzeug erfassen oder Fahrzeit berechnen'''

    print("Treffen sie Eine Auswahl:")
    print("Neues Fahrzeug erfassen:     n")
    print("Fahrtzeit berechnen:         f")
    print("Ende:                        e")
    q = input('-> ')
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
        m = input('Marke: ')
        s = input('Speed: ')
        p = input('Sitze: ')
        auto[m] = Auto(m)
        auto[m].speed = int(s)
        auto[m].sitze = int(p)
    elif q1 == 'f':
        ap = eval(input('Anzahl Personen: '))
        distanz = eval(input('Distanz in Kilometer: '))
        print("Verfügbare Fahrzeuge:")
        for i in list(auto.keys()):
            if auto[i].sitze >= ap:
                print(i, "->", i[0])
                auswahl = i[0]
                a[auswahl] = i

        m = input('Ihre Auswahl: ')
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
