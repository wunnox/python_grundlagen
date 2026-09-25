####################################################
#
# Musterlösung: Stadtlauf Bern mit for-Schleife und Turtle
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur

# Start der Darstellung
while run:
    if d > 0:

        # Lauf zum Käfigturm
        for i in range(210):
            time.sleep(slower)
            x = go_right()
            if x % 10 == 0:
                y = go_up()

            redrawGameWindow()

        ####################################################
        # Lösung: Lauf zum Zytglogge
        for i in range(230):
            time.sleep(slower)
            x = go_right()
            if x % 10 == 0:
                y = go_down()

            redrawGameWindow()
        ####################################################

        d -= 1
        go_stop()
        redrawGameWindow()

    # Nach dem automatischen Lauf: manuelle Steuerung.
    # Die Funktion wartet auf ein Tastaturereignis und liefert False bei q.
    run = check_key()
    redrawGameWindow()

screen.bye()
