#!/usr/bin/python3
##############################################
#
# Name: U6_4_Auto.py
#
# Author: Peter Christen
#
# Version: 1.1
#
# Date: 20.11.2015 V1.0
#       25.03.2024 V1.1 Übung überarbeitet
#
# Purpose: Beispiel eines Object Oriented Python Scripts mit Operatoren
#
# Vorlage: Übung 6.7 oop_operator.py aus Buch "Einstig in Python"
#
##############################################

# Klassen
class Auto:
    '''Klasse zum Verwalten von Fahrzeugen'''

    def __init__(self, marke,speed):
        self.marke = marke
        self.speed = speed

    def __gt__(self, other):
        return self.speed > other.speed

    def __eq__(self, other):
        return self.speed == other.speed

auto1=input("Fahrzeugname 1: ")
speed1=input("Speed 1: ")
auto2=input("Fahrzeugname 2: ")
speed2=input("Speed 2: ")

objekt1 = Auto(auto1,speed1)
objekt2 = Auto(auto2,speed2)

print()
if objekt1 == objekt2:
    print(f"Der {objekt1.marke} und der {objekt2.marke} sind gleich schnell ({int(objekt1.speed)} km/h)")
elif objekt1 > objekt2:
    print(f"Der {objekt1.marke} ist {int(objekt1.speed)-int(objekt2.speed)} km/h schneller als der {objekt2.marke}")
else:
    print(f"Der {objekt2.marke} ist {int(objekt2.speed)-int(objekt1.speed)} km/h schneller als der {objekt1.marke}")
