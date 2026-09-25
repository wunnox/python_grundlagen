"""Turtle-Modul für die Stadtlauf-Bern-Übungen.

Liest GIF-Bilder aus dem Verzeichnis 'Bilder' neben diesem Modul.
Die Spiele verwenden weiterhin Koordinaten mit Ursprung oben links.
"""

from pathlib import Path
import time
import turtle

BREITE = 1050
HOEHE = 400
BILDER = Path(__file__).resolve().parent / "Bilder"


def _bild(dateiname):
    pfad = BILDER / dateiname
    if not pfad.is_file():
        raise FileNotFoundError(f"GIF-Datei fehlt: {pfad}")
    return str(pfad)


KARTE = _bild("karte-bern_kl.gif")
CHAR = _bild("standing.gif")
walkRight = [_bild(f"R{i}.gif") for i in range(1, 10)]
walkLeft = [_bild(f"L{i}.gif") for i in range(1, 10)]

screen = turtle.Screen()
screen.setup(width=BREITE + 20, height=HOEHE + 20)
screen.title("Spaziergang durch Bern")
screen.tracer(0, 0)
screen.bgpic(KARTE)

for datei in [CHAR, *walkRight, *walkLeft]:
    screen.register_shape(datei)

# Tk-GIF-Bilder haben eine feste Pixelgrösse. Diese wird für die
# Umrechnung von pygame-Position (linke obere Ecke) zu Turtle-Mitte benötigt.
_bildgroessen = {
    datei: (
        screen._shapes[datei]._data.width(),
        screen._shapes[datei]._data.height(),
    )
    for datei in [CHAR, *walkRight, *walkLeft]
}

_figur = turtle.Turtle(visible=False)
_figur.penup()
_figur.speed(0)

_textstift = turtle.Turtle(visible=False)
_textstift.penup()
_textstift.speed(0)
_textstift.color("red")

x = 20
y = 155
end = 1050
left = False
right = False
walkCount = 0
run = True

_tasten = set()
_beenden = False


def _taste_druecken(taste):
    _tasten.add(taste)


def _taste_loslassen(taste):
    _tasten.discard(taste)


def _beenden():
    global _beenden
    _beenden = True


for _taste in ("Right", "Left", "Up", "Down"):
    screen.onkeypress(lambda taste=_taste: _taste_druecken(taste), _taste)
    screen.onkeyrelease(lambda taste=_taste: _taste_loslassen(taste), _taste)
screen.onkeypress(_beenden, "q")
screen.listen()


def _fenster_aktualisieren():
    """Verarbeitet Tk-Ereignisse auch während der automatischen Schleifen."""
    try:
        screen.getcanvas().update()
    except (turtle.Terminator, turtle.TurtleGraphicsError):
        return False
    return True


def _bild_zeichnen(datei):
    """Zeichnet ein GIF mit seiner linken oberen Ecke bei (x, y)."""
    breite, hoehe = _bildgroessen[datei]
    _figur.shape(datei)
    _figur.goto(
        x + breite / 2 - BREITE / 2,
        HOEHE / 2 - y - hoehe / 2,
    )
    _figur.showturtle()


def redrawGameWindow(text2show="", xt=None, yt=None):
    """Zeichnet Marsi und optional einen Text an (xt, yt).

    Unterstützt sowohl redrawGameWindow() als auch
    redrawGameWindow(text2show, xt, yt) aus den Übungen.
    """
    global walkCount

    if xt is None:
        xt = x
    if yt is None:
        yt = y

    _textstift.clear()
    if text2show:
        _textstift.goto(xt - BREITE / 2, HOEHE / 2 - yt)
        _textstift.write(
            text2show,
            align="left",
            font=("Comic Sans MS", 20, "normal"),
        )

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        datei = walkLeft[walkCount // 3]
        walkCount += 1
    elif right:
        datei = walkRight[walkCount // 3]
        walkCount += 1
    else:
        datei = CHAR
        walkCount = 0

    _bild_zeichnen(datei)
    screen.update()
    _fenster_aktualisieren()


def go_walk_right(gx, gy):
    """Setzt Marsi auf eine vorgegebene Position und zeigt nach rechts."""
    global x, y, left, right
    x, y = gx, gy
    left, right = False, True
    return x, y


def go_walk_left(gx, gy):
    """Setzt Marsi auf eine vorgegebene Position und zeigt nach links."""
    global x, y, left, right
    x, y = gx, gy
    left, right = True, False
    return x, y


def go_left(steps=1):
    """Bewegt Marsi nach links."""
    global x, left, right
    if x > 1:
        x -= steps
        left, right = True, False
        return x
    go_stop()
    return None


def go_right(steps=1):
    """Bewegt Marsi nach rechts."""
    global x, left, right
    if x < end:
        x += steps
        left, right = False, True
        return x
    go_stop()
    return None


def go_stop():
    """Zeigt das stehende GIF an und stoppt die Animation."""
    global left, right
    left, right = False, False


def go_up(steps=1):
    """Bewegt Marsi nach oben (Bildkoordinaten)."""
    global y
    y -= steps
    return y


def go_down(steps=1):
    """Bewegt Marsi nach unten (Bildkoordinaten)."""
    global y
    y += steps
    return y


def check_key():
    """Verarbeitet die Pfeiltasten und beendet bei q oder Fensterschluss."""
    if not _fenster_aktualisieren() or _beenden:
        return False

    if "Right" in _tasten:
        go_right(2)
        print("Position x,y: ", x, y)
    elif "Left" in _tasten:
        go_left(2)
        print("Position x,y: ", x, y)

    if "Up" in _tasten:
        go_up()
        print("Position x,y: ", x, y)
    elif "Down" in _tasten:
        go_down()
        print("Position x,y: ", x, y)

    time.sleep(1 / 60)
    return True
