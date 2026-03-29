##############################################
#
# Name: Stadtlauf_Bern_OO_Moorhuhn.py
#
# Author: Peter Christen
#
# Version: 2.0
#
# Date: 10.09.2022 V1.0
#       29.03.2026 V2.0 Mit KI überarbeitet
#
# Purpose: Marsi läuft in der Stadt Bern herum, mehrere Moorhühner fliegen umher
#
##############################################

# Module
import time
import random
import stadtlauf_bern_oo_moorhuhn_modul as sf
import stadtlauf_bern_sehenswuerdigkeiten_inventar as sbi
import stadtlauf_bern_wegpunkte as wp

# Konfiguration
SLOWER = 0.005              # Je höher die Zahl, umso langsamer läuft die Figur
ANZAHL_MOORHUEHNER = 3      # Anzahl Moorhühner
MOORHUHN_INTERVALL = 50     # Ticks bis zum nächsten Start eines Moorhuhns

# Globale Variablen
run = True
wege = {}

# Hilfsfunktionen


def kollidiert_rect(a, b, width_a=40, height_a=60, width_b=40, height_b=60):
    """Einfache Rechteck-Kollision zwischen zwei Dicts mit x,y."""
    ax1, ay1 = a['x'], a['y']
    ax2, ay2 = ax1 + width_a, ay1 + height_a
    bx1, by1 = b['x'], b['y']
    bx2, by2 = bx1 + width_b, by1 + height_b

    if ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2:
        return False
    return True


def check_text(x, y):
    """Prüft ob eine Sehenswürdigkeit in der Nähe ist."""
    sehenswurdigkeit = ''
    for s in sbi.sehensw:
        if x in sbi.pos[s][0] and y in sbi.pos[s][1]:
            sehenswurdigkeit = s
    return sehenswurdigkeit, x, y - 15


def walk_generator(weg):
    """Schrittgenerator."""
    schritte = len(weg)
    s = 0
    while s < schritte:
        yield s
        s += 1


def wege_analysieren():
    """Die möglichen Wege an einer Position aufführen."""
    for k in wp.wegpunkt.keys():
        l = k.split('-')
        if l[0] in wege.keys():
            wege[l[0]].append(l)
        else:
            wege[l[0]] = [l]


def neues_ziel_definieren(start):
    """Ziel ab Startpunkt definieren."""
    zufall = random.randint(0, len(wege[start]) - 1)
    start, ende = wege[start][zufall]
    strecke = start + "-" + ende
    return strecke, ende


# Wege vorbereiten
wege_analysieren()

# Erste Strecke definieren
strecke, ende = neues_ziel_definieren('Bahnhofplatz')
schritt = walk_generator(wp.wegpunkt[strecke])

# Figuren als Objekte initialisieren
# Marsmenschen als Liste (aktuell nur einer)
marsmenschen = []
marsi = sf.Figur('Marsi')
marsmenschen.append({
    "name": "Marsi0",
    "obj": marsi,
    "Status": "Go",
    "x": 20,
    "y": 150,
    "Seite": "Stop"
})

# Mehrere Moorhühner
moorhuehner = []
for i in range(ANZAHL_MOORHUEHNER):
    moori = sf.Figur(f"Moori{i}")
    moorhuehner.append({
        "name": f"Moorhuhn{i}",
        "obj": moori,
        "Status": "Stop",
        "x": 1000,
        "y": 20,
        "Seite": "Stop",
        "intervall": MOORHUHN_INTERVALL,
        "counter": random.randint(0, MOORHUHN_INTERVALL),
        "richtung": "right"
    })

# Sonne als eigene "Figur" (für Kollision)
sonne_dict = {"x": 0, "y": 0}


# Hauptschleife
while run:
    sf.clock.tick(27)
    time.sleep(SLOWER)  # Laufgeschwindigkeit reduzieren

    # Marsmenschen bewegen sich entlang der Strecke (für Beispiel nur marsmenschen[0])
    akt_mars = marsmenschen[0]
    try:
        schr = next(schritt)
        gx, gy, links, rechts = wp.wegpunkt[strecke][schr]
        if links:
            akt_mars['x'], akt_mars['y'], akt_mars['Seite'] = akt_mars['obj'].go_walk_left(
                gx, gy)
        else:
            akt_mars['x'], akt_mars['y'], akt_mars['Seite'] = akt_mars['obj'].go_walk_right(
                gx, gy)
    except StopIteration:
        strecke, ende = neues_ziel_definieren(ende)
        schritt = walk_generator(wp.wegpunkt[strecke])
        print(f"Laufe Strecke {strecke}")

    # Zusätzlich Tastatursteuerung für Marsi (nur erster Marsmensch)
    akt_mars['x'], akt_mars['y'], akt_mars['Seite'], run = akt_mars['obj'].check_key()

    # Koordinaten im Dict aktuell halten
    akt_mars['obj'].x = akt_mars['x']
    akt_mars['obj'].y = akt_mars['y']

    # Moorhühner bewegen
    for mh in moorhuehner:
        # Referenz auf Marsi für Kollision
        mars_dict = {
            "x": akt_mars['x'],
            "y": akt_mars['y']
        }

        if mh['counter'] > mh['intervall']:
            # Neues Moorhuhn starten
            mh['y'] = random.randint(10, 300)
            mh['richtung'] = random.choice(("right", "left"))
            mh['x'] = 0 if mh['richtung'] == "right" else 1000
            mh['counter'] = 0
            mh['Status'] = "Go"

        elif mh['Status'] == "Go":
            # In welche Richtung soll es gehen
            if mh['richtung'] == "right":
                mh['x'], mh['Seite'] = mh['obj'].go_right(mh['x'], 3)
            else:
                mh['x'], mh['Seite'] = mh['obj'].go_left(mh['x'], 3)

            # Ist das Moorhuhn in der Nähe der Sonne?
            if kollidiert_rect({"x": mh['x'], "y": mh['y']},
                               {"x": sonne_dict['x'], "y": sonne_dict['y']},
                               width_a=40, height_a=40,
                               width_b=40, height_b=40):
                print(
                    f"{mh['name']} von Sonne verbrannt, xh:{mh['x']}, yh:{mh['y']}")
                mh['Status'] = 'tot'

            # Ist das Moorhuhn in der Nähe eines Marsmenschen?
            if kollidiert_rect({"x": mh['x'], "y": mh['y']},
                               mars_dict,
                               width_a=40, height_a=40,
                               width_b=40, height_b=60):
                print(
                    f"{mh['name']} von Marsi gefressen, xh:{mh['x']}, xm:{mars_dict['x']}, yh:{mh['y']}, ym:{mars_dict['y']}")
                mh['Status'] = 'Stop'
                mh['counter'] = 0

            # Kollision mit anderen Moorhühnern (abstürzen lassen)
            for mh2 in moorhuehner:
                if mh2 is mh:
                    continue
                if mh2['Status'] == "Go":
                    if kollidiert_rect(
                        {"x": mh['x'], "y": mh['y']},
                        {"x": mh2['x'], "y": mh2['y']},
                        width_a=40, height_a=40,
                        width_b=40, height_b=40
                    ):
                        print(
                            f"{mh['name']} und {mh2['name']} kollidieren und stürzen ab!")
                        mh['Status'] = 'tot'
                        mh2['Status'] = 'tot'

            # Ist das Moorhuhn am Bildende?
            if mh['x'] < 0 or mh['x'] > 999:
                mh['counter'] = 0
                mh['Status'] = 'Stop'

        elif mh['Status'] == "tot":
            mh['y'] = mh['obj'].go_down(mh['y'], 2)
            if mh['y'] >= 340:
                mh['counter'] = 0
                mh['Status'] = 'Stop'
        else:
            # Warten bis zum nächsten Start
            mh['counter'] += 1

    # Text auswählen, der angezeigt werden soll (für akt_mars)
    text2show, xt, yt = check_text(akt_mars['x'], akt_mars['y'])

    # Bild neu aufbauen, inkl. Sonne und aller Figuren
    # xs, ys zurückgeben und im sonne_dict aktualisieren
    xs, ys = sf.redrawGameWindow(
        text2show,
        xt,
        yt,
        marsmenschen=marsmenschen,
        moorhuehner=moorhuehner
    )
    sonne_dict['x'], sonne_dict['y'] = xs, ys
