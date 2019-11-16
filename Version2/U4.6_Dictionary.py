#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung:
# Erstellen Sie folgendes Tupel:
# a=('Peter','Hans','Fred','Hans','Ursula','Robert','Ursula','Hans')
#
# Listen Sie jeden Namen in obigem Tupel nur einmal auf gefolgt von einer Zahl,
# die angibt, wie oft dieser Name im Tupel vorkommt. Dazu benötigen Sie folgende
# Elemente ein Dictionary, zwei for-Schlaufen und eine if/else-Bedingung.
#
# Geben Sie das Resultat auf dem Bildschirm aus
#
####################################################

#### Lösung: ####

a = ('Peter', 'Hans', 'Fred', 'Hans', 'Ursula', 'Robert', 'Ursula', 'Hans')
d = {}

for n in a:
    if n in d.keys():
        d[n] += 1
    else:
        d[n] = 1

for n, a in d.items():
    print(n, a)
