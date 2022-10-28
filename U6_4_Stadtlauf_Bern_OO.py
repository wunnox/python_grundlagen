#! env python3
####################################################
#
# Uebung:
# Der Berner Stadtlauf wurde Objekt Orientiert programmiert
# Das heisst somit folgendes:
#   - Es gibt eine Klasse Figur (aufrufen mit sf.Figur), in welcher die Figuren, welche durch die Stadt laufen, als Objekt erfasst werden können
#   - Alle vorhandenen Funktionen wurden als Methoden in die Klasse Figur übernommen. Beachten Sie die Hinweise bei den Eingabeblöcken..
#
# Erfassen Sie somit ein neues Objekt mit einen Namen für die Figur Ihrer Wahl
# Lassen Sie Ihr Objekt(Figur) den vorgegebenen Weg zum Zytglogge ablaufen
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
# Hinweis: In jedem der drei Codeblöcke braucht es jeweils nur eine Zeile
#          Die Methoden der Klasse "Figur" geben nicht nur die Werte
#          x und y zurück sondern auch die Bool-Werte von "left" und "right"
#
####################################################

#Module
import pygame
import time
import stadtlauf_bern_oo_modul as sf
import U5_5_stadtlauf_Bern_Parameter_Wegdaten as wd
from U5_6_stadtlauf_Bern_check_text import check_text

#Variablen
run=True
d=1           #Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur
x=0
y=0
left=None
right=None

##############################################
#######################################
# Hier kommt Ihr neuer Code
# Figur als Objekt initialisieren mit dem Klassenaufruf <objekt>=sf.Figur(<Name>)
# sf.Figur deshalb, weil die Klasse im Modul stadtlauf_bern_oo_modul erfasst wurde, welches "as sf" importiert ist
# Die Bezeichnungen für das Objekt und den Namen können frei gewählt werden



# bis hier
#######################################
##############################################

while run:
    sf.clock.tick(27)

    if d>0:
       for wg in wd.weg['Zytglogge']:
         gx,gy=wg
         time.sleep(slower)  #Laufgeschwindigkeit reduzieren

##############################################
         #######################################
         # Hier kommt Ihr neuer Code
         # Figur den vorgegebenen Weg laufen lassen
         # Hierzu muss die Methode go_walk_right(gx,gy) verwendet werden

         x,y,left,right=

         # bis hier
         #######################################
##############################################

         text2show,xt,yt=check_text(x,y)       #Prüfen ob ein Text angezeigt werden soll
         sf.redrawGameWindow(text2show,xt,yt-15,x,y,left,right)  #Grafik neu darstellen
    d-=1

##############################################
    #######################################
    # Hier kommt Ihr neuer Code
    # Hierzu die Methode check_key() verwenden

    x,y,left,right,run=              #Prüfen ob und welche Taste gedrückt wurde

    # bis hier
    #######################################
##############################################

    sf.redrawGameWindow(text2show,xt,yt-15,x,y,left,right)  #Grafik neu darstellen
    
#Ende Darstellung
pygame.quit()
