#!/usr/local/bin/python3
##############################################
#
# Name: UT3_EuroMillion.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 12.01.2016
#
# Purpose: Erstellt aus dem File UT3_EuroMillion.txt
#          eine Liste mit der häufigste Lottozahl und
#          dem häufigsten Stern in den Ziehungen von 2015
#
##############################################

# Variabeln
file = 'UT3_EuroMillion.txt'
zahlen = []
sterne = []
maxZahl = 0
AnzahlZahl = 0
maxStern = 0
AnzahlStern = 0

# Daten aus File einlesen
f = open(file, 'r')
for line in f:
    allezahlen = line.strip().split(";")
    # Zahlen auflisten
    for i in allezahlen[:-2]:
        zahlen.append(i)
    # Sterne auflisten
    for i in allezahlen[-2:]:
        sterne.append(i)
f.close()

# Daten auswerten
for i in zahlen:
    if zahlen.count(i) > AnzahlZahl:
        maxZahl = i
        AnzahlZahl = zahlen.count(i)

print("\nHäufigste Zahl ist die", maxZahl, "mit", AnzahlZahl, "Treffern")

for i in sterne:
    if sterne.count(i) > AnzahlStern:
        maxStern = i
        AnzahlStern = sterne.count(i)

print("\nHäufigster Stern ist die", maxStern, "mit", AnzahlStern, "Treffern")
