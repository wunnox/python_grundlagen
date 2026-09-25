####################################################
# Musterlösung: Stadtlauf Bern – eigenes Modul mit Turtle
####################################################

import time
from stadtlauf_bern_modul import *
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd
from U5_6_stadtlauf_Bern_check_text import check_text

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
