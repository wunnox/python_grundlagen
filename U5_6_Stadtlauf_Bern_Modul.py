####################################################
# Übung: Stadtlauf Bern – eigenes Modul mit Turtle
#
# Verlegen Sie die Funktion check_text() in eine eigene Datei.
# Importieren Sie die Funktion anschliessend als Modul.
#
# Benennen Sie die neue Datei:
# U5_6_stadtlauf_Bern_check_text.py
#
# Verschieben Sie das Dictionary pos und die Funktion check_text()
# aus diesem Skript in die neue Datei. Importieren Sie danach nur
# noch die Funktion check_text.
####################################################

import time
from stadtlauf_bern_modul import *
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd

####################################################
# Hier kommt Ihr neuer Code
# Beispiel:
# from U5_6_stadtlauf_Bern_check_text import check_text


# bis hier
####################################################

# Code zum Verschieben/Löschen:
# Das Dictionary pos und die Funktion check_text() müssen in die Datei
# U5_6_stadtlauf_Bern_check_text.py verschoben werden.
pos = {
    "Käfigturm": (200, 280, 120, 150),
    "Zytglogge": (410, 490, 140, 160),
    "Bundeshaus": (190, 240, 180, 210),
    "Münster": (570, 725, 200, 250),
    "Kasino": (440, 540, 230, 270),
    "Rathaus": (660, 750, 60, 110),
    "Nydeck Kirche": (870, 950, 60, 100),
}


def check_text(x, y):
    """Prüft, ob ein Text angezeigt werden soll."""
    text2show, xt, yt = "", x, y
    for name, (x_min, x_max, y_min, y_max) in pos.items():
        if x_min < x < x_max and y_min < y < y_max:
            text2show, xt, yt = name, x, y
    return text2show, xt, yt


# Variablen
d = 1
slower = 0.01
text2show = ""
xt, yt = x, y

while run:
    if d > 0:
        for gx, gy in wd.weg["Zytglogge"]:
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
