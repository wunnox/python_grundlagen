####################################################
# Übung: Stadtlauf Bern – Parameter mit Turtle
#
# Geben Sie beim Starten des Skripts ein Ziel als Parameter an.
# Marsi soll dann zu diesem Ziel laufen.
#
# Prüfen Sie:
# - Wurde ein Parameter eingegeben?
# - Ist das Ziel gültig?
#
# Ohne Ziel soll die Meldung erscheinen:
# "Es wurde kein Ziel eingegeben!"
# Anschliessend soll das Programm mit sys.exit() beendet werden.
#
# Gültige Ziele:
# Käfigturm, Zytglogge, Bundeshaus, Münster, Kasino,
# Rathaus, Nydeck Kirche
#
# Beispiel:
# python U5_5_Stadtlauf_Bern_Parameter.py Zytglogge
####################################################

import sys
import time

####################################################
# Hier kommt Ihr Code
# Parameter prüfen und das Ziel in der Variable ziel speichern.


# bis hier
####################################################

# Diese Module werden erst geladen, wenn ein gültiges Ziel feststeht.
from stadtlauf_bern_modul import *
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd

# Variablen
d = 1
slower = 0.01

pos = {
    "Käfigturm": (200, 280, 120, 150),
    "Zytglogge": (410, 490, 140, 160),
    "Bundeshaus": (190, 240, 180, 250),
    "Münster": (570, 725, 200, 250),
    "Kasino": (440, 540, 230, 270),
    "Rathaus": (660, 750, 60, 110),
    "Nydeck Kirche": (870, 950, 60, 100),
}


def check_text(x, y):
    """Prüft, ob Marsi sich im Bereich einer Sehenswürdigkeit befindet."""
    text2show, xt, yt = "", x, y
    for name, (x_min, x_max, y_min, y_max) in pos.items():
        if x_min < x < x_max and y_min < y < y_max:
            text2show, xt, yt = name, x, y
    return text2show, xt, yt


text2show = ""
xt, yt = x, y

while run:
    if d > 0:
        for gx, gy in wd.weg[ziel]:
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
