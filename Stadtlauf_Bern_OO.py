#! env python3
##############################################
#
# Name: Stadtlauf_Bern_OO.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.09.2022
#
# Purpose: Marsi läuft in der Stadt Bern herum
#
##############################################

#Module
import time
import stadtlauf_bern_oo_modul as sf
import stadtlauf_bern_sehenswuerdigkeiten_inventar as sbi
import stadtlauf_bern_wegdaten as wd

run=True
d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur
x=0
y=0

#Figur als Objekt initialisieren
marsi=sf.Figur('Marsi')
starttext=f"{marsi.figur} on the road"

#Funktion
def check_text(x,y):
   sehenswurdigkeit=''
   for s in sbi.sehensw:
      if x in sbi.pos[s][0] and y in sbi.pos[s][1]:
         sehenswurdigkeit=s
   return sehenswurdigkeit,x,y-15

while run:
    sf.clock.tick(27)

    if d>0:
      
       for wg in wd.weg["Käfigturm"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)

       for wg in wd.weg["Zytglogge"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)

       for wg in wd.weg["Rathaus"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)
       for wg in wd.weg["Nydeck Kirche"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)
       
       for wg in wd.weg["Münster"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_left(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)

       for wg in wd.weg["Bundeshaus"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_left(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)
       
       for wg in wd.weg["Heiliggeist Kirche links"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_left(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)
       
       for wg in wd.weg["Heiliggeist Kirche rechts"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          marsi.redrawGameWindow(text2show,xt,yt)
       
    d-=1

    marsi.go_stop()
    run=marsi.check_key()
    marsi.redrawGameWindow(text2show,xt,yt)
