####################################################
#
# Übung: Stadtlauf Bern mit for-Schleife und Turtle
#
# In diesem Script läuft die Figur zunächst nur zum Käfigturm.
# Ergänzen Sie im markierten Bereich den Lauf bis zum Zytglogge.
#
# Lernziele
# - Eine for-Schleife für eine wiederholte Bewegung einsetzen.
# - Mit dem Modulo-Operator (%) jeden zehnten Schritt erkennen.
# - Vorhandene Funktionen verwenden.
#
# Auftrag
# - Lassen Sie Marsi mit einer for-Schleife weitere 230 Schritte nach rechts
#   bis zum Zytglogge laufen.
# - Bei jedem zehnten Schritt soll Marsi einen Schritt nach unten gehen.
# - Reduzieren Sie die Laufgeschwindigkeit mit time.sleep(slower).
# - Aktualisieren Sie nach jedem Durchlauf das Bild mit redrawGameWindow().
# - Die Funktion redrawGameWindow() muss die letzte Zeile der for-Schleife sein.
#
# Vorhandene Funktionen
# - go_right(): einen Schritt nach rechts
# - go_left(): einen Schritt nach links
# - go_up(): einen Schritt nach oben
# - go_down(): einen Schritt nach unten
# - go_stop(): Bewegung stoppen
# - redrawGameWindow(): Turtle-Grafik neu zeichnen
#
# Taste q: Spiel beenden
#
####################################################

import time
from stadtlauf_bern_import *

# Variablen
d = 1
slower = 0.01  # Je höher die Zahl, umso langsamer läuft die Figur

# Start der Darstellung
while run:
    if d > 0:

        # Lauf zum Käfigturm
        for i in range(210):
            time.sleep(slower)
            x = go_right()
            if x % 10 == 0:
                y = go_up()

            redrawGameWindow()

        ####################################################
        # Hier kommt Ihr Code (ab diesem Einzug)
        # Lauf zum Zytglogge


        # bis hier
        ####################################################

        d -= 1
        go_stop()
        redrawGameWindow()

    # Nach dem automatischen Lauf: manuelle Steuerung.
    # Die Funktion wartet auf Tastenereignisse und liefert False bei q.
    run = check_key()
    redrawGameWindow()

screen.bye()
