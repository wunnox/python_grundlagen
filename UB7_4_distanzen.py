#!/usr/bin/python3
##############################################
#
# Name: UB7_4_distanzen.py
#
# Author: Peter Christen
#
# Version: 1.1
#
# Date: 08.09.2020
#
# Purpose: Liest Adressen ein ung gibt deren
#          Geo-Positionen aus und berechnet
#          die Distanz zwischen den beiden.
#
##############################################

from geopy.geocoders import Nominatim
from geopy import distance

#from geopy.distance import vincenty

# Variabeln
geolocator = Nominatim(user_agent="geoapiExercises")


# Adresse bestimmen
digizh = geolocator.geocode("Limmatstrasse 50, 8005 Zürich")
digibe = geolocator.geocode("Bubenbergplatz 11, 3011 Bern")

# Längen und Breitengrade auslesen
digizhkoord = (digizh.latitude, digizh.longitude)
digibekoord = (digibe.latitude, digibe.longitude)

# Distanz berechnen
distanz = distance.distance(digizhkoord, digibekoord).km

# Angaben ausgeben
print("Standort Zürich Koordinaten: ", digizhkoord)
print("Standort Bern Koordinaten  : ", digibekoord)
print("Distanz dazwischen         : ", distanz, "km")
