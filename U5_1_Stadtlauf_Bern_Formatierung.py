####################################################
# Übung: Stadtlauf Bern – formatierte Ausgabe mit Turtle
#
# Marsi läuft anhand der gespeicherten Wegdaten zum Zytglogge.
# Zählen Sie die Schritte
# - von der Heiliggeistkirche bis zum Käfigturm und
# - vom Käfigturm bis zum Zytglogge.
#
# Geben Sie die Resultate formatiert im Terminal aus, zum Beispiel:
#
# Distanz von          Bis          Anzahl Schritte
# Heiliggeist Kirche   Käfigturm              200 Schritte
# Käfigturm            Zytglogge             230 Schritte
#
# Hinweis: Neuer Code nur im markierten Bereich.
####################################################

import time
from stadtlauf_bern_modul import *

# Wegdaten zum Zytglogge als Tupel mit (x, y)-Paaren.
zytglogge = tuple(
    (pos_x, 155 - min((pos_x - 20) // 10, 19) + max((pos_x - 210) // 10, 0))
    for pos_x in range(21, 471)
)

# Variablen
d = 1
slower = 0.01
schritte = 0

pos = {
    "Käfigturm": (200, 280, 120, 150),
    "Zytglogge": (410, 490, 140, 160),
}


def check_text(x, y):
    """Prüft mithilfe von pos, ob eine Sehenswürdigkeit nahe ist."""
    text2show, xt, yt = "", x, y
    for name, (x_min, x_max, y_min, y_max) in pos.items():
        if x_min < x < x_max and y_min < y < y_max:
            text2show, xt, yt = name, x, y
    return text2show, xt, yt


text2show = ""
xt, yt = x, y

while run:
    if d > 0:
        for gx, gy in zytglogge:
            time.sleep(slower)
            x, y = go_walk_right(gx, gy)

            text2show, xt, yt = check_text(x, y)
            redrawGameWindow(text2show, xt, yt - 15)

            ####################################################
            # Hier kommt Ihr Code
            # Schritte zählen und formatiert ausgeben.


            # bis hier
            ####################################################

        d -= 1
        go_stop()
        redrawGameWindow(text2show, xt, yt - 15)

    run = check_key()
    text2show, xt, yt = check_text(x, y)
    redrawGameWindow(text2show, xt, yt - 15)

screen.bye()
