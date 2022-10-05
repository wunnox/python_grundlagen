#! env python3
####################################################
#
# Uebung:
# Verlegen Sie die Funktion check_text in eine eigene Datei
# Importieren Sie diese anschliessend als Modul
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
# Hinweis: Benennen Sie die neue Datei: U5_6_stadtlauf_Bern_check_text.py
#
####################################################

#Module
import pygame
import time
from stadtlauf_bern_modul import *
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd

##############################################
#######################################
# Hier kommt Ihr neuer Code

from U5_6_stadtlauf_Bern_check_text import check_text

#bis hier
#######################################
##############################################

d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

while run:
    clock.tick(27)

    if d>0:
       for wg in wd.weg['Zytglogge']:
         gx,gy=wg
         time.sleep(slower)  #Laufgeschwindigkeit reduzieren
         x,y=go_walk_right(gx,gy)

         text2show,xt,yt=check_text(x,y)       #Prüfen ob eine Sehenswürdigkeit angezeigt werden soll
         redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen
    d-=1

    go_stop()
    run=check_key()  #Prüfen ob und welche Taste gedrückt wurde

    redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()
