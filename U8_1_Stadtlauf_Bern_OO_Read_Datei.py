####################################################
# Übung: Stadtlauf Bern OO – Wegdaten aus Datei lesen
#
# Öffnen Sie die Datei mit den aufgezeichneten Wegdaten.
# Lesen Sie die Wegdaten ein und lassen Sie Marsi den
# aufgezeichneten Weg erneut ablaufen.
#
# Das erwartete Dateiformat pro Zeile lautet:
# x:y:left:right
#
# Beispiel:
# 21:155:False:True
####################################################

import time
import stadtlauf_bern_oo_modul as sf
from U5_6_stadtlauf_Bern_check_text_turtle import check_text

SLOWER = 0.01
marsi = sf.Figur("Marsi")

####################################################
# Hier kommt Ihr Code
# Wegdaten aus Datei einlesen.
# Tipp: with open("Wegdaten_OO.txt", encoding="utf-8") as datei:
#           alleschritte = datei.readlines()


# bis hier
####################################################

####################################################
# Hier kommt Ihr Code
# Wegdaten abschreiten.
# Je nach gespeicherter Richtung verwenden Sie:
# marsi.go_walk_left(gx, gy) oder marsi.go_walk_right(gx, gy)


# bis hier
####################################################

# Das Fenster bleibt nach dem automatischen Ablauf geöffnet.
# q oder das Schliessen des Fensters beendet das Programm.
run = True
while run:
    x, y, left, right, run = marsi.check_key()
    text2show, xt, yt = check_text(x, y)
    sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

sf.screen.bye()
