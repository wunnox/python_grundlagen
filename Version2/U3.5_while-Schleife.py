#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
###################################################################
#
# Uebung:
# Erstellen Sie eine Endlosschlaufe in welcher Sie eine Variable
# hoch zählen und aktuellen Wert auf dem Bildschirm ausgeben.
# Brechen Sie die Schlaufe nach zehn Durchgängen ab.
#
###################################################################

#### Lösung: ####

c = 0
while True:
    c += 1
    print(c)
    if c == 10:
        break
