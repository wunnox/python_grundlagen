###################################################################
#
# Beispiel Gefahr von eval und exec:
# Finden Sie mit der KI heraus, welche Gefahren dieses Script beinhaltet. 
#
###################################################################

# KI-Prompt
# Analysiere nachfolgendes Python Script und beurteile welche Gefahren es bergen könnte:

import os

# Eingabe einer Zahl
print("Bitte eine Zahl eingeben")
x = eval(input("-> "))

# Auswertung
if x > 50:
    print("Die Zahl", x, "ist grösser als 50")
else:
    print("Die Zahl", x, "ist nicht grösser als 50")
