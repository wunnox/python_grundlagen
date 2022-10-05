#! env python3
####################################################
#
# Uebung:
# Geben Sie beim Starten des Scripts das Ziel als Paraemter mit
# Die Figur wird dann bis zu diesem Ziel laufen
# 
# Prüfen Sie, ob ein Parameter eingegeben wurde.
# Wenn nein, erscheint die Meldung: "Es wurde kein Ziel eingegeben!" und das 
# Script bricht mit der Funktion exit() ab
# 
# Wenn ja, schreiben Sie den Parameter in die Variable "ziel"
#
# Gültige Ziele sind die folgenden: 'Käfigturm', 'Zytglogge', 'Bundeshaus', 'Münster', 'Kasino', 'Rathaus', 'Nydeck Kirche'
#
# Wenn Sie noch Zeit haben, können Sie prüfen, ob ein gültiges Ziel eingegeben wurde
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
# Hinweis: Neuer Code nur im markierten Bereich eintragen
#
####################################################

#Module
import time
import sys

##############################################
#######################################
# Hier kommt Ihr Code

#Auswahl festlegen
choises=('Käfigturm','Zytglogge','Bundeshaus','Münster','Kasino','Rathaus','Nydeck Kirche')

#Prüfen, ob und welches Ziel eingegeben wurde
if len(sys.argv )==1:
   print("Es wurde kein Ziel eingegeben!")
   exit()
else:
   ziel=sys.argv[1]
   if ziel not in choises:
      print(f"{ziel} ist ein unbekanntest Ziel!")
      print(f"Wählen Sie eines der folgenden: {choises}")
      exit()
   else:
      print()
      print(f"Wir laufen Richtung {ziel}")
      print()

#bis hier
#######################################
##############################################

#Wir laden diese Module erst, wenn klar ist wo es hin geht!
import pygame
from stadtlauf_bern_modul import *
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd

d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

#Dictionary mit Positionsdaten für Sehenswürdigkeiten
pos={}
pos['Käfigturm']=(200,280,120,150)
pos['Zytglogge']=(410,490,140,160)
pos['Bundeshaus']=(190,240,180,250)
pos['Münster']=(570,725,200,250)
pos['Kasino']=(440,540,230,270)
pos['Rathaus']=(660,750,60,110)
pos['Nydeck Kirche']=(870,950,60,100)

#Funktion
def check_text(x,y):
   ''' Prüfen ob eine Sehenswürdigkeit angezeigt werden soll'''

   text2show,xt,yt='',x,y

   for p in pos.keys():
      if x>pos[p][0] and x<pos[p][1] and y>pos[p][2] and y<pos[p][3]:
         text2show=p
         xt,yt=x,y
         break

   return text2show,xt,yt

#Start Game
while run:
    clock.tick(27)

    if d>0:
       #Lauf zu gewünschtem Ziel
       if "ziel" in globals():
          for wg in wd.weg[ziel]:
             gx,gy=wg
             time.sleep(slower)                #Laufgeschwindigkeit reduzieren
             x,y=go_walk_right(gx,gy)          #Gehe zu Koordinaten nach rechts
             text2show,xt,yt=check_text(x,y)   #Prüfen ob eine Sehenswürdigkeit angezeigt werden soll
             redrawGameWindow(text2show,xt,yt-15) #Grafik neu darstellen
       else:
          text2show="Habe kein Ziel"
          xt,yt=20,150
          redrawGameWindow(text2show,xt,yt)  #Grafik neu darstellen
    d-=1

    go_stop()
    run=check_key()  #Prüfen ob und welche Taste gedrückt wurde

    redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()
