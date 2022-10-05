#! env python3
####################################################
#
# Uebung:
# Öffnen Sie die Datei mit den aufgezeichneten Wegdaten
# Lesen Sie die Wegdaten ein und lassen Sie die Figur
# den aufgezeichneten Weg noch einmal ablaufen.
# 
# Vorhandene Funktionen
#
# go_right()   : Geht einen Schritt nach rechts
# go_left()    : Geht einen Schritt nach links
# go_up()      : Geht einen Schritt hoch
# go_down()    : Geht einen Schritt runter
# go_walk_right(x,y): Läuft zur Position x,y nach rechts
# go_walk_left(x,y) : Läuft zur Position x,y nach links
# Taste q      : Abbruch des Spiels
#
# Hinweis: 
#
####################################################

#Module
import pygame
import time
import stadtlauf_bern_oo_modul as sf
from U5_6_stadtlauf_Bern_check_text import check_text

run=True
d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur
x=0
y=0
left=None
right=None

#Figur als Objekt initialisieren
marsi=sf.Figur('Marsi')

##############################################
#######################################
# Hier kommt Ihr Code
# Wegdaten aus Datei einlesen



#bis hier
#######################################
##############################################

while run:
    sf.clock.tick(27)

    if d>0:

##############################################
       #######################################
       # Hier kommt Ihr Code
       # Wegdaten abschreiten







          text2show,xt,yt=check_text(x,y)       #Prüfen ob ein Text angezeigt werden soll
          sf.redrawGameWindow(text2show,xt,yt-15,x,y,left,right)  #Grafik neu darstellen

       #bis hier
       #######################################
##############################################

    d-=1

    x,y,left,right,run=marsi.check_key()  #Prüfen ob und welche Taste gedrückt wurde
    sf.redrawGameWindow(text2show,xt,yt-15,x,y,left,right)  #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()
