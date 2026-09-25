####################################################
# Musterlösung: Stadtlauf Bern – objektorientiert mit Turtle
####################################################

import time
import stadtlauf_bern_oo_modul as sf
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd
from U5_6_stadtlauf_Bern_check_text import check_text

run = True
d = 1
slower = 0.01

# 1. Ein Objekt der Klasse Figur erstellen.
marsi = sf.Figur("Marsi")

text2show = ""
xt = 0
yt = 0
x, y = marsi.x, marsi.y

while run:
    if d > 0:
        for gx, gy in wd.weg["Zytglogge"]:
            time.sleep(slower)

            # 2. Das Objekt entlang der vorgegebenen Wegdaten bewegen.
            x, y, left, right = marsi.go_walk_right(gx, gy)

            text2show, xt, yt = check_text(x, y)
            sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

        d -= 1
        marsi.go_stop()
        sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

    # 3. Die Tastatur über die Methode des Objekts prüfen.
    x, y, left, right, run = marsi.check_key()

    text2show, xt, yt = check_text(x, y)
    sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

sf.screen.bye()
