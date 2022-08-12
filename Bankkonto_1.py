#!/usr/bin/python3
##############################################
#
# Name: Bankkonto_1.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 25.05.2020
#
# Purpose: Kontoverwaltung
#          Basis Script
#
##############################################

import time

#Klassen
class Konto:
  '''Klasse Konto zur Verwaltung von Bankkonten'''

  #Konstruktor Methode
  def __init__(self,ktnr):
      self.kontonummer=ktnr

  #Destruktor Methode
  def __del__(self):
      print ("\nLösche", self.kontonummer, "wieder")

#Objekt erfassen
konto1=Konto("12345-1")

#Daten auslesen
print("Kontonummer:",konto1.kontonummer)

