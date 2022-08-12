#!/usr/bin/python3
##############################################
#
# Name: U6_2_Bankkonto.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 22.05.2020
#
# Purpose: Kontoverwaltung
#          Auszahlen 
#
##############################################

import datetime, time

#Klassen
class Konto:
  '''Klasse Konto zur Verwaltung von Bankkonten'''

  #Konstruktor Methode
  def __init__(self,ktnr):
      self.kontonummer=ktnr

  #Weitere Methode
  def kontostand_erfassen(self,kontostand):
      '''Initialer Kontostand erfassen'''

      now = datetime.datetime.now()
      self.kontostand=kontostand
      self.aenderung_kontostand=now.strftime("%d.%m.%Y %H:%M:%S")

  def daten_ausgeben(self):
      '''Kontodaten ausgeben'''

      print ("######################")
      print ("# Kontoangaben       ")
      print ("######################")
      print ("Kontonummer:", self.kontonummer)
      print ("Kontostand:", "{:.2f}".format(self.kontostand))
      print ("per Stichtag:", self.aenderung_kontostand)
      print ()

class Transaktionen(Konto):
  '''Subklasse Transaktion zum Ein- und Auszahlen'''

  def __init__(self,ktnr):
      Konto.__init__(self,ktnr)

  def einzahlen(self,betrag):
      '''Geld einzahlen'''

      now = datetime.datetime.now()
      self.kontostand+=betrag
      self.aenderung_kontostand=now.strftime("%d.%m.%Y %H:%M:%S")

  def auszahlen(self,betrag):
      '''Geld auszahlen'''

      now = datetime.datetime.now()
      self.kontostand-=betrag
      self.aenderung_kontostand=now.strftime("%d.%m.%Y %H:%M:%S")

#Objekt/Daten erfassen
konto1=Transaktionen("12345-1")
konto1.kontostand_erfassen(200)

#Daten ausgeben
konto1.daten_ausgeben()

time.sleep(2)

#Geld einbezahlen
konto1.einzahlen(1000)
konto1.daten_ausgeben()

time.sleep(2)

#Geld auszahlen
konto1.auszahlen(500)
konto1.daten_ausgeben()
