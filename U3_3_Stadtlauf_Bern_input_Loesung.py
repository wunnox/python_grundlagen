#! env python3
####################################################
#
# Uebung:
# Fügen Sie im markierten Bereich folgender Code ein:
#
#   - Lesen Sie mit «input» die Anzahl Schritte ein, welche die Figur laufen soll
#   - Fügen Sie im markierten Bereich folgender Code ein:
#
#   - Eine input-Funktion, mit welcher die Anzahl Schritte eingegeben werden kann, welche die Figur laufen soll
#   - Prüfen Sie die Eingabe, bei weniger als 10 Schritten wird er Wert auf 10 gesetzt, bei mehr als 450 Schritten soll er auf 450 gesetzt werden
#   - Verwenden Sie zum Einlesen des Wertes in input die Variable "schritte"
#   - Sobald die Figur beim Zytglogge Turm ankommt, beendet sich das Spiel
#
# Vorhandene Funktionen
#
# go_right()   : Geht einen Schritt nach rechts
# go_left()    : Geht einen Schritt nach links
# go_up()      : Geht einen Schritt hoch
# go_down()    : Geht einen Schritt runter
# Taste q      : Abbruch des Spiels
#
# Hinweis: Neuer Code nur im markierten Feld eintragen
#
####################################################

#Module
import pygame
import time
from stadtlauf_bern_modul import *

#Variablen
schritte=0    #Anzahl Schritte
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur


#Start der Darstellung
while run:
    clock.tick(27)

    #Lauf zu Zytglogge Turm
    for i in range(schritte):
      time.sleep(slower)      #Laufgeschwindigkeit reduzieren
      x=go_right()            #Gehe nach rechts
      if x%10==0 and x<=210:  #Nach jedem 10ten Schritt ein Schritt hoch
         y=go_up()
      elif x%10==0 and x<450: #Nach jedem 10ten Schritt ein Schritt runter
         y=go_down()

      redrawGameWindow()      #Grafik neu darstellen

      if x>450: 
         go_stop()
         redrawGameWindow("Weiter geht's nicht mehr",x,y-15)  #Grafik neu darstellen
         time.sleep(2)
         break

    if x>450: break
    go_stop()
    run=check_key()  #Prüfen ob und welche Taste gedrückt wurde
    redrawGameWindow()  #Grafik neu darstellen

##############################################
    #######################################
    # Hier kommt Ihr Code

    schritte=int(input("Geben Sie die Anzahl Schritte zw. 10 und 450 ein: "))
    if schritte>450:
       schritte=450
    elif schritte<10:
       schritte=10
    
    #bis hier
    #######################################
##############################################

#Ende Darstellung
pygame.quit()
