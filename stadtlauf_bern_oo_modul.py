#! env python3
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

#Initialisierung
pygame.init()
pygame.display.set_caption("Spaziergang durch Bern")
screen = pygame.display.set_mode((1050,400))

#Bilder
walkRight = [pygame.image.load('Bilder/R1.png'), pygame.image.load('Bilder/R2.png'), pygame.image.load('Bilder/R3.png'), pygame.image.load('Bilder/R4.png'), pygame.image.load('Bilder/R5.png'), pygame.image.load('Bilder/R6.png'), pygame.image.load('Bilder/R7.png'), pygame.image.load('Bilder/R8.png'), pygame.image.load('Bilder/R9.png')]
walkLeft = [pygame.image.load('Bilder/L1.png'), pygame.image.load('Bilder/L2.png'), pygame.image.load('Bilder/L3.png'), pygame.image.load('Bilder/L4.png'), pygame.image.load('Bilder/L5.png'), pygame.image.load('Bilder/L6.png'), pygame.image.load('Bilder/L7.png'), pygame.image.load('Bilder/L8.png'), pygame.image.load('Bilder/L9.png')]
bg = pygame.image.load('Bilder/karte-bern_kl.jpg')
char = pygame.image.load('Bilder/standing.png')

#Variablen
font = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()
xt=0  #Standard Textposition x
yt=0  #Standard Textposition y
x = 20
y = 155
walkCount = 0

keys = pygame.key.get_pressed()

def redrawGameWindow(text2show,xt,yt,x,y,left,right):
      '''Baut das Bild neu auf'''

      global screen,walkCount

      textimg = font.render(text2show, True, (255, 0, 0))
      screen.blit(bg, (0,0))  
      screen.blit(textimg, (xt,yt))
      if walkCount + 1 >= 27:
         walkCount = 0
        
      if left:  
         screen.blit(walkLeft[walkCount//3], (x,y))
         walkCount += 1                          
      elif right:
         screen.blit(walkRight[walkCount//3], (x,y))
         walkCount += 1
      else:
         screen.blit(char, (x, y))
         walkCount = 0
        
      pygame.display.update() 

class Figur:
   '''Klasse zum Verwalten der Spielfigur'''

   #Konstruktor Methode
   def __init__(self,figur):
      self.figur=figur   #Key Addtribut
      self.x=20          #Start Position x
      self.y=150         #Start Position y
      self.max_x=1000    #Max Position x
      self.max_y=340     #Max Position y
      self.min_x=-10     #Min Position x
      self.min_y=-10     #Min Position y
      self.left = False  #Nicht Richtung links schauen
      self.right = False #Nicht Richtung rechts schauen

   def go_walk_right(self,gx,gy):
      '''Läuft nach einem vorgegebenen Plan nach rechts'''

      self.x,self.y=gx,gy
      self.left = False
      self.right = True

      return self.x,self.y,self.left,self.right

   def go_walk_left(self,gx,gy):
      '''Läuft nach einem vorgegebenen Plan nach links'''

      self.x,self.y=gx,gy
      self.left = True
      self.right = False

      return self.x,self.y,self.left,self.right

   def go_left(self,steps=1):
      '''Nach links gehen'''

      if self.x > self.min_y:
         self.x -= steps
         self.left = True
         self.right = False
         return self.x,self.left,self.right
      else:
         self.go_stop()

   def go_right(self,steps=1):
      '''Nach rechts gehen'''
     
      if self.x < self.max_x:
         self.x += steps
         self.left = False
         self.right = True
         return self.x,self.left,self.right
      else:
         self.go_stop()

   def go_stop(self):
      '''Bewegung stoppen'''

      self.left = False
      self.right = False
      walkCount = 0

      return walkCount,self.left,self.right

   def go_up(self,steps=1):
      '''Nach oben gehen'''

      if self.y > self.min_y:
         self.y-=steps
         return self.y
      else:
         self.go_stop()

   def go_down(self,steps=1):
      '''Nach unten gehen'''

      if self.y < self.max_y:
         self.y+=steps
         return self.y
      else:
         self.go_stop()

   def check_key(self):
      '''Prüfen welche Taste gedrückt wurde'''

      self.left=False
      self.right=False

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

      keys = pygame.key.get_pressed()
      if keys[pygame.K_RIGHT]:
         self.go_right(1)
         self.right=True
         print("Position x,y: ",self.x,self.y)
      elif keys[pygame.K_LEFT]:
         self.go_left(1)
         self.left=True
         print("Position x,y: ",self.x,self.y)

      if keys[pygame.K_UP]:
         self.go_up(1)
         print("Position x,y: ",self.x,self.y)
      elif keys[pygame.K_DOWN]:
         self.go_down(1)
         print("Position x,y: ",self.x,self.y)

      if keys[pygame.K_q]: 
         return self.x,self.y,self.left,self.right,False
      else: 
         return self.x,self.y,self.left,self.right,True
       

