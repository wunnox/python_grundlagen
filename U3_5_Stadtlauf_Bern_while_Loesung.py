####################################################
#
# Musterlösung: Stadtlauf Bern mit while-Schleife und Turtle
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur

while run:
    if d > 0:

        # Lauf zum Zytglogge-Turm
        for i in range(440):
            time.sleep(slower)
            x = go_right()
            if x % 10 == 0 and x <= 210:
                y = go_up()
            elif x % 10 == 0 and x < 450:
                y = go_down()
            redrawGameWindow()

        ####################################################
        # Lösung: Lauf zur Gerechtigkeitsgasse
        while x < 670:
            time.sleep(slower)
            x = go_right()
            redrawGameWindow()
        ####################################################

        d -= 1
        go_stop()
        redrawGameWindow()

    # Nach dem automatischen Lauf kann Marsi manuell bewegt werden.
    # Die Taste q beendet die while-Schleife.
    run = check_key()
    redrawGameWindow()

screen.bye()
