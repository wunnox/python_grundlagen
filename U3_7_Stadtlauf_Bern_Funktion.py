####################################################
#
# Übung: Stadtlauf Bern – Funktionen mit Turtle
#
# Erstellen Sie eine Funktion mit dem Namen check_text().
# Verschieben Sie die Prüfung, ob eine Sehenswürdigkeit angezeigt
# werden soll, in diese Funktion. Rufen Sie anschliessend nur noch
# diese Funktion auf.
#
# Die Funktion soll drei Werte zurückgeben:
# - den anzuzeigenden Text,
# - die x-Position des Textes,
# - die y-Position des Textes.
#
# Vorhandene Funktionen aus stadtlauf_bern_modul.py
#
# go_right()                     : Geht einen Schritt nach rechts
# go_left()                      : Geht einen Schritt nach links
# go_up()                        : Geht einen Schritt nach oben
# go_down()                      : Geht einen Schritt nach unten
# go_stop()                      : Stoppt die Bewegung
# redrawGameWindow(text, x, y)   : Zeichnet die Turtle-Grafik neu
# check_key()                    : Prüft Pfeiltasten und Taste q
#
# Hinweis: Neuer Code nur im markierten Bereich eintragen.
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur
text2show = ""
xt, yt = x, y

####################################################
# Hier kommt Ihre Funktion hin


# bis hier
####################################################

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

            # Prüfung über die selbst erstellte Funktion.
            text2show, xt, yt = check_text(x, y)
            redrawGameWindow(text2show, xt, yt - 15)

        d -= 1
        go_stop()
        redrawGameWindow(text2show, xt, yt - 15)

    # Nach dem automatischen Lauf kann Marsi manuell bewegt werden.
    # Die Taste q beendet die while-Schleife.
    run = check_key()
    text2show, xt, yt = check_text(x, y)
    redrawGameWindow(text2show, xt, yt - 15)

screen.bye()
