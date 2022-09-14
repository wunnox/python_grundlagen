#! env python3
####################################################
#
# Uebung:
# Erweitern Sie das Programm so, dass die Figur bis zum Zytglogge Turm läuft.
#
# Achten Sie darauf, dass sie auf der Marktgasse bleibt und nicht in die Häuser läuft.
# Wenn sie beim Zytglogge Turm ankommt, soll die entsprechende Bezeichnung des Turms "Zytglogge" erscheinen.
#
# Vorhandene Funktionen
#
# go_right()   : Geht einen Schritt nach rechts
# go_left()    : Geht einen Schritt nach links
# go_up()      : Geht einen Schritt hoch
# go_down()    : Geht einen Schritt runter
#
# Hinweis: Neuer Code nur im markierten Feld eintragen
#          Der Zytglogge Turm ist an der x,y-Position 430,180
#
####################################################

#Module
import pygame
import time
from stadtlauf_func import *

#Variablen
d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

#Start der Darstellung
while run:
    clock.tick(27)
    if d>0:

##############################################
       #######################################
       # Hier kommt Ihr Code

       for i in range(230):
         time.sleep(slower)
         x=go_right()
         if x%10==0 and x<=210:
            y=go_up()
         if x>200 and x<250 and y>150 and y<170:
            text2show='Käfigturm'
            xt,yt=x,y
         redrawGameWindow(text2show,xt,yt)

       #bis hier
       #######################################
##############################################

    d-=1
    go_stop()
    run=check_key()
    redrawGameWindow(text2show,xt,yt) 
    
#Ende Darstellung
pygame.quit()
