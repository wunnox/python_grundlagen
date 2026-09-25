####################################################
#
# Übung: Stadtlauf Bern – Tupel mit Turtle
#
# Im untenstehenden Tupel "zytglogge" ist die Wegstrecke
# zum Zytglogge hinterlegt.
#
# Lesen Sie das Tupel ein und lassen Sie Marsi mit diesen Daten
# den Weg ablaufen. Verwenden Sie dazu:
#
#     x, y = go_walk_right(x, y)
#
# Die Texte zu den Sehenswürdigkeiten sollen weiterhin erscheinen.
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur

# Wegdaten zum Zytglogge.
# Die Erzeugung mit range() ergibt dasselbe Prinzip wie ein langes Tupel
# aus einzelnen (x, y)-Koordinaten: ein unveränderbares Tupel.
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

        ####################################################
        # Hier kommt Ihr Code
        # Die Wegdaten aus dem Tupel nacheinander ablaufen.


        # bis hier
        ####################################################

        d -= 1
        go_stop()
        redrawGameWindow(text2show, xt, yt - 15)

    run = check_key()
    text2show, xt, yt = check_text(x, y)
    redrawGameWindow(text2show, xt, yt - 15)

screen.bye()
