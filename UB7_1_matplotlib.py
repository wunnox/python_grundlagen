#!/usr/bin/python3
# -*- coding: utf-8 -*-
##############################################
#
# Name: UB7_1_matplotlib.py
#
# Author: Peter Christen / Digicomp
#
# Version: 1.0
#
# Date: 12.01.2016
#
# Purpose: Zeichnet eine Kurvengrafik mit matplotlib
#
##############################################

import matplotlib.pyplot as plt

# Variabeln
li = [184,186,185,196,425,438,519,583,620,585,284,152,286,552,548,543,540,306,462,530,532,515,487,421,390,192,187,194,207]

# Grafik erstellen
plt.plot(li)
plt.title('Ausschlag')
plt.ylabel('Messwerte')
plt.xlabel('Zeit')

# Grafik ausgeben
plt.show()
