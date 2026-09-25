####################################################
#
# Übung: Stadtlauf Bern mit while-Schleife und Turtle
#
# Erweitern Sie das Programm so, dass Marsi bis zur
# Gerechtigkeitsgasse läuft.
#
# Verwenden Sie hierfür eine while-Schleife.
# Die Gerechtigkeitsgasse beginnt bei der x-Position 670.
#
# Vorhandene Funktionen aus stadtlauf_bern_modul.py
#
# go_right()          : Geht einen Schritt nach rechts
# go_left()           : Geht einen Schritt nach links
# go_up()             : Geht einen Schritt nach oben
# go_down()           : Geht einen Schritt nach unten
# go_stop()           : Stoppt die Bewegung
# redrawGameWindow()  : Zeichnet die Turtle-Grafik neu
# check_key()         : Prüft Pfeiltasten und die Taste q
#
# Hinweis: Neuer Code nur im markierten Bereich eintragen.
#
####################################################

import time
from stadtlauf_bern_modul import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur

while run:
    if d > 0:

        # Lauf zum Zytglogge-Turm
        for i in range(440):
            time.sleep(slower)
            x = go_right()
            if x % 10 == 0 and x <= 210:
                y = go_up()
            elif x % 10 == 0 and x < 450:
                y = go_down()
            redrawGameWindow()

        ####################################################
        # Hier kommt Ihr Code (ab diesem Einzug)
        # Lauf zur Gerechtigkeitsgasse


        # bis hier
        ####################################################

        d -= 1
        go_stop()
        redrawGameWindow()

    # Nach dem automatischen Lauf kann Marsi manuell bewegt werden.
    # Die Taste q beendet die while-Schleife.
    run = check_key()
    redrawGameWindow()

screen.bye()
