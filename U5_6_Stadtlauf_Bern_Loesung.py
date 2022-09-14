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

import pygame
import time
from stadtlauf_func import *
from U5_6_Stadtlauf_Bern_check_text import check_text

d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur

while run:
    clock.tick(27)

    if d>0:
       #Lauf zu Zytglogge
       for i in range(440):
         time.sleep(slower)
         x=go_right()
         if x%10==0 and x<260:
            y=go_up()
         elif x%10==0 and x<450:
            y=go_down()
         text2show,xt,yt=check_text(x,y)
         redrawGameWindow(text2show,xt,yt)

       #Lauf wieder zurück
       for i in range(470):
         time.sleep(slower)
         x=go_left()
         if x==None: x=0
         if x<440 and x>420:
            y=go_down(2)
         elif x<100 and x>13 and x%10==0:
            y=go_down()
         elif x<16:
            y=go_up(2)
         text2show,xt,yt=check_text(x,y)
         redrawGameWindow(text2show,xt,yt)
    d-=1

    go_stop()
    text2show=None
    run=check_key()

    redrawGameWindow(text2show,xt,yt) 
    
pygame.quit()
