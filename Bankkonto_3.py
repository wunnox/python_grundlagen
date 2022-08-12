#!/usr/bin/python3
##############################################
#
# Name: Bankkonto_3.py
#
# Author: Peter Christen
#
# Version: 1.1
# 
# Date: 22.05.2020
#       05.05.2022 V1.1 Zeitanpassung
#
# Purpose: Kontoverwaltung
#          Daten ausgeben
#
##############################################

import datetime

#Klassen
class Konto:
  '''Klasse Konto zur Verwaltung von Bankkonten'''
  
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

  def daten_ausgeben(self):
      '''Kunden- und Kontodaten ausgeben'''

      print ("######################")
      print ("# Kontoangaben       ")
      print ("######################")
      print ("Kontonummer:", self.kontonummer)
      print ("Kontostand:", "{:.2f}".format(self.kontostand))
      print ("per Stichtag:", self.aenderung_kontostand)
      print ()

#Objekt/Daten erfassen
konto1=Konto("12345-1")
konto1.kontostand_erfassen(200)

#Daten ausgeben
konto1.daten_ausgeben()

