#!/usr/local/bin/python3
##############################################
#
# Name: U6.1_Bankkonto.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 22.05.2020
#
# Purpose: Kontoverwaltung
#          Datenausgaben
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
      self.aenderung_kontostand=self.now.strftime("%d.%m.%Y %H:%M:%S")

  def personalien_erfassen(self,vn,nn,ort):
      self.vorname=vn
      self.nachname=nn
      self.wohnort=ort
      self.aenderung_personalien=self.now.strftime("%d.%m.%Y")

  def daten_ausgeben(self):
      print ("######################")
      print ("# Kontoangaben       ")
      print ("######################")
      print ("Kontonummer:", self.kontonummer)
      print ("Kontostand:", "{:.2f}".format(self.kontostand))
      print ("per Stichtag:", self.aenderung_kontostand)
      print ()
      print ("Kontoinhaber:",self.vorname,self.nachname)
      print ("Wohnort:",self.wohnort)
      print ("Letzte Anpassung:",self.aenderung_personalien)
      print ()

#Objekt/Daten erfassen
konto1=Konto("12345-1")
konto1.kontostand_erfassen(200)
konto1.personalien_erfassen('Max','Muster','Musterlingen')

#Daten ausgeben
konto1.daten_ausgeben()

