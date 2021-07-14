#!/usr/local/bin/python3
##############################################
#
# Name: Bankkonto_2.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 22.05.2020
#
# Purpose: Kontoverwaltung
#          Kontostand erfassen
#
##############################################

import datetime


#Klassen
class Konto:
  #Klassenvariable
  now = datetime.datetime.now()

  #Konstruktor Methode
  def __init__(self,ktnr):
      #Attribute
      self.kontonummer=ktnr

  #Weitere Methode
  def kontostand_erfassen(self,kontostand):
      self.kontostand=kontostand
      self.aenderung_kontostand=Konto.now.strftime("%d.%m.%Y %H:%M:%S")

#Objekt/Daten erfassen
konto1=Konto("12345-1")
konto1.kontostand_erfassen(200)

#Daten auslesen
print("Kontonummer:",konto1.kontonummer, "\nKontostand:",konto1.kontostand)

