#! env python3
##############################################
#
# Name: stadtlauf_func.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.09.2022
#
# Purpose: Modul zu Script stadlauf.py
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
x = 20
y = 155
xt=0
yt=0
end=1050
left = False
right = False
walkCount = 0
run = True
text2show=None

keys = pygame.key.get_pressed()

#Module
def redrawGameWindow(text2show=None,xt=x,yt=y):
    '''Bildaufbereitung'''

    global walkCount

    img1 = font.render(text2show, True, (255, 0, 0))
    screen.blit(bg, (0,0))  
    screen.blit(img1, (xt,yt))
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
    
def go_walk_right(gx,gy):
   '''Läuft nach einem vorgegebenen Plan'''

   global x,y,left,right

   x,y=gx,gy
   left = False
   right = True

   return x,y

def go_walk_left(gx,gy):
   '''Läuft nach einem vorgegebenen Plan'''

   global x,y,left,right

   x,y=gx,gy
   left = True
   right = False

   return x,y

def go_left(steps=1):
   '''Nach links gehen'''

   global x,left,right

   if x > 1:
      x -= steps
      left = True
      right = False
      return x
   else:
      go_stop()

def go_right(steps=1):
   '''Nach rechts gehen'''

   global x,left,right
     
   if x < end:
      x += steps
      left = False
      right = True
      return x
   else:
      go_stop()

def go_stop():
   '''Bewegung stoppen'''

   global left,right,walkCount

   left = False
   right = False
   #walkCount = 0

def go_up(steps=1):
   '''Nach oben gehen'''

   global y

   y-=steps
   return y

def go_down(steps=1):
   '''Nach unten gehen'''

   global y

   y+=steps
   return y

def check_key():
   '''Prüfen welche Taste gedrückt wurde'''

   global x,y
 
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False

   keys = pygame.key.get_pressed()
   if keys[pygame.K_RIGHT]:
      go_right(2)
      print("Position x,y: ",x,y)
      #return True
   elif keys[pygame.K_LEFT]:
      go_left(2)
      print("Position x,y: ",x,y)
      #return True

   if keys[pygame.K_UP]:
      go_up(1)
      print("Position x,y: ",x,y)
      #return True
   elif keys[pygame.K_DOWN]:
      go_down(1)
      print("Position x,y: ",x,y)
      #return True

   if keys[pygame.K_q]: 
      return False
   else: 
      return True
       
