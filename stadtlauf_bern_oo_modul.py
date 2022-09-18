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
screen = pygame.display.set_mode((1050,400))
pygame.display.set_caption("Spaziergang durch Bern")

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
keys = pygame.key.get_pressed()

class Figur:
   '''Klasse zum Verwalten der Spielfigur'''

   #Konstruktor Methode
   def __init__(self,figur):
      self.figur=figur   #Key Addtribut
      self.x=20          #Start Position x
      self.y=150         #Start Position y
      #self.x=700          #Start Position x
      #self.y=120         #Start Position y
      self.max_x=1000    #Max Position x
      self.max_y=340     #Max Position y
      self.min_x=-10     #Min Position x
      self.min_y=-10     #Min Position y
      self.left = False  #Nicht Richtung links schauen
      self.right = False #Nicht Richtung rechts schauen
      self.walkCount = 0 #Schrittzähler

   def redrawGameWindow(self,text2show,xt,yt):
      '''Baut das Bild neu auf'''

      global screen

      textimg = font.render(text2show, True, (255, 0, 0))
      screen.blit(bg, (0,0))  
      screen.blit(textimg, (xt,yt))
      if self.walkCount + 1 >= 27:
         self.walkCount = 0
        
      if self.left:  
         screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
         self.walkCount += 1                          
      elif self.right:
         screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
         self.walkCount += 1
      else:
         screen.blit(char, (self.x, self.y))
         self.walkCount = 0
        
      pygame.display.update() 

   def go_walk_right(self,gx,gy):
      '''Läuft nach einem vorgegebenen Plan nach rechts'''

      self.x,self.y=gx,gy
      self.left = False
      self.right = True

      return self.x,self.y

   def go_walk_left(self,gx,gy):
      '''Läuft nach einem vorgegebenen Plan nach links'''

      self.x,self.y=gx,gy
      self.left = True
      self.right = False

      return self.x,self.y

   def go_left(self,steps=1):
      '''Nach links gehen'''

      if self.x > self.min_y:
         self.x -= steps
         self.left = True
         self.right = False
         return self.x
      else:
         self.go_stop()

   def go_right(self,steps=1):
      '''Nach rechts gehen'''
     
      if self.x < self.max_x:
         self.x += steps
         self.left = False
         self.right = True
         return self.x
      else:
         self.go_stop()

   def go_stop(self):
      '''Bewegung stoppen'''

      self.left = False
      self.right = False
      self.walkCount = 0

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

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

      keys = pygame.key.get_pressed()
      if keys[pygame.K_RIGHT]:
         self.go_right(5)
         print("Position x,y: ",self.x,self.y)
         return True
      elif keys[pygame.K_LEFT]:
         self.go_left(5)
         print("Position x,y: ",self.x,self.y)
         return True
      elif keys[pygame.K_UP]:
         self.go_up(2)
         print("Position x,y: ",self.x,self.y)
         return True
      elif keys[pygame.K_DOWN]:
         self.go_down(5)
         print("Position x,y: ",self.x,self.y)
         return True
      elif keys[pygame.K_q]: return False
      else: return True
       
