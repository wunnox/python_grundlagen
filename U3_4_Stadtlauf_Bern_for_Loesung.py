#! env python3
####################################################
#
# Uebung:
# Fügen Sie im markierten Bereich folgenden Code ein:
#
#   - Lassen Sie die Figur mit einer for-Schleife bis zum Käfigturm laufen
#   - Bei jedem 10ten Schritt soll sie einen Schritt nach oben machen
#   - Reduzieren Sie die Laufgeschwindigkeit mit: time.sleep(slower)
#   - Bis zum Käfigturm sind es 210 Schritte
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

#Variablen
schritte=0    #Anzahl Schritte
d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

#Start der Darstellung
while run:
    clock.tick(27)
    if d>0:

##############################################
       #######################################
       # Hier kommt Ihr Code (ab diesem Einzug)
       #Lauf zu Käfigturm

       for i in range(210):
          time.sleep(slower)      #Laufgeschwindigkeit reduzieren
          x=go_right()            #Gehe ein Schritt nach rechts
          if x%10==0:             #Nach jedem 10ten Schritt ein Schritt hoch
             y=go_up()
         
          redrawGameWindow()      #Grafik neu darstellen. Dies muss die letzte Zeile der for-Schleife sein
       #bis hier
       #######################################
##############################################

    d-=1
    go_stop()
    run=check_key()      #Prüfen ob und welche Taste gedrückt wurde
    redrawGameWindow()   #Grafik neu darstellen

#Ende Darstellung
pygame.quit()
