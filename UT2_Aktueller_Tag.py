#!/usr/local/bin/python3
####################################################
#
# Uebung UT2.3_Aktueller_Tag:
# Schreiben Sie ein Programm, welches ihnen den aktuellen
# Wochentag und das aktuelle Datum im Format:
# TT. Monatsname JJJJ ausgeben.
#
####################################################

import time

# Datum/Zeit einlesen
lt = time.localtime()
jahr, monat, tag, stunde, minute, sekunde, wtagnr = lt[0:7]

# Wochentage und Monate erfassen
wtage = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag"]
monate = [
    "Januar",
    "Februar",
    "März",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "Oktober",
    "November",
    "Dezember"]

# Werte ausgeben
datum = str(tag) + ". " + monate[monat] + " " + str(jahr)
print("Heute ist", wtage[wtagnr], "der", datum)
