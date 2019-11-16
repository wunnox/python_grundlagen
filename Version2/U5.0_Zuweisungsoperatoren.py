#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung:
# Setzen Sie zwei Variablen wie folgt:
# a=4
# n='Anna'
# Erzeugen Sie mit Hilfe von Zuweisungsoperatoren folgende Ausgabe:
# Anna16
#
####################################################

#### Lösung: ####

a = 4
n = 'Anna'
a **= 2
n += str(a)
print(n)
