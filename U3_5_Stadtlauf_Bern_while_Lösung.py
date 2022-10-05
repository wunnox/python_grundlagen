#! env python3
####################################################
#
# Uebung:
# Erweitern Sie das Programm so, dass die Figur bis zur Gerechtigkeitsgasse läuft.
#
# Verwenden Sie hierfür eine while-Schleife
# Die Gerechtigkeitsgasse beginnt an der x-Position 670
#
# Vorhandene Funktionen
#
# go_right()   : Geht einen Schritt nach rechts
# go_left()    : Geht einen Schritt nach links
# go_up()      : Geht einen Schritt hoch
# go_down()    : Geht einen Schritt runter
# Taste q      : Abbruch des Spiels
#
# Hinweis: Neuer Code nur im markierten Bereich eintragen
#
####################################################

#Module
import pygame
import time
from stadtlauf_bern_modul import *

d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

while run:
    clock.tick(27)
    if d>0:

       #Lauf zu Zytglogge Turm
       for i in range(440):
         time.sleep(slower)  #Laufgeschwindigkeit reduzieren
         x=go_right()
         if x%10==0 and x<=210:
            y=go_up()
         elif x%10==0 and x<450:
            y=go_down()
         redrawGameWindow()  #Grafik neu darstellen

##############################################
       #######################################
       # Hier kommt Ihr Code (ab diesem Einzug)
       #Lauf zu Gerechtigkeitsgasse

       while x<670:
         time.sleep(slower)  #Laufgeschwindigkeit reduzieren
         x=go_right()
         redrawGameWindow()  #Grafik neu darstellen

       #bis hier
       #######################################
##############################################

    d-=1
    go_stop()
    run=check_key()  #Prüfen ob und welche Taste gedrückt wurde
    redrawGameWindow()  #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()

