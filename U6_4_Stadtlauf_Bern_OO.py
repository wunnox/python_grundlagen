####################################################
# Übung: Stadtlauf Bern – objektorientiert mit Turtle
#
# Der Berner Stadtlauf ist objektorientiert programmiert:
# - Die Klasse Figur wird über sf.Figur aufgerufen.
# - Marsi wird als Objekt der Klasse Figur erstellt.
# - Bewegungen erfolgen über Methoden des Objekts.
#
# Erstellen Sie ein Objekt mit einem Namen Ihrer Wahl und lassen
# Sie es den gespeicherten Weg zum Zytglogge ablaufen.
#
# Hinweis: In jedem der drei markierten Bereiche genügt eine Zeile.
####################################################

import time
import stadtlauf_bern_oo_modul as sf
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd
from U5_6_stadtlauf_Bern_check_text import check_text

run = True
d = 1
slower = 0.01

####################################################
# Hier kommt Ihr neuer Code
# Figur als Objekt initialisieren, beispielsweise:
# marsi = sf.Figur("Marsi")


# bis hier
####################################################

text2show = ""
xt = 0
yt = 0

while run:
    if d > 0:
        for gx, gy in wd.weg["Zytglogge"]:
            time.sleep(slower)

            ####################################################
            # Hier kommt Ihr neuer Code
            # Figur den vorgegebenen Weg laufen lassen.
            # Verwenden Sie: marsi.go_walk_right(gx, gy)


            # bis hier
            ####################################################

            text2show, xt, yt = check_text(x, y)
            sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

        d -= 1
        marsi.go_stop()
        sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

    ####################################################
    # Hier kommt Ihr neuer Code
    # Tastatur prüfen. Verwenden Sie: marsi.check_key()


    # bis hier
    ####################################################

    text2show, xt, yt = check_text(x, y)
    sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

sf.screen.bye()
