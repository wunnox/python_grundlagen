#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches Ihr Alter
# (oder sonst eines) berechnet.
#
####################################################

#### Lösung: ####
import time

dztupel = (1965, 6, 20, 0, 0, 0, 0, 0, 0)
ltgeburt = time.localtime(time.mktime(dztupel))
ltheute = time.localtime()  # Aktuell
alter = ltheute[0] - ltgeburt[0]
print("Ich bin", alter, "Jahre alt")
