#!/usr/local/bin/python3
##############################################
#
# Name: Bankkonto_4.py
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
  now = datetime.datetime.now()

  #Konstruktor Methode
  def __init__(self,ktnr):
      #Attribute
      self.kontonummer=ktnr

  #Weitere Methode
  def kontostand_erfassen(self,kontostand):
      now = datetime.datetime.now()
      self.kontostand=kontostand
      self.aenderung_kontostand=now.strftime("%d.%m.%Y %H:%M:%S")

  def daten_ausgeben(self):
      print ("######################")
      print ("# Kontoangaben       ")
      print ("######################")
      print ("Kontonummer:", self.kontonummer)
      print ("Kontostand:", "{:.2f}".format(self.kontostand))
      print ("per Stichtag:", self.aenderung_kontostand)
      print ()

  #Besondere Methode
  def __str__(self):
      return "Kurzangaben:\nKontonummer: "+str(self.kontonummer)+"\nKontostand: "+"{:.2f}".format(self.kontostand)

  def __repr__(self):
      return "Objekt "+str(self.kontonummer)+" der Klasse Konto"

#Objekt/Daten erfassen
konto1=Konto("12345-1")
konto1.kontostand_erfassen(200)

#Daten ausgeben
print (konto1)
print ()
print (repr(konto1))

