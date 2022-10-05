#! env python3
####################################################
#
# Uebung:
# Verlegen Sie die Funktion check_text in eine eigene Datei
# Importieren Sie diese anschliessend als Modul
# 
# Benennen Sie die neue Datei: U5_6_Stadtlauf_Bern_check_text.py 
#
####################################################

#Module
import pygame
import time
from stadtlauf_bern_modul import *
import stadtlauf_bern_sehenswuerdigkeiten_inventar as sbi

d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

#Funktion
def check_text(x,y):
   '''Prüft welche Sehenswürdigkeit angezeigt werden soll'''

   sehenswurdigkeit=''
   for s in sbi.sehensw:
      if x in sbi.pos[s][0] and y in sbi.pos[s][1]:
         sehenswurdigkeit=s
   return sehenswurdigkeit,x,y-15

while run:
    clock.tick(27)

    if d>0:
       #Lauf zu Zytglogge
       for i in range(440):
         time.sleep(slower)                      #Laufgeschwindigkeit reduzieren
         x=go_right()                            #Gehe einen Schritt nach rechts
         if x%10==0 and x<210:                   #Nach jedem 10ten Schritt ein Schritt hoch
            y=go_up()
         elif x%10==0 and x<450:                 #Nach jedem 10ten Schritt ein Schritt runter
            y=go_down()
         text2show,xt,yt=check_text(x,y)         #Prüfen, ob eine Sehenswürdigkeit angezeigt werden soll
         redrawGameWindow(text2show,xt,yt-15)    #Grafik neu darstellen

       #Lauf wieder zurück 
       for i in range(470):
         time.sleep(slower)                     #Laufgeschwindigkeit reduzieren
         x=go_left()                            #Gehe einen Schritt nach links
         if x==None: x=0
         if x<450 and x>420:                    #Nach jedem 10ten Schritt ein Schritt runter
            y=go_down()
         elif x<140 and x>13 and x%10==0:       #Nach jedem 10ten Schritt ein Schritt runter
            y=go_down()
         elif x<16:
            y=go_up(2)
         text2show,xt,yt=check_text(x,y)        #Prüfen, ob eine Sehenswürdigkeit angezeigt werden soll
         redrawGameWindow(text2show,xt,yt-15)   #Grafik neu darstellen
    d-=1

    go_stop()                                   #Stehen bleiben
    run=check_key()                             #Prüfen ob und welche Taste gedrückt wurde
    redrawGameWindow(text2show,xt,yt-15)        #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()
