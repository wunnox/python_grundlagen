"""Objektorientiertes Turtle-Modul für die Stadtlauf-Bern-Übungen."""

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
screen.title("Spaziergang durch Bern – objektorientiert")
screen.tracer(0, 0)
screen.bgpic(KARTE)

for datei in [CHAR, *walkRight, *walkLeft]:
    screen.register_shape(datei)

_bildgroessen = {
    datei: (screen._shapes[datei]._data.width(), screen._shapes[datei]._data.height())
    for datei in [CHAR, *walkRight, *walkLeft]
}

_textstift = turtle.Turtle(visible=False)
_textstift.penup()
_textstift.speed(0)
_textstift.color("red")

_tasten = set()
_beenden = False


def _taste_druecken(taste):
    _tasten.add(taste)


def _taste_loslassen(taste):
    _tasten.discard(taste)


def _q_gedrueckt():
    global _beenden
    _beenden = True


for _taste in ("Right", "Left", "Up", "Down"):
    screen.onkeypress(lambda taste=_taste: _taste_druecken(taste), _taste)
    screen.onkeyrelease(lambda taste=_taste: _taste_loslassen(taste), _taste)
screen.onkeypress(_q_gedrueckt, "q")
screen.listen()


class Clock:
    """Kleiner Ersatz für pygame.time.Clock()."""

    def tick(self, fps):
        if fps > 0:
            time.sleep(1 / fps)


clock = Clock()


def _fenster_aktualisieren():
    try:
        screen.getcanvas().update()
    except (turtle.Terminator, turtle.TurtleGraphicsError):
        return False
    return True


def redrawGameWindow(text2show="", xt=None, yt=None, figur=None):
    """Zeichnet eine Figur und optional den Text einer Sehenswürdigkeit.

    figur ist ein Objekt der Klasse Figur. Die bisherigen x/y/left/right-
    Einzelparameter werden dadurch nicht mehr benötigt.
    """
    _textstift.clear()
    if text2show:
        if xt is None:
            xt = figur.x if figur else 0
        if yt is None:
            yt = figur.y if figur else 0
        _textstift.goto(xt - BREITE / 2, HOEHE / 2 - yt)
        _textstift.write(text2show, align="left", font=("Comic Sans MS", 20, "normal"))

    if figur is not None:
        figur.zeichnen()

    screen.update()
    _fenster_aktualisieren()


class Figur:
    """Eine mit GIF-Bildern animierte Spielfigur."""

    def __init__(self, name):
        self.name = name
        self.x = 20
        self.y = 155
        self.end = 1050
        self.left = False
        self.right = False
        self.walk_count = 0
        self.sprite = turtle.Turtle(visible=False)
        self.sprite.penup()
        self.sprite.speed(0)

    def _bild_zeichnen(self, datei):
        breite, hoehe = _bildgroessen[datei]
        self.sprite.shape(datei)
        self.sprite.goto(
            self.x + breite / 2 - BREITE / 2,
            HOEHE / 2 - self.y - hoehe / 2,
        )
        self.sprite.showturtle()

    def zeichnen(self):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if self.left:
            datei = walkLeft[self.walk_count // 3]
            self.walk_count += 1
        elif self.right:
            datei = walkRight[self.walk_count // 3]
            self.walk_count += 1
        else:
            datei = CHAR
            self.walk_count = 0

        self._bild_zeichnen(datei)

    def go_walk_right(self, gx, gy):
        self.x, self.y = gx, gy
        self.left, self.right = False, True
        return self.x, self.y, self.left, self.right

    def go_walk_left(self, gx, gy):
        self.x, self.y = gx, gy
        self.left, self.right = True, False
        return self.x, self.y, self.left, self.right

    def go_left(self, steps=1):
        if self.x > 1:
            self.x -= steps
            self.left, self.right = True, False
        else:
            self.go_stop()
        return self.x, self.y, self.left, self.right

    def go_right(self, steps=1):
        if self.x < self.end:
            self.x += steps
            self.left, self.right = False, True
        else:
            self.go_stop()
        return self.x, self.y, self.left, self.right

    def go_up(self, steps=1):
        self.y -= steps
        return self.x, self.y, self.left, self.right

    def go_down(self, steps=1):
        self.y += steps
        return self.x, self.y, self.left, self.right

    def go_stop(self):
        self.left, self.right = False, False
        return self.x, self.y, self.left, self.right

    def check_key(self):
        """Steuert genau dieses Objekt mit Pfeiltasten; q beendet das Spiel."""
        if not _fenster_aktualisieren() or _beenden:
            return self.x, self.y, self.left, self.right, False

        if "Right" in _tasten:
            self.go_right(2)
            print("Position x,y: ", self.x, self.y)
        elif "Left" in _tasten:
            self.go_left(2)
            print("Position x,y: ", self.x, self.y)

        if "Up" in _tasten:
            self.go_up()
            print("Position x,y: ", self.x, self.y)
        elif "Down" in _tasten:
            self.go_down()
            print("Position x,y: ", self.x, self.y)

        time.sleep(1 / 60)
        return self.x, self.y, self.left, self.right, True
