#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches zählt, wieviele
# Parameter Sie auf der Kommandozeile angegeben haben.
#
####################################################

#### Lösung: ####
import sys

l = len(sys.argv)

if l == 1:
    print("Es wurden keine Parameter angegeben")
else:
    print("Es wurden", l - 1, "Parameter angegeben")
