#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung:
# Erstellen Sie ein Modul, welches die Berechnungen
# der Distanzen nach Chur via Zürich beinhaltet.
#
####################################################

#### Lösung: ####

# Inhalt Datei U56_modul_Distanz.py:
#####################################
# def Distanzen(bern=125,basel=85,luzern=51):
#   chur=119
#   bern=bern+chur
#   basel=basel+chur
#   luzern=luzern+chur
#   return bern,basel,luzern
#####################################

import U56_modul_Distanz as dis

bern, basel, luzern = dis.Distanzen(135, 92)
print("Distanzen nach Chur via Zürich:")
print("Bern;", bern, "Basel:", basel, "Luzern:", luzern)
