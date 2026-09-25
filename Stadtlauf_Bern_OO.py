"""Stadtlauf Bern mit Turtle und den Originalbildern als GIF.

Verzeichnisstruktur:
  stadtlauf_bern.py
  stadtlauf_bern_sehenswuerdigkeiten_inventar.py
  stadtlauf_bern_wegpunkte.py
  Bilder/karte-bern_kl.gif, standing.gif, Sonne2.gif,
         R1.gif ... R9.gif, L1.gif ... L9.gif,
         Rchicken1.gif ... Rchicken9.gif,
         Lchicken1.gif ... Lchicken9.gif,
         chickendead1.gif ... chickendead8.gif
"""

import datetime
from pathlib import Path
import random
import turtle

import stadtlauf_bern_sehenswuerdigkeiten_inventar as sbi
import stadtlauf_bern_wegpunkte as wp

BREITE, HOEHE = 1050, 400
TICK_MS = 37
ANZAHL_MOORHUEHNER = 3
MOORHUHN_INTERVALL = 50
BILDER = Path(__file__).resolve().parent / "Bilder"


def bild(name):
    """Prüft eine Bilddatei und gibt ihren absoluten Pfad zurück."""
    pfad = BILDER / name
    if not pfad.is_file():
        raise FileNotFoundError(f"Benötigtes GIF fehlt: {pfad}")
    return str(pfad)


def bildfolge(muster, anzahl=9):
    return [bild(muster.format(i)) for i in range(1, anzahl + 1)]


# Bilder wie in der ursprünglichen pygame-Fassung laden.
WALK_RIGHT = bildfolge("R{}.gif")
WALK_LEFT = bildfolge("L{}.gif")
HUHN_RIGHT = bildfolge("Rchicken{}.gif")
HUHN_LEFT = bildfolge("Lchicken{}.gif")
# Bild 9 war im Original nochmals chickendead8.png.
HUHN_TOT = bildfolge("chickendead{}.gif", 8)
HUHN_TOT.append(HUHN_TOT[-1])
STANDING = bild("standing.gif")
SONNE = bild("Sonne2.gif")
KARTE = bild("karte-bern_kl.gif")

screen = turtle.Screen()
screen.setup(width=BREITE + 20, height=HOEHE + 20)
screen.title("Spaziergang durch Bern – Turtle/GIF")
screen.tracer(0, 0)
screen.bgpic(KARTE)
for datei in set(WALK_RIGHT + WALK_LEFT + HUHN_RIGHT + HUHN_LEFT + HUHN_TOT + [STANDING, SONNE]):
    screen.register_shape(datei)


def pos(x, y, breite=0, hoehe=0):
    """Bild-Position von pygame (oben links) zu Turtle (Bildmitte) umrechnen."""
    return (x + breite / 2 - BREITE / 2,
            HOEHE / 2 - y - hoehe / 2)


def abmessungen(datei):
    """Ermittelt die echte Bildgrösse über das von Turtle verwendete Tk."""
    foto = screen._shapes[datei]._data
    return foto.width(), foto.height()


BILDGROESSEN = {datei: abmessungen(datei) for datei in
                 set(WALK_RIGHT + WALK_LEFT + HUHN_RIGHT + HUHN_LEFT + HUHN_TOT + [STANDING, SONNE])}


def setze_bild(sprite, datei, x, y):
    """Positioniert das GIF passend zur ursprünglichen blit(x, y)-Position."""
    breite, hoehe = BILDGROESSEN[datei]
    sprite.shape(datei)
    sprite.goto(*pos(x, y, breite, hoehe))
    sprite.showturtle()


def sprite_neu():
    sprite = turtle.Turtle(visible=False)
    sprite.penup()
    sprite.speed(0)
    return sprite


def kollidiert_rect(a, b, width_a=40, height_a=60, width_b=40, height_b=60):
    ax1, ay1 = a["x"], a["y"]
    ax2, ay2 = ax1 + width_a, ay1 + height_a
    bx1, by1 = b["x"], b["y"]
    bx2, by2 = bx1 + width_b, by1 + height_b
    return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)


def check_text(x, y):
    for sehenswurdigkeit in sbi.sehensw:
        if x in sbi.pos[sehenswurdigkeit][0] and y in sbi.pos[sehenswurdigkeit][1]:
            return sehenswurdigkeit, x, y - 15
    return "", x, y - 15


def walk_generator(weg):
    yield from range(len(weg))


def wege_analysieren():
    wege = {}
    for name in wp.wegpunkt:
        start, ziel = name.split("-", 1)
        wege.setdefault(start, []).append((name, ziel))
    return wege


def sonnenstand():
    jetzt = datetime.datetime.now()
    stunde, minute = jetzt.hour, jetzt.minute
    x, y = 1100, 400
    if stunde > 6:
        x -= 100 * (stunde - 6) + minute * 1.66
    if 6 < stunde <= 12:
        y -= 30 * (stunde - 6) + minute * 0.5
    else:
        y -= 30 * (18 - stunde) + minute * 0.5
    return int(x), int(y)


class Figur:
    def __init__(self, name):
        self.name = name
        self.sprite = sprite_neu()
        self.anim = 0

    def zeichnen(self, x, y, frames):
        datei = frames[(self.anim // 3) % len(frames)]
        setze_bild(self.sprite, datei, x, y)
        self.anim = (self.anim + 1) % (3 * len(frames))

    def verstecken(self):
        self.sprite.hideturtle()
        self.anim = 0


class Spiel:
    def __init__(self):
        self.wege = wege_analysieren()
        self.strecke, self.ende = self.neues_ziel("Bahnhofplatz")
        self.schritt = walk_generator(wp.wegpunkt[self.strecke])
        self.marsi = {
            "name": "Marsi0", "obj": Figur("Marsi"), "Status": "Go",
            "x": 20, "y": 150, "Seite": "Stop",
        }
        self.moorhuehner = []
        for nummer in range(ANZAHL_MOORHUEHNER):
            self.moorhuehner.append({
                "name": f"Moorhuhn{nummer}", "obj": Figur(f"Moori{nummer}"),
                "Status": "Stop", "x": 1000, "y": 20, "Seite": "Stop",
                "intervall": MOORHUHN_INTERVALL,
                "counter": random.randint(0, MOORHUHN_INTERVALL),
                "richtung": "right",
            })
        self.sonne = sprite_neu()
        self.sonne_dict = {"x": 0, "y": 0}
        self.text_sprite = sprite_neu()
        self.text_sprite.color("red")
        self.aktiv = True
        # Tastenimpulse sind zusätzlich zum automatischen Wegpunktlauf wirksam.
        self.tastenbewegung = [0, 0]

    def neues_ziel(self, start):
        moeglichkeiten = self.wege.get(start)
        if not moeglichkeiten:
            # Ein Ziel ohne ausgehenden Weg: zum Bahnhofplatz zurückkehren.
            moeglichkeiten = self.wege["Bahnhofplatz"]
        return random.choice(moeglichkeiten)

    def taste(self, dx, dy):
        self.tastenbewegung[0] += dx
        self.tastenbewegung[1] += dy

    def beenden(self):
        self.aktiv = False
        screen.bye()

    def marsi_bewegen(self):
        try:
            nummer = next(self.schritt)
            x, y, links, _rechts = wp.wegpunkt[self.strecke][nummer]
            self.marsi["x"], self.marsi["y"] = x, y
            self.marsi["Seite"] = "left" if links else "right"
        except StopIteration:
            self.strecke, self.ende = self.neues_ziel(self.ende)
            self.schritt = walk_generator(wp.wegpunkt[self.strecke])
            print(f"Laufe Strecke {self.strecke}")
        dx, dy = self.tastenbewegung
        self.marsi["x"] = max(-10, min(1000, self.marsi["x"] + dx))
        self.marsi["y"] = max(-10, min(340, self.marsi["y"] + dy))
        if dx:
            self.marsi["Seite"] = "right" if dx > 0 else "left"
        self.tastenbewegung = [0, 0]

    def moorhuehner_bewegen(self):
        for mh in self.moorhuehner:
            if mh["Status"] == "Stop":
                mh["counter"] += 1
                if mh["counter"] > mh["intervall"]:
                    mh["y"] = random.randint(10, 300)
                    mh["richtung"] = random.choice(("right", "left"))
                    mh["Seite"] = mh["richtung"]
                    mh["x"] = 0 if mh["richtung"] == "right" else 1000
                    mh["counter"] = 0
                    mh["Status"] = "Go"
                continue

            if mh["Status"] == "tot":
                mh["y"] = min(340, mh["y"] + 2)
                if mh["y"] >= 340:
                    mh["Status"] = "Stop"
                    mh["counter"] = 0
                continue

            mh["x"] += 3 if mh["richtung"] == "right" else -3
            if kollidiert_rect(mh, self.sonne_dict, 40, 40, 40, 40):
                print(f"{mh['name']} von Sonne verbrannt")
                mh["Status"] = "tot"
            elif kollidiert_rect(mh, self.marsi, 40, 40, 40, 60):
                print(f"{mh['name']} von Marsi gefressen")
                mh["Status"] = "Stop"
                mh["counter"] = 0
            elif mh["x"] < 0 or mh["x"] > 999:
                mh["Status"] = "Stop"
                mh["counter"] = 0

        # Jedes Paar genau einmal prüfen.
        for i, mh in enumerate(self.moorhuehner):
            if mh["Status"] != "Go":
                continue
            for mh2 in self.moorhuehner[i + 1:]:
                if mh2["Status"] == "Go" and kollidiert_rect(mh, mh2, 40, 40, 40, 40):
                    print(f"{mh['name']} und {mh2['name']} kollidieren und stürzen ab!")
                    mh["Status"] = mh2["Status"] = "tot"
                    break

    def zeichnen(self):
        mars = self.marsi
        if mars["Seite"] == "left":
            mars["obj"].zeichnen(mars["x"], mars["y"], WALK_LEFT)
        elif mars["Seite"] == "right":
            mars["obj"].zeichnen(mars["x"], mars["y"], WALK_RIGHT)
        else:
            setze_bild(mars["obj"].sprite, STANDING, mars["x"], mars["y"])

        for mh in self.moorhuehner:
            if mh["Status"] == "Go":
                frames = HUHN_LEFT if mh["Seite"] == "left" else HUHN_RIGHT
                mh["obj"].zeichnen(mh["x"], mh["y"], frames)
            elif mh["Status"] == "tot":
                mh["obj"].zeichnen(mh["x"], mh["y"], HUHN_TOT)
            else:
                mh["obj"].verstecken()

        xs, ys = sonnenstand()
        self.sonne_dict["x"], self.sonne_dict["y"] = xs, ys
        setze_bild(self.sonne, SONNE, xs, ys)
        text, x, y = check_text(mars["x"], mars["y"])
        self.text_sprite.clear()
        if text:
            self.text_sprite.goto(x - BREITE / 2, HOEHE / 2 - y)
            self.text_sprite.write(text, font=("Comic Sans MS", 20, "normal"))
        screen.update()

    def tick(self):
        if not self.aktiv:
            return
        self.marsi_bewegen()
        self.moorhuehner_bewegen()
        self.zeichnen()
        screen.ontimer(self.tick, TICK_MS)


def main():
    spiel = Spiel()
    screen.onkey(lambda: spiel.taste(-8, 0), "Left")
    screen.onkey(lambda: spiel.taste(8, 0), "Right")
    screen.onkey(lambda: spiel.taste(0, -8), "Up")
    screen.onkey(lambda: spiel.taste(0, 8), "Down")
    screen.onkey(spiel.beenden, "q")
    screen.listen()
    spiel.tick()
    screen.mainloop()


if __name__ == "__main__":
    main()
