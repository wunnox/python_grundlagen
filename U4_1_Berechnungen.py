###################################################################
#
# Uebung:
# Geben Sie eine Sinuswelle über 20 Zeilen 
# und einer Amplitude von 20 Charakter aus
#
###################################################################

#### Lösung: ####

# KI-Prompt
# Erstelle ein Python Script, welches eine einzelne Sinuswelle mit einer 
# Amplitude von 20 Charakter und einer Länge von 20 Zeilen auf dem Terminal ausgibt. 
# Als Zeichen soll ein grosses X verwendet werden.

import math

amplitude = 20
laenge = 20  # Anzahl der Zeilen (Wellenpunkte)

for x in range(laenge):
    y = math.sin(x * (2 * math.pi / laenge))  # Eine komplette Sinuswelle auf 20 Zeilen
    zeile = int(round(amplitude * y)) + amplitude
    print(" " * zeile + "X")
