#!/usr/bin/python3
##############################################
#
# Name: UB7_3_planeten.py
#
# Author: Peter Christen / Digicomp
#
# Version: 1.0
#
# Date: 12.01.2016
#
# Purpose: Gibt Positionen von Planeten aus
# Hinweis: Das Azimut ist die Abweichung von
#          Norden nach Osten in Grad.
#          die Höhe ist der Winkel von einer
#          gedachten Ebene aus (90° ist senkrecht)
#
##############################################

import ephem as ep

gatech = ep.Observer()
gatech.lon, gatech.lat = '7.4393795', '46.9472123'

# Sonne und Mond berechnen
sunbe,moonbe = ep.Sun(), ep.Moon()
sunbe.compute(gatech)
moonbe.compute(gatech)

# Planete berechnen
marsbe,venusbe = ep.Mars(), ep.Venus()
marsbe.compute(gatech)
venusbe.compute(gatech)

# Positionen ausgeben
print("Bern  : Azimut         Höhe")
print(f"Sonne : {sunbe.az}   {sunbe.alt}")
print(f"Mond  : {moonbe.az}   {moonbe.alt}")
print(f"Mars  : {marsbe.az}   {marsbe.alt}")
print(f"Venus : {venusbe.az}   {venusbe.alt}")
print()
print("Sonnenaufgang   (UTC):", gatech.next_rising(sunbe))
print("Sonnenuntergang (UTC):", gatech.next_setting(sunbe))
print("Mondaufgang     (UTC):", gatech.next_rising(moonbe))
print("Monduntergang   (UTC):", gatech.next_setting(moonbe))
print()
