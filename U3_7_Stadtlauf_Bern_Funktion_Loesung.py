####################################################
#
# Musterlösung: Stadtlauf Bern – Funktionen mit Turtle
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur
text2show = ""
xt, yt = x, y

####################################################
# Lösung: Prüfung in eine eigene Funktion auslagern

def check_text(x, y):
    """Liefert Text und Position einer Sehenswürdigkeit zurück."""
    if 200 < x < 280 and 120 < y < 150:
        text2show = "Käfigturm"
        xt, yt = x, y
    elif 410 < x < 490 and 140 < y < 160:
        text2show = "Zytglogge"
        xt, yt = x, y
    else:
        text2show, xt, yt = "", x, y

    return text2show, xt, yt

####################################################

while run:
    if d > 0:

        # Lauf zum Zytglogge-Turm
        for i in range(450):
            time.sleep(slower)
            x = go_right()
            if x % 10 == 0 and x <= 210:
                y = go_up()
            elif x % 10 == 0 and x < 450:
                y = go_down()

            text2show, xt, yt = check_text(x, y)
            redrawGameWindow(text2show, xt, yt - 15)

        d -= 1
        go_stop()
        redrawGameWindow(text2show, xt, yt - 15)

    # Nach dem automatischen Lauf kann Marsi manuell bewegt werden.
    # Die Taste q beendet die while-Schleife.
    run = check_key()
    text2show, xt, yt = check_text(x, y)
    redrawGameWindow(text2show, xt, yt - 15)

screen.bye()
