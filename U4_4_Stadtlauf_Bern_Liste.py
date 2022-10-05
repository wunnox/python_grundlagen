#! env python3
####################################################
#
# Uebung:
# Im untenstehnden Code läuft die Figur zum Zytgloggen Turm
#
# Zeichnen Sie den Weg, welchen die Figur läuft, in einer Liste auf, damit dieser Weg
# anhand dieser Daten noch einmal abgelaufen werden kann.
# Erfassen Sie die einzelnen x,y-Koordinaten in einer Subliste
#
# Geben Sie den Inhalt der Liste am Ende des Scripts auf dem Bildschirm aus 
#
# Vorhandene Funktionen
#
# go_right()   : Geht einen Schritt nach rechts
# go_left()    : Geht einen Schritt nach links
# go_up()      : Geht einen Schritt hoch
# go_down()    : Geht einen Schritt runter
# Taste q      : Abbruch des Spiels
#
# Hinweis: Neuer Code nur in den markierten Bereichen eintragen
#          Achtung, der Code muss hier in drei Bereichen erfasst werden
#
####################################################

#Module
import pygame
import time
from stadtlauf_bern_modul import *

d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

def check_text(x,y):
   ''' Prüfen ob eine Sehenswürdigkeit angezeigt werden soll'''

   if x>200 and x<280 and y>120 and y<150:
      text2show='Käfigturm'
      xt,yt=x,y
   elif x>410 and x<490 and y>140 and y<160:
      text2show='Zytglogge'
      xt,yt=x,y
   else:
      text2show,xt,yt='',x,y

   return text2show,xt,yt

##############################################
#######################################
# Hier kommt Ihr Code
# Liste "weg" für Wegdaten erstellen


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
         text2show,xt,yt=check_text(x,y)  #Prüfen ob eine Sehenswürdigkeit angezeigt werden soll

         redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen

##############################################
         #####################################
         # Hier kommt Ihr Code
         # Liste mit Wegdaten abfüllen


         #bis hier
         #####################################
##############################################

    d-=1
    go_stop()
    run=check_key()  #Prüfen ob und welche Taste gedrückt wurde
    redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()

##############################################
#######################################
# Hier kommt Ihr Code
# Wegdaten ausgeben


#bis hier
#######################################
##############################################
