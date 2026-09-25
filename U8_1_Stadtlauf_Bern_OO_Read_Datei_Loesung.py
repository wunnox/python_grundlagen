####################################################
# Musterlösung: Stadtlauf Bern OO – Wegdaten aus Datei lesen
####################################################

import time
import stadtlauf_bern_oo_modul as sf
from U5_6_stadtlauf_Bern_check_text import check_text

SLOWER = 0.01
marsi = sf.Figur("Marsi")

# Wegdaten aus Datei einlesen.
with open("Wegdaten_OO.txt", "r", encoding="utf-8") as datei:
    alleschritte = datei.readlines()

# Wegdaten abschreiten.
for schritt in alleschritte:
    gx, gy, gl, gr = schritt.rstrip().split(":")
    gx, gy = int(gx), int(gy)

    time.sleep(SLOWER)
    if gl == "True":
        x, y, left, right = marsi.go_walk_left(gx, gy)
    elif gr == "True":
        x, y, left, right = marsi.go_walk_right(gx, gy)
    else:
        x, y, left, right = marsi.go_stop()

    text2show, xt, yt = check_text(x, y)
    sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

# Das Fenster bleibt nach dem automatischen Ablauf geöffnet.
# q oder das Schliessen des Fensters beendet das Programm.
run = True
while run:
    x, y, left, right, run = marsi.check_key()
    text2show, xt, yt = check_text(x, y)
    sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

sf.screen.bye()
