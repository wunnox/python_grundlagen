#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Name: UB7.4_distanzen.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 12.01.2016
#
# Purpose: Liest Adressen ein ung gibt deren
#          Geo-Positionen aus und berechnet
#          die Distanz zwischen den beiden.
#
##############################################

from geopy.geocoders import Nominatim
from geopy.distance import vincenty

# Variabeln
geolocator = Nominatim()

# Adresse bestimmen
digizh = geolocator.geocode("Limmatstrasse 50, 8005 Zürich")
digibe = geolocator.geocode("Bubenbergplatz 11, 3011 Bern")

# Längen und Breitengrade auslesen
digizhkoord = (digizh.latitude, digizh.longitude)
digibekoord = (digibe.latitude, digibe.longitude)

# Distanz berechnen
distanz = vincenty(digizhkoord, digibekoord).km

# Angaben ausgeben
print "Standort Zürich Koordinaten: ", digizhkoord
print "Standort Bern Koordinaten  : ", digibekoord
print "Distanz dazwischen         : ", distanz, "km"
