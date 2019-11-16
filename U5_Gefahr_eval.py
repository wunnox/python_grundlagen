#!/usr/local/bin/python3
###################################################################
#
# Beispiel Gefahr von eval und exec:
# Starten Sie dieses Script und geben Sie an Stelle einer Zahl
# folgenden Code ein: os.system('rm U5_Gefahr_eval.py')
#
# Was wäre bei der Eingabe: os.system('rm -R *') passiert?
# Achtung nicht testen ohne vorherige Datensicherung!!!!
#
###################################################################

import os

# Eingabe einer Zahl
print("Bitte eine Zahl eingeben")
x = eval(input("-> "))

# Auswertung
if x > 50:
    print("Die Zahl", x, "ist grösser als 50")
else:
    print("Die Zahl", x, "ist nicht grösser als 50")
