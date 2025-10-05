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
walkCount = 0
left = False
right = False


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
          x,y,left,right=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)

       for wg in wd.weg["Zytglogge"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y,left,right=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)

       for wg in wd.weg["Rathaus"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y,left,right=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)
       for wg in wd.weg["Nydeck Kirche"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y,left,right=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)
       
       for wg in wd.weg["Münster"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y,left,right=marsi.go_walk_left(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)

       for wg in wd.weg["Bundeshaus"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y,left,right=marsi.go_walk_left(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)
       
       for wg in wd.weg["Heiliggeist Kirche links"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y,left,right=marsi.go_walk_left(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)
       
       for wg in wd.weg["Heiliggeist Kirche rechts"]:
          gx,gy=wg
          time.sleep(slower)  #Laufgeschwindigkeit reduzieren
          x,y,left,right=marsi.go_walk_right(gx,gy)
          text2show,xt,yt=check_text(x,y)
          sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)
       
    d-=1

    walkCount,left,right=marsi.go_stop()
    x,y,left,right,run=marsi.check_key()
    sf.redrawGameWindow(text2show,xt,yt,x,y,left,right)

