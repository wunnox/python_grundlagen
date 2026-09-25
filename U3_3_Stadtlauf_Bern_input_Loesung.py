"""Musterlösung: Eingabe von Schritten für den Stadtlauf mit Turtle.

Benötigt stadtlauf_bern_modul.py sowie die GIF-Bilder in Bilder/.
Die Eingabe erfolgt im Terminal; danach läuft Marsi im Turtle-Fenster.
"""

import time
import stadtlauf_bern_modul as sf

SLOWER = 0.01
MAX_X = 450


def lauf(schritte):
    """Bewegt Marsi um höchstens 'schritte' Positionen nach rechts."""
    for _ in range(schritte):
        time.sleep(SLOWER)
        x = sf.go_right()
        if x is None:
            break

        if x % 10 == 0 and x <= 210:
            sf.go_up()
        elif x % 10 == 0 and x < MAX_X:
            sf.go_down()

        sf.redrawGameWindow()

        if x > MAX_X:
            sf.go_stop()
            sf.redrawGameWindow("Weiter geht's nicht mehr", x, sf.y - 10)
            return False

    sf.go_stop()
    sf.redrawGameWindow()
    return True


def main():
    sf.redrawGameWindow()

    while True:
        try:
            schritte = int(input("Geben Sie die Anzahl Schritte zw. 10 und 450 ein: "))
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")
            continue
        except (EOFError, KeyboardInterrupt):
            break

        if schritte > 450:
            schritte = 450
        elif schritte < 10:
            schritte = 10

        if not lauf(schritte):
            # Das automatische Spiel endet am Zytglogge; das Fenster bleibt
            # sichtbar, bis es geschlossen oder q gedrückt wird.
            break

    try:
        sf.screen.mainloop()
    except sf.turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
