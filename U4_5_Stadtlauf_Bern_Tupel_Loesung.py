####################################################
#
# Musterlösung: Stadtlauf Bern – Tupel mit Turtle
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur

# Wegdaten zum Zytglogge als unveränderbares Tupel.
zytglogge = tuple(
    (pos_x, 155 - min((pos_x - 20) // 10, 19) + max((pos_x - 210) // 10, 0))
    for pos_x in range(21, 471)
)


def check_text(x, y):
    """Prüft, ob eine Sehenswürdigkeit angezeigt werden soll."""
    if 200 < x < 280 and 120 < y < 150:
        text2show = "Käfigturm"
        xt, yt = x, y
    elif 410 < x < 490 and 140 < y < 160:
        text2show = "Zytglogge"
        xt, yt = x, y
    else:
        text2show, xt, yt = "", x, y
    return text2show, xt, yt


text2show = ""
xt, yt = x, y

while run:
    if d > 0:

        # Jedes Element wg ist ein Tupel mit zwei Werten: (gx, gy).
        for wg in zytglogge:
            gx, gy = wg
            time.sleep(slower)
            x, y = go_walk_right(gx, gy)

            text2show, xt, yt = check_text(x, y)
            redrawGameWindow(text2show, xt, yt - 15)

        d -= 1
        go_stop()
        redrawGameWindow(text2show, xt, yt - 15)

    run = check_key()
    text2show, xt, yt = check_text(x, y)
    redrawGameWindow(text2show, xt, yt - 15)

screen.bye()
