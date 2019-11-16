#!/usr/local/bin/python3
##############################################
#
# Name: UB7.3_planeten.py
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

# Standort aus Liste wählen
zurich = ep.city("Zurich")
zurich.date = ep.now()

# Standort selber definieren
bern = ep.Observer()
bern.lon = ep.degrees("7.4393795")
bern.lat = ep.degrees("46.9472123")
bern.elevation = 550
bern.date = ep.now()
bern.pressure = 0  # Let's neglect atmospheric refraction

# Sonne und Mond berechnen
sunbe = ep.Sun(bern)
moonbe = ep.Moon(bern)
sunzh = ep.Sun(zurich)
moonzh = ep.Moon(zurich)

# Planete berechnen
marsbe = ep.Mars(bern)
venusbe = ep.Venus(bern)
marszh = ep.Mars(zurich)
venuszh = ep.Venus(zurich)

# Positionen ausgeben
print("Bern  : Azimut,     Höhe")
print("Sonne :", sunbe.az, sunbe.alt)
print("Mond  :", moonbe.az, moonbe.alt)
print("Mars  :", marsbe.az, marsbe.alt)
print("Venus :", venusbe.az, venusbe.alt)
print()
print("Sonnenaufgang  :", ep.localtime(sunbe.rise_time))
print("Sonnenuntergang:", ep.localtime(sunbe.set_time))
print("Mondaufgang    :", ep.localtime(moonbe.rise_time))
print("Monduntergang  :", ep.localtime(moonbe.set_time))
print()
print("Zürich: Azimut,     Höhe")
print("Sonne :", sunzh.az, sunzh.alt)
print("Mond  :", moonzh.az, moonzh.alt)
print("Mars  :", marszh.az, marszh.alt)
print("Venus :", venuszh.az, venuszh.alt)
print()
print("Sonnenaufgang  :", ep.localtime(sunzh.rise_time))
print("Sonnenuntergang:", ep.localtime(sunzh.set_time))
print("Mondaufgang    :", ep.localtime(moonzh.rise_time))
print("Monduntergang  :", ep.localtime(moonzh.set_time))
print()
