##############################################
#
# Name: stadtlauf_bern_oo_moorhuhn_modul.py
#
# Author: Peter Christen
#
# Version: 2.0
#
# Date: 10.09.2022 V1.0
#       29.03.2026 V2.0 Mit KI Überarbeitet
#
# Purpose: Modul zu Script Stadtlauf_Bern_OO_Moorhuhn.py
#
##############################################

import pygame
import datetime

# Initialisierung
pygame.init()
pygame.display.set_caption("Spaziergang durch Bern")
screen = pygame.display.set_mode((1050, 400))

# Bilder
walkRight = [
    pygame.image.load('Bilder/R1.png'), pygame.image.load('Bilder/R2.png'),
    pygame.image.load('Bilder/R3.png'), pygame.image.load('Bilder/R4.png'),
    pygame.image.load('Bilder/R5.png'), pygame.image.load('Bilder/R6.png'),
    pygame.image.load('Bilder/R7.png'), pygame.image.load('Bilder/R8.png'),
    pygame.image.load('Bilder/R9.png')
]
walkLeft = [
    pygame.image.load('Bilder/L1.png'), pygame.image.load('Bilder/L2.png'),
    pygame.image.load('Bilder/L3.png'), pygame.image.load('Bilder/L4.png'),
    pygame.image.load('Bilder/L5.png'), pygame.image.load('Bilder/L6.png'),
    pygame.image.load('Bilder/L7.png'), pygame.image.load('Bilder/L8.png'),
    pygame.image.load('Bilder/L9.png')
]
huhnLeft = [
    pygame.image.load(
        'Bilder/Lchicken1.png'), pygame.image.load('Bilder/Lchicken2.png'),
    pygame.image.load(
        'Bilder/Lchicken3.png'), pygame.image.load('Bilder/Lchicken4.png'),
    pygame.image.load(
        'Bilder/Lchicken5.png'), pygame.image.load('Bilder/Lchicken6.png'),
    pygame.image.load(
        'Bilder/Lchicken7.png'), pygame.image.load('Bilder/Lchicken8.png'),
    pygame.image.load('Bilder/Lchicken9.png')
]
huhnRight = [
    pygame.image.load(
        'Bilder/Rchicken1.png'), pygame.image.load('Bilder/Rchicken2.png'),
    pygame.image.load(
        'Bilder/Rchicken3.png'), pygame.image.load('Bilder/Rchicken4.png'),
    pygame.image.load(
        'Bilder/Rchicken5.png'), pygame.image.load('Bilder/Rchicken6.png'),
    pygame.image.load(
        'Bilder/Rchicken7.png'), pygame.image.load('Bilder/Rchicken8.png'),
    pygame.image.load('Bilder/Rchicken9.png')
]
huhntot = [
    pygame.image.load(
        'Bilder/chickendead1.png'), pygame.image.load('Bilder/chickendead2.png'),
    pygame.image.load(
        'Bilder/chickendead3.png'), pygame.image.load('Bilder/chickendead4.png'),
    pygame.image.load(
        'Bilder/chickendead5.png'), pygame.image.load('Bilder/chickendead6.png'),
    pygame.image.load(
        'Bilder/chickendead7.png'), pygame.image.load('Bilder/chickendead8.png'),
    pygame.image.load('Bilder/chickendead8.png')
]

bg = pygame.image.load('Bilder/karte-bern_kl.jpg')
char = pygame.image.load('Bilder/standing.png')
sonne = pygame.image.load('Bilder/Sonne2.png')

# Variablen
font = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()
walkCount = 0        # globaler Animationszähler für Marsmenschen
mit_sonnenstand = True


def redrawGameWindow(text2show, xt, yt, marsmenschen, moorhuehner):
    """Baut das Bild neu auf."""
    global screen, walkCount

    textimg = font.render(text2show, True, (255, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(textimg, (xt, yt))

    # Animation-Counter für Marsis begrenzen
    if walkCount >= len(walkRight) * 3:
        walkCount = 0

    # Alle Marsmenschen zeichnen
    for m in marsmenschen:
        if m["Status"] == "Go":
            if m['Seite'] == 'left':
                screen.blit(walkLeft[walkCount // 3], (m['x'], m['y']))
                walkCount += 1
            elif m['Seite'] == 'right':
                screen.blit(walkRight[walkCount // 3], (m['x'], m['y']))
                walkCount += 1
            else:
                screen.blit(char, (m['x'], m['y']))
                walkCount = 0
        else:
            screen.blit(char, (m['x'], m['y']))
            walkCount = 0

    # Alle Moorhühner zeichnen – eigener Animationszähler pro Huhn
    for mh in moorhuehner:
        # Animationszähler initialisieren, falls noch nicht vorhanden
        if "anim" not in mh:
            mh["anim"] = 0

        # Für die verschiedenen Status unterschiedliche Frame-Listen verwenden
        if mh["Status"] == 'Go':
            # Begrenzen, damit der Index nie aus der Liste läuft
            if mh["anim"] >= len(huhnLeft) * 3:
                mh["anim"] = 0

            if mh["Seite"] == 'left':
                frame = huhnLeft[mh["anim"] // 3]
                screen.blit(frame, (mh["x"], mh["y"]))
                mh["anim"] += 1
            elif mh["Seite"] == 'right':
                frame = huhnRight[mh["anim"] // 3]
                screen.blit(frame, (mh["x"], mh["y"]))
                mh["anim"] += 1

        elif mh["Status"] == 'tot':
            if mh["anim"] >= len(huhntot) * 3:
                mh["anim"] = 0
            frame = huhntot[mh["anim"] // 3]
            screen.blit(frame, (mh["x"], mh["y"]))
            mh["anim"] += 1
        else:
            # Status 'Stop' – nichts animieren
            mh["anim"] = 0

    xs, ys = 0, 0
    if mit_sonnenstand:
        xs, ys = sonnenstand()
        screen.blit(sonne, (xs, ys))

    pygame.display.update()
    return xs, ys


def sonnenstand():
    """Errechnet den Sonnenstand anhand der aktuellen Zeit."""
    heute = datetime.datetime.now()
    stunde = int(heute.strftime("%H"))
    minute = int(heute.strftime("%M"))
    x = 1100
    y = 400
    if stunde > 6:
        x = x - (100 * (stunde - 6)) - (minute * 1.66)
    if 6 < stunde <= 12:
        y = y - (30 * (stunde - 6)) - (minute * 0.5)
    else:
        y = y - (30 * (18 - stunde)) - (minute * 0.5)

    return int(x), int(y)


class Figur:
    """Klasse zum Verwalten der Spielfigur."""

    def __init__(self, figur, width=40, height=60):
        self.figur = figur      # Name / Key
        self.x = 20             # Position x
        self.y = 150            # Position y
        self.max_x = 1000       # Max Position x
        self.max_y = 340        # Max Position y
        self.min_x = -10        # Min Position x
        self.min_y = -10        # Min Position y
        self.seite = "Stop"     # Ausgangsposition Figur
        self.width = width
        self.height = height

    def go_walk_right(self, x, y):
        """Läuft nach einem vorgegebenen Plan nach rechts."""
        self.x, self.y = x, y
        self.seite = "right"
        return self.x, self.y, self.seite

    def go_walk_left(self, x, y):
        """Läuft nach einem vorgegebenen Plan nach links."""
        self.x, self.y = x, y
        self.seite = "left"
        return self.x, self.y, self.seite

    def go_left(self, x, steps=1):
        """Nach links gehen."""
        self.x = x
        if self.x > self.min_x:
            self.x -= steps
            self.seite = "left"
        else:
            self.go_stop()
        return self.x, self.seite

    def go_right(self, x, steps=1):
        """Nach rechts gehen."""
        self.x = x
        if self.x < self.max_x:
            self.x += steps
            self.seite = "right"
        else:
            self.go_stop()
        return self.x, self.seite

    def go_stop(self):
        """Bewegung stoppen."""
        self.seite = "stop"
        global walkCount
        walkCount = 0
        return walkCount, self.seite

    def go_up(self, y, steps=1):
        """Nach oben gehen."""
        self.y = y
        if self.y > self.min_y:
            self.y -= steps
        else:
            self.go_stop()
        return self.y

    def go_down(self, y, steps=1):
        """Nach unten gehen."""
        self.y = y
        if self.y < self.max_y:
            self.y += steps
        else:
            self.go_stop()
        return self.y

    def rect(self):
        """Gibt ein pygame.Rect der Figur zurück."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides_with(self, other):
        """Kollision mit anderer Figur basierend auf Rect."""
        return self.rect().colliderect(other.rect())

    def check_key(self):
        """Prüfen welche Taste gedrückt wurde."""
        run = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.go_right(self.x, 1)
        elif keys[pygame.K_LEFT]:
            self.go_left(self.x, 1)

        if keys[pygame.K_UP]:
            self.go_up(self.y, 1)
        elif keys[pygame.K_DOWN]:
            self.go_down(self.y, 1)

        if keys[pygame.K_q]:
            run = False

        return self.x, self.y, self.seite, run
