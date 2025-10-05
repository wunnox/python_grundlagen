##############################################
#
# Name: Bankkonto_5.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 22.05.2020
#       05.05.2022 V1.1 Zeitanpassung
#
# Purpose: Kontoverwaltung
#          Besondere Methoden
#
##############################################

import datetime

#Klassen
class Konto:
  '''Initialer Kontostand erfassen'''

  #Konstruktor Methode
  def __init__(self,ktnr):
      #Attribute
      self.kontonummer=ktnr

  #Weitere Methode
  def kontostand_erfassen(self,kontostand):
      '''Initialer Kontostand erfassen'''

      now = datetime.datetime.now()
      self.kontostand=kontostand
      self.aenderung_kontostand=now.strftime("%d.%m.%Y %H:%M:%S")

  #Besondere Methode
  def __str__(self):
      return "Kurzangaben:\nKontonummer: "+str(self.kontonummer)+"\nKontostand: "+"{:.2f}".format(self.kontostand)

  def __eq__(self, other):
      return self.kontostand == other.kontostand

  def __lt__(self, other):
      return self.kontostand < other.kontostand

#Objekt/Daten erfassen
konto1=Konto("12345-1")
konto1.kontostand_erfassen(200)
konto2=Konto("27364-1")
konto2.kontostand_erfassen(200)

#Daten ausgeben
print ("Konto1:",konto1)
print ("Konto2:",konto2)
print ()

#Kontostand vergleichen
if konto1==konto2:
   print("Die Konten 1 + 2 haben denselben Kontostand")
elif konto1<konto2:
   print("Das Konto 1 hat einen tieferen Kontostand als Konto 2")
else:
   print("Das Konto 2 hat einen tieferen Kontostand als Konto 1")

