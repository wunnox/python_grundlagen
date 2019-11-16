#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung:
# In folgendem Code gibt es einen Fehler.
# Prüfen Sie mal auf Zahlen über 50
# Verwenden Sie das Debugging Modul für die Analyse
#
# # Eingabe einer Rechnung
# x = input("Geben Sie eine Rechnung ein (Bsp. 10+20). Das Resultat muss von 1 - 50 sein: ")
# a=eval(str(x))
#
# #Auswertung
# if a>0 or a<50:
#      print "Richtig!"
# else:
#      print "Falsch, das Ergebnis ist nicht zw. 1 und 50"
#
####################################################

#### Lösung: ####
import pdb

# Eingabe einer Zahl
x = raw_input(
    "Geben Sie eine Rechnung ein (Bsp. 10+20). Das Resultat muss von 1 - 50 sein: ")

a = eval(str(x))
# pdb.set_trace()

# Auswertung
if a > 0 or a < 50:
    print("Richtig!")
else:
    print("Falsch, das Ergebnis ist nicht zw. 1 und 50")
