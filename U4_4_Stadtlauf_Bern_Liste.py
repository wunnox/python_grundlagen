####################################################
#
# Übung: Stadtlauf Bern – Listen mit Turtle
#
# Marsi läuft zum Zytglogge-Turm. Zeichnen Sie den Weg,
# den die Figur läuft, in einer Liste auf. Damit kann der Weg
# später anhand dieser Daten nochmals abgelaufen werden.
#
# Erfassen Sie jede x/y-Position in einer Subliste.
# Geben Sie den Inhalt der Liste am Ende im Terminal aus.
#
# Hinweis: Neuer Code nur in den drei markierten Bereichen.
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur


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


####################################################
# Hier kommt Ihr Code
# Liste "weg" für Wegdaten erstellen


# bis hier
####################################################

text2show = ""
xt, yt = x, y

while run:
    if d > 0:

        # Lauf zum Zytglogge-Turm
        for i in range(450):
            time.sleep(slower)
            x = go_right()
            if x % 10 == 0 and x <= 210:
                y = go_up()
            elif x % 10 == 0 and x < 450:
                y = go_down()

            text2show, xt, yt = check_text(x, y)
            redrawGameWindow(text2show, xt, yt - 15)

            ####################################################
            # Hier kommt Ihr Code
            # Liste mit Wegdaten abfüllen


            # bis hier
            ####################################################

        d -= 1
        go_stop()
        redrawGameWindow(text2show, xt, yt - 15)

    run = check_key()
    text2show, xt, yt = check_text(x, y)
    redrawGameWindow(text2show, xt, yt - 15)

screen.bye()

####################################################
# Hier kommt Ihr Code
# Wegdaten im Terminal ausgeben


# bis hier
####################################################
