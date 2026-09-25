####################################################
# Übung: Stadtlauf Bern – input() mit Turtle
#
# Fügen Sie im markierten Bereich Code ein:
#
# - Lesen Sie mit input() die Anzahl Schritte ein, welche Marsi
#   laufen soll.
# - Verwenden Sie dazu die Variable schritte.
# - Bei weniger als 10 Schritten wird der Wert auf 10 gesetzt.
# - Bei mehr als 450 Schritten wird der Wert auf 450 gesetzt.
# - Sobald Marsi beim Zytglogge ankommt, endet der automatische Lauf.
#
# Taste q: Spiel beenden.
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
schritte = 0
d = 2
slower = 0.01

# Start der Darstellung
while run:

    # Lauf zum Zytglogge-Turm
    for i in range(schritte):
        time.sleep(slower)
        x = go_right()

        if x % 10 == 0 and x <= 210:
            y = go_up()
        elif x % 10 == 0 and x < 450:
            y = go_down()

        redrawGameWindow()

        if x > 450:
            go_stop()
            redrawGameWindow("Weiter geht's nicht mehr", x, y - 10)
            time.sleep(2)
            break

    go_stop()
    redrawGameWindow()

    ####################################################
    # Hier kommt Ihr Code
    # Erfassen Sie einen Wert für die Variable "schritte".


    # bis hier
    ####################################################

    # Nach der Eingabe kann Marsi mit Pfeiltasten bewegt werden.
    run = check_key()
    redrawGameWindow()

screen.bye()
