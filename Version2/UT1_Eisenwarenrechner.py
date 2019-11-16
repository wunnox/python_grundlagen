#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung UT1_Eisenwarenrechner
# Schreiben Sie ein Programm, welches die Kosten für
# einen Einkauf von Schrauben, Muttern und Unterlagscheiben
# berechnet. Definieren Sie die Preise selber.
#
####################################################

# Variabeln
schraubenpreis = 0.20
mutternpreis = 0.10
unterlagscheibenpreis = 0.05

# Eingabe der Mengen
print("Geben Sie ein von welchen Teilen Sie wieviele brauchen:")
anzahlschrauben = input("Anzahl Schrauben: ")
anzahlmuttern = input("Anzahl Muttern: ")
anzahlunterlagscheiben = input("Anzahl Unterlegscheiben: ")

# Berechnung des Preises
preis = anzahlschrauben * schraubenpreis + anzahlmuttern * \
    mutternpreis + anzahlunterlagscheiben * unterlagscheibenpreis
print("Gesamtpreis: ", preis, "Franken")
