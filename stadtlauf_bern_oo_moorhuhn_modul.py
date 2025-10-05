##############################################
#
# Name: stadtlauf_bern_oo_modul.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.09.2022
#
# Purpose: Modul zu Script Stadtlauf_Bern_OO.py
#
##############################################

#Module
import pygame
import datetime

#Initialisierung
pygame.init()
pygame.display.set_caption("Spaziergang durch Bern")
screen = pygame.display.set_mode((1050,400))

#Bilder
walkRight = [pygame.image.load('Bilder/R1.png'), pygame.image.load('Bilder/R2.png'), pygame.image.load('Bilder/R3.png'), pygame.image.load('Bilder/R4.png'), pygame.image.load('Bilder/R5.png'), pygame.image.load('Bilder/R6.png'), pygame.image.load('Bilder/R7.png'), pygame.image.load('Bilder/R8.png'), pygame.image.load('Bilder/R9.png')]
walkLeft = [pygame.image.load('Bilder/L1.png'), pygame.image.load('Bilder/L2.png'), pygame.image.load('Bilder/L3.png'), pygame.image.load('Bilder/L4.png'), pygame.image.load('Bilder/L5.png'), pygame.image.load('Bilder/L6.png'), pygame.image.load('Bilder/L7.png'), pygame.image.load('Bilder/L8.png'), pygame.image.load('Bilder/L9.png')]
huhnLeft = [pygame.image.load('Bilder/Lchicken1.png'), pygame.image.load('Bilder/Lchicken2.png'), pygame.image.load('Bilder/Lchicken3.png'), pygame.image.load('Bilder/Lchicken4.png'), pygame.image.load('Bilder/Lchicken5.png'), pygame.image.load('Bilder/Lchicken6.png'), pygame.image.load('Bilder/Lchicken7.png'), pygame.image.load('Bilder/Lchicken8.png'), pygame.image.load('Bilder/Lchicken9.png')]
huhnRight = [pygame.image.load('Bilder/Rchicken1.png'), pygame.image.load('Bilder/Rchicken2.png'), pygame.image.load('Bilder/Rchicken3.png'), pygame.image.load('Bilder/Rchicken4.png'), pygame.image.load('Bilder/Rchicken5.png'), pygame.image.load('Bilder/Rchicken6.png'), pygame.image.load('Bilder/Rchicken7.png'), pygame.image.load('Bilder/Rchicken8.png'), pygame.image.load('Bilder/Rchicken9.png')]
huhntot = [pygame.image.load('Bilder/chickendead1.png'), pygame.image.load('Bilder/chickendead2.png'), pygame.image.load('Bilder/chickendead3.png'), pygame.image.load('Bilder/chickendead4.png'), pygame.image.load('Bilder/chickendead5.png'), pygame.image.load('Bilder/chickendead6.png'), pygame.image.load('Bilder/chickendead7.png'), pygame.image.load('Bilder/chickendead8.png'), pygame.image.load('Bilder/chickendead8.png')]

bg = pygame.image.load('Bilder/karte-bern_kl.jpg')
char = pygame.image.load('Bilder/standing.png')
sonne = pygame.image.load('Bilder/Sonne2.png')

#Variablen
font = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()
walkCount = 0
flightCount = 0
mit_sonnenstand=True

keys = pygame.key.get_pressed()

def redrawGameWindow(text2show,xt,yt,marsmensch,moorhuhn):
      '''Baut das Bild neu auf'''

      global screen,walkCount,flightCount

      textimg = font.render(text2show, True, (255, 0, 0))
      screen.blit(bg, (0,0))  
      screen.blit(textimg, (xt,yt))

      if walkCount + 1 >= 27:
         walkCount = 0
      if flightCount + 1 >= 27:
         flightCount = 0

      if marsmensch["Status"]=="Go":
         if marsmensch['Seite']=='left':  
            screen.blit(walkLeft[walkCount//3], (marsmensch['x'],marsmensch['y']))
            walkCount += 1                          
         elif marsmensch['Seite']=='right':
            screen.blit(walkRight[walkCount//3], (marsmensch['x'],marsmensch['y']))
            walkCount += 1
         else:
            screen.blit(char, (marsmensch['x'],marsmensch['y']))
            walkCount = 0
      else:
         screen.blit(char, (marsmensch['x'],marsmensch['y']))
         walkCount = 0
        
      if moorhuhn["Status"]=='Go':
         if moorhuhn["Seite"]=='left':  
            screen.blit(huhnLeft[flightCount//3], (moorhuhn["x"],moorhuhn["y"]))
            flightCount +=1
         elif moorhuhn["Seite"]=='right':
            screen.blit(huhnRight[flightCount//3], (moorhuhn["x"],moorhuhn["y"]))
            flightCount +=1
      elif moorhuhn["Status"]=='tot':
            screen.blit(huhntot[flightCount//3], (moorhuhn["x"],moorhuhn["y"]))
            flightCount +=1

      if mit_sonnenstand:
         #Aktueller Sonnenstand
         xs,ys=sonnenstand()
         screen.blit(sonne, (xs,ys))

      pygame.display.update() 

      return xs,ys

def sonnenstand():
   '''Errechnet den Sonnenstand anhand der aktuellen Zeit'''

   heute = datetime.datetime.now()
   stunde=heute.strftime("%H")
   minute=heute.strftime("%M")
   x=1100
   y=400
   if int(stunde) > 6: x=x-(100*(int(stunde)-6))-(int(minute)*1.66)
   if int(stunde) > 6 and int(stunde) <=12: y=y-(30*(int(stunde)-6))-(int(minute)*0.5)
   else: y=y-(30*(18-int(stunde)))-(int(minute)*0.5)

   return int(x),int(y)

#Klassen
class Figur:
   '''Klasse zum Verwalten der Spielfigur'''

   #Konstruktor Methode
   def __init__(self,figur):
      self.figur=figur   #Key Addtribut
      self.x=20          #Position x
      self.y=150         #Position y
      self.max_x=1000    #Max Position x
      self.max_y=340     #Max Position y
      self.min_x=-10     #Min Position x
      self.min_y=-10     #Min Position y
      self.seite = "Stop"  #Ausgangsposition Figur

   def go_walk_right(self,x,y):
      '''Läuft nach einem vorgegebenen Plan nach rechts'''

      self.x,self.y=x,y
      self.seite = "right"

      return self.x,self.y,self.seite

   def go_walk_left(self,x,y):
      '''Läuft nach einem vorgegebenen Plan nach links'''

      self.x,self.y=x,y
      self.seite = "left"

      return self.x,self.y,self.seite

   def go_left(self,x,steps=1):
      '''Nach links gehen'''

      self.x=x
      if self.x > self.min_x:
         self.x -= steps
         self.seite = "left"
         return self.x,self.seite
      else:
         self.go_stop()

   def go_right(self,x,steps=1):
      '''Nach rechts gehen'''
     
      self.x=x
      if self.x < self.max_x:
         self.x += steps
         self.seite = "right"
         return self.x,self.seite
      else:
         self.go_stop()

   def go_stop(self):
      '''Bewegung stoppen'''

      self.seite = "stop"
      walkCount = 0

      return walkCount,self.seite

   def go_up(self,y,steps=1):
      '''Nach oben gehen'''

      self.y=y
      if self.y > self.min_y:
         self.y-=steps
         return self.y
      else:
         self.go_stop()

   def go_down(self,y,steps=1):
      '''Nach unten gehen'''

      self.y=y
      if self.y < self.max_y:
         self.y+=steps
         return self.y
      else:
         self.go_stop()

   def __eq__(self, other):
      if self.x <= other.x+10 and self.x >= other.x-10 and self.y <= other.y+15 and self.y >= other.y-60:
         return True
      else:
        return False

   def check_key(self):
      '''Prüfen welche Taste gedrückt wurde'''

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

      keys = pygame.key.get_pressed()
      if keys[pygame.K_RIGHT]:
         self.go_right(self.x,1)
         print("Position x,y: ",self.x,self.y,self.seite)
      elif keys[pygame.K_LEFT]:
         self.go_left(self.x,1)
         print("Position x,y: ",self.x,self.y,self.seite)

      if keys[pygame.K_UP]:
         self.go_up(self.y,1)
         print("Position x,y: ",self.x,self.y,self.seite)
      elif keys[pygame.K_DOWN]:
         self.go_down(self.y,1)
         print("Position x,y: ",self.x,self.y,self.seite)

      if keys[pygame.K_q]: 
         return self.x,self.y,self.seite,False
      else: 
         return self.x,self.y,self.seite,True
       

