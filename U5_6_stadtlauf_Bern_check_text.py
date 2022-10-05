#! env python3
##############################################
#
# Name: U5_6_stadtlauf_Bern_check_text.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.09.2022
#
# Purpose: Modul mit den passenden Texten pro Position
#
##############################################

#Dictionary mit Positionsdaten für Sehenswürdigkeiten
pos={}
pos['Käfigturm']=(200,280,120,150)
pos['Zytglogge']=(410,490,140,160)
pos['Bundeshaus']=(190,240,180,210)
pos['Münster']=(570,725,200,250)
pos['Kasino']=(440,540,230,270)
pos['Rathaus']=(660,750,60,110)
pos['Nydeck Kirche']=(870,950,60,100)

#Funktion
def check_text(x,y):
   ''' Prüfen ob ein Text angezeigt werden soll'''

   text2show,xt,yt='',x,y

   for p in pos.keys():
      if x>pos[p][0] and x<pos[p][1] and y>pos[p][2] and y<pos[p][3]:
         text2show=p
         xt,yt=x,y
         break

   return text2show,xt,yt

