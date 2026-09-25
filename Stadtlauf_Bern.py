"""Stadtlauf Bern – Turtle-Version der einfachen pygame-Fassung.

Benötigte Dateien:
- stadtlauf_bern_sehenswuerdigkeiten_inventar.py
- Bilder/karte-bern_kl.gif
- Bilder/standing.gif
- Bilder/R1.gif ... Bilder/R9.gif
- Bilder/L1.gif ... Bilder/L9.gif

Steuerung nach dem automatischen Hin- und Rücklauf:
- Pfeiltasten: Marsi bewegen
- q: Fenster/Spiel beenden
"""

from pathlib import Path
import turtle

import stadtlauf_bern_sehenswuerdigkeiten_inventar as sbi

# Entspricht den Einstellungen des pygame-Originals
BREITE = 1050
HOEHE = 400
TICK_MS = 37               # pygame: clock.tick(27)
SLOWER = 0.01              # pygame: time.sleep(slower)
PAUSE_MS = int(SLOWER * 1000)
BILDER = Path(__file__).resolve().parent / "Bilder"


def bild(name):
    """Gibt den geprüften absoluten Pfad zu einer GIF-Datei zurück."""
    pfad = BILDER / name
    if not pfad.is_file():
        raise FileNotFoundError(f"Benötigtes Bild fehlt: {pfad}")
    return str(pfad)


KARTE = bild("karte-bern_kl.gif")
CHAR = bild("standing.gif")
WALK_RIGHT = [bild(f"R{i}.gif") for i in range(1, 10)]
WALK_LEFT = [bild(f"L{i}.gif") for i in range(1, 10)]

# Turtle verwendet seine Koordinaten mit Ursprung in der Bildschirmmitte.
# pygame setzt Bilder hingegen mit der linken oberen Bildecke bei (x, y) ab.
def pygame_zu_turtle(x, y, bildbreite, bildhoehe):
    return (
        x + bildbreite / 2 - BREITE / 2,
        HOEHE / 2 - y - bildhoehe / 2,
    )


screen = turtle.Screen()
screen.setup(BREITE + 20, HOEHE + 20)
screen.title("Spaziergang durch Bern – Turtle")
screen.tracer(0, 0)
screen.bgpic(KARTE)

for datei in [CHAR, *WALK_RIGHT, *WALK_LEFT]:
    screen.register_shape(datei)


def groesse(datei):
    """Ermittelt Breite und Höhe eines bei Turtle registrierten GIFs."""
    tk_bild = screen._shapes[datei]._data
    return tk_bild.width(), tk_bild.height()


BILDGROESSEN = {datei: groesse(datei) for datei in [CHAR, *WALK_RIGHT, *WALK_LEFT]}

marsi = turtle.Turtle(visible=False)
marsi.penup()
marsi.speed(0)
textstift = turtle.Turtle(visible=False)
textstift.penup()
textstift.color("red")
textstift.speed(0)

# Die gleichen Zustandsvariablen wie im pygame-Modul
x = 20
y = 155
ende = 1050
left = False
right = False
walk_count = 0
run = True
text2show = ""
xt = 0
yt = 0

# Ablauf der zwei ursprünglichen for-Schleifen
phase = "hin"
schritt = 0


def check_text(pos_x, pos_y):
    """Prüft, welche Sehenswürdigkeit an der Position angezeigt werden soll."""
    sehenswurdigkeit = ""
    for name in sbi.sehensw:
        if pos_x in sbi.pos[name][0] and pos_y in sbi.pos[name][1]:
            sehenswurdigkeit = name
    return sehenswurdigkeit, pos_x, pos_y - 15


def go_left(steps=1):
    global x, left, right
    if x > 1:
        x -= steps
        left = True
        right = False
        return x
    go_stop()
    return None


def go_right(steps=1):
    global x, left, right
    if x < ende:
        x += steps
        left = False
        right = True
        return x
    go_stop()
    return None


def go_up(steps=1):
    global y
    y -= steps
    return y


def go_down(steps=1):
    global y
    y += steps
    return y


def go_stop():
    global left, right
    left = False
    right = False


def zeichne_bild(datei):
    """Zeichnet das GIF an derselben Position wie screen.blit(datei, (x, y))."""
    bildbreite, bildhoehe = BILDGROESSEN[datei]
    marsi.shape(datei)
    marsi.goto(*pygame_zu_turtle(x, y, bildbreite, bildhoehe))
    marsi.showturtle()


def redraw_game_window():
    """Entspricht redrawGameWindow() des pygame-Moduls."""
    global walk_count

    textstift.clear()
    if text2show:
        textstift.goto(xt - BREITE / 2, HOEHE / 2 - yt)
        textstift.write(text2show, align="left", font=("Comic Sans MS", 20, "normal"))

    if walk_count + 1 >= 27:
        walk_count = 0

    if left:
        zeichne_bild(WALK_LEFT[walk_count // 3])
        walk_count += 1
    elif right:
        zeichne_bild(WALK_RIGHT[walk_count // 3])
        walk_count += 1
    else:
        zeichne_bild(CHAR)
        walk_count = 0

    screen.update()


def hin_schritt():
    """Erste Originalschleife: 440 Schritte nach rechts Richtung Zytglogge."""
    global schritt
    go_right()
    if x % 10 == 0 and x < 210:
        go_up()
    elif x % 10 == 0 and x < 450:
        go_down()
    schritt += 1


def rueck_schritt():
    """Zweite Originalschleife: 470 Schritte zurück nach links."""
    global schritt
    neue_x = go_left()
    if neue_x is None:
        # Wie im Original: if x == None: x = 0
        # Der Rückgabewert wird dort auf 0 gesetzt; die globale x-Position
        # bleibt aufgrund von go_stop() unverändert.
        neue_x = 0
    if x < 450 and x > 420:
        go_down()
    elif x < 140 and x > 13 and x % 10 == 0:
        go_down()
    elif x < 16:
        go_up(2)
    schritt += 1


def automatischer_lauf():
    """Ersetzt die blockierenden pygame-for-Schleifen durch Turtle-ontimer."""
    global phase, schritt, text2show, xt, yt

    if not run:
        return

    if phase == "hin":
        if schritt < 440:
            hin_schritt()
        else:
            phase = "zurueck"
            schritt = 0
    elif phase == "zurueck":
        if schritt < 470:
            rueck_schritt()
        else:
            phase = "manuell"
            schritt = 0
            go_stop()

    text2show, xt, yt = check_text(x, y)
    redraw_game_window()

    if phase in ("hin", "zurueck"):
        screen.ontimer(automatischer_lauf, TICK_MS + PAUSE_MS)
    else:
        # Die pygame-Version zeichnet nach dem ersten Durchgang eine stehende Figur.
        # Danach reagieren die Tastenereignisse direkt über die bind()-Funktionen.
        redraw_game_window()


def manuell_bewegen(dx, dy):
    """Entspricht check_key(): pro Tastendruck bewegen und Position ausgeben."""
    global x, y, text2show, xt, yt
    if not run:
        return

    if dx > 0:
        go_right(2)
    elif dx < 0:
        go_left(2)

    if dy < 0:
        go_up(1)
    elif dy > 0:
        go_down(1)

    print("Position x,y: ", x, y)
    text2show, xt, yt = check_text(x, y)
    redraw_game_window()


def beenden():
    global run
    run = False
    screen.bye()


def main():
    screen.onkey(lambda: manuell_bewegen(-2, 0), "Left")
    screen.onkey(lambda: manuell_bewegen(2, 0), "Right")
    screen.onkey(lambda: manuell_bewegen(0, -1), "Up")
    screen.onkey(lambda: manuell_bewegen(0, 1), "Down")
    screen.onkey(beenden, "q")
    screen.listen()
    automatischer_lauf()
    screen.mainloop()


if __name__ == "__main__":
    main()
