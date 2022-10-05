#! env python3
####################################################
#
# Uebung:
# Öffnen Sie eine Datei zum Beschreiben
# Bewegen Sie anschliessend die Figur mit den Pfeiltasten durch die Stadt
# Bei jedem Schritt der Figur sollen die Wegdaten in die Datei geschrieben werden
# Wenn die Figur steht, sollen keine Daten geschrieben werden
# Am Ende soll die Datei wieder geschlossen werden
#
# Die Idee ist, dass Sie die Daten in dieser Datei verwenden können, um denselben
# Weg noch einmal abzulaufen
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

#Figur als Objekt initialisieren
marsi=sf.Figur('Marsi')

##############################################
#######################################
# Hier kommt Ihr Code
# Datei zum Beschreiben öffnen

w=open('Wegdaten_OO.txt','w')
x1=0
y1=0

#bis hier
#######################################
##############################################

while run:
    sf.clock.tick(27)
    x,y,left,right,run=marsi.check_key()  #Prüfen ob und welche Taste gedrückt wurde
    text2show,xt,yt=check_text(x,y)
    sf.redrawGameWindow(text2show,xt,yt-15,x,y,left,right)  #Grafik neu darstellen

##############################################
    #######################################
    # Hier kommt Ihr Code
    # Datei mit Wegdaten beschreiben

    if x!=x1 or y!=y1:
       wg=str(x)+":"+str(y)+":"+str(left)+":"+str(right)+"\n"
       w.write(wg)
       x1,y1=x,y

    #bis hier
    #######################################
##############################################
    
#Ende Darstellung
pygame.quit()

##############################################
#######################################
# Hier kommt Ihr Code
# Datei schliessen

w.close()

#bis hier
#######################################
##############################################
