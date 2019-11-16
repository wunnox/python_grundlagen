#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung:
# Erstellen Sie eine Funktion, welche die Distanzen nach Chur via Zürich von den Städten
# Bern, Basel und Luzern berechnet, je nach dem welcher Weg nach Zürich gewählt wird.
# D.h. es gibt je eine Standard-Strecken nach Zürich, aber es können auch längere gewählt werden.
# Die Distanz von Zürich nach Chur ist fix 119km
# Die Standard Strecken sind: Bern: 125km, Basel: 85km, Luzern: 51km
# Für die Übung wählen Sie folgende variablen Distanzen Bern: 145km, Luzern 60km
# Sie sollten ein Resultat analog zu diesem kriegen:
# Bern: 264 Basel: 204 Luzern: 179
#
####################################################

#### Lösung: ####

def Distanzen(bern=125, basel=85, luzern=51):
    chur = 119
    bern = bern + chur
    basel = basel + chur
    luzern = luzern + chur
    return bern, basel, luzern

bern, basel, luzern = Distanzen(145, luzern=60)

print("Distanzen nach Chur via Zürich:")
print("Bern:", bern, "Basel:", basel, "Luzern:", luzern)
