#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung UT2_Morsen.py:
# Erstellen Sie ein Programm, welches anhand einer
# Morsetabelle einen Text in Morsecode ausgibt.
# Verwenden Sie hierzu das Modul UT2_Morsecodes.py
#
####################################################

import UT2_Morsecodes as mc

w = raw_input('-> ')  # Wort einlesen
w = w.replace(' ', '_')
for l in w:
    print(mc.morse(l), end=' ')

print()
