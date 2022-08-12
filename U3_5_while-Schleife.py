#!/usr/bin/python3
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
