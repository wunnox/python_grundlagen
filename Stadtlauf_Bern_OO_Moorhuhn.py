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
import random
import stadtlauf_bern_oo_moorhuhn_modul as sf
import stadtlauf_bern_sehenswuerdigkeiten_inventar as sbi
import stadtlauf_bern_wegpunkte as wp

#Variablen
run=True
slower=0.005   #Je höher die Zahl, umso langsamer läuft die Figur
wege={}

moorhuhn={"Status":"Stop","x":1000,"y":20,"Seite":"Stop",'intervall':50,'counter':0}
marsmensch={"Status":"Go","x":20,"y":150,"Seite":"Stop"}

#Figur als Objekt initialisieren
marsi=sf.Figur('Marsi')
moori=sf.Figur('Moori')

#Funktion
def check_text(x,y):
   '''Prüft ob eine Sehenswürdigkeit in der Nähe ist'''

   sehenswurdigkeit=''
   for s in sbi.sehensw:
      if x in sbi.pos[s][0] and y in sbi.pos[s][1]:
         sehenswurdigkeit=s
   return sehenswurdigkeit,x,y-15

def walk_generator(weg):
   '''Schrittgenerator'''

   schritte=len(weg)
   s=0

   while s<=schritte:
      yield s
      s+=1

def wege_analysieren():
   '''Die möglichen Wege an einer Position aufführen'''

   for k in wp.wegpunkt.keys():
      l=k.split('-')
      if l[0] in wege.keys():
         wege[l[0]].append(l)
      else:
         wege[l[0]]=[l]

def neues_ziel_definieren(start):
   '''Ziel ab Startpunkt definieren'''

   zufall=random.randint(0,3)
   start,ende=wege[start][zufall]
   strecke=start+"-"+ende

   return strecke,ende   

wege_analysieren()

#Erste Strecke definieren
strecke,ende=neues_ziel_definieren('Bahnhofplatz')
schritt=walk_generator(wp.wegpunkt[strecke])

while run:
    sf.clock.tick(27)
    time.sleep(slower)  #Laufgeschwindigkeit reduzieren

    if moorhuhn['counter'] > moorhuhn['intervall']:
       moorhuhn['y']=random.randint(10,300)
       dire=random.choice(("right","left"))
       if dire=="right": moorhuhn['x']=0
       else: moorhuhn['x']=1000
       moorhuhn['counter']=0
       moorhuhn['Status']="Go"
    elif moorhuhn['Status']=="Go":
          #In welche Richtung soll es gehen
          if dire=="right":
             moorhuhn['x'],moorhuhn['Seite']=moori.go_right(moorhuhn['x'],3)
          else:
             moorhuhn['x'],moorhuhn['Seite']=moori.go_left(moorhuhn['x'],3)
          #Ist das Moorhuhn in der Nähe der Sonne
          if moorhuhn['x'] <= xs+10 and moorhuhn['x'] >= xs-10 and moorhuhn['y'] <= ys+15 and moorhuhn['y'] >= ys-60: 
             print(f"Mohrhuhn tot, xh:{moorhuhn['x']},xs:{xs},yh:{moorhuhn['y']},ys:{ys}")
             moorhuhn['Status']='tot'
          #Ist das Moorhuhn in der Nähe von Marsi
          if moorhuhn['x'] <= marsmensch['x']+10 and moorhuhn['x'] >= marsmensch['x']-10 and moorhuhn['y'] <= marsmensch['y']+15 and moorhuhn['y'] >= marsmensch['y']-60: 
             print(f"Mohrhuhn gefressen, xh:{moorhuhn['x']},xm:{moorhuhn['x']},yh:{moorhuhn['y']},ym:{marsmensch['y']}")
             moorhuhn['Status']='Stop'
          #Ist das Moorhuhn am Bild Ende
          if moorhuhn['x']<0 or moorhuhn['x']>999:
             moorhuhn['counter']=0
             moorhuhn['Status']='Stop'
    elif moorhuhn['Status']=="tot":
          moorhuhn['y']=moori.go_down(moorhuhn['y'],2)
          if moorhuhn['y'] >= 340:
             moorhuhn['counter']=0
             moorhuhn['Status']='Stop'
    else:
       moorhuhn['counter']+=1

    #Marsi läuft seine Strecke ab
    try:
       schr=next(schritt)
       gx,gy,links,rechts=wp.wegpunkt[strecke][schr]
       if links:
          marsmensch['x'],marsmensch['y'],marsmensch['Seite']=marsi.go_walk_left(gx,gy)
       else:
          marsmensch['x'],marsmensch['y'],marsmensch['Seite']=marsi.go_walk_right(gx,gy)
    except:
       strecke,ende=neues_ziel_definieren(ende)
       schritt=walk_generator(wp.wegpunkt[strecke])
       print(f"Laufe Strecke {strecke}")

    #Prüfen welche Taste gedrückt wurde
    marsmensch['x'],marsmensch['y'],marsmensch['Seite'],run=marsi.check_key()
    #Text auswählen, der angezeigt werden soll
    text2show,xt,yt=check_text(marsmensch['x'],marsmensch['y'])
    #Bild neu aufbauen
    xs,ys=sf.redrawGameWindow(text2show,xt,yt,marsmensch,moorhuhn)

