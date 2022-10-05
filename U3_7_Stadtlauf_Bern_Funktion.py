#! env python3
####################################################
#
# Uebung:
# Erstellen Sie eine Funktion mit dem Namen "check_text"
# Verschieben Sie die Prüfung, ob eine Sehenswürdigkeit angezeigt werden soll in diese Funktion
# Anschliessend rufen Sie zur Prüfung nur noch diese Funktion auf
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

##############################################
#######################################
# Hier kommt Ihre Funktion hin




#bis hier
#######################################
##############################################

while run:
    clock.tick(27)
    if d>0:

       #Lauf zu Zytglogge Turm
       for i in range(450):
         time.sleep(slower)  #Laufgeschwindigkeit reduzieren
         x=go_right()
         if x%10==0 and x<=210:
            y=go_up()
         elif x%10==0 and x<450:
            y=go_down()

         #Prüfen ob eine Sehenswürdigkeit angezeigt werden soll
         if x>200 and x<280 and y>120 and y<150:
            text2show='Käfigturm'
            xt,yt=x,y
         elif x>410 and x<490 and y>140 and y<160:
            text2show='Zytglogge'
            xt,yt=x,y

         redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen

    d-=1
    go_stop()
    run=check_key()  #Prüfen ob und welche Taste gedrückt wurde
    redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()

