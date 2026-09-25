####################################################
# Übung: Stadtlauf Bern – Dictionary mit Turtle
#
# Marsi läuft anhand gespeicherter Wegdaten zum Zytglogge.
# Ändern Sie check_text() so, dass die Prüfung der
# Sehenswürdigkeiten über das Dictionary pos erfolgt.
#
# In pos enthält jeder Schlüssel den Namen einer Sehenswürdigkeit.
# Der Wert ist ein Tupel mit den Grenzen:
# (x_min, x_max, y_min, y_max)
#
# Hinweis: Passen Sie nur den markierten Bereich an.
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01

# Wegdaten zum Zytglogge als Tupel mit (x, y)-Paaren.
zytglogge = tuple(
    (pos_x, 155 - min((pos_x - 20) // 10, 19) + max((pos_x - 210) // 10, 0))
    for pos_x in range(21, 471)
)

# Dictionary mit Positionsdaten für Sehenswürdigkeiten.
pos = {
    "Käfigturm": (200, 280, 120, 150),
    "Zytglogge": (410, 490, 140, 160),
}

####################################################
# Hier kommt Ihre Code-Anpassung

def check_text(x, y):
    """Prüft mithilfe von pos, ob eine Sehenswürdigkeit nahe ist."""

    # Ergänzen Sie hier den Code.
    pass

# bis hier
####################################################

text2show = ""
xt, yt = x, y

while run:
    if d > 0:
        for gx, gy in zytglogge:
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
