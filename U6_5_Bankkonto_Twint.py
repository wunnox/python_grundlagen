#!/usr/bin/python3
##############################################
#
# Name: U6_5_Bankkonto_Twint.py
#
# Author: Peter Christen (Nach einer Idee eines Teilnehmers)
#
# Version: 1.0
# 
# Date: 28.04.2024
#
# Purpose: Kontoverwaltung
#          Konten automatisch ausgleichen 
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

      self.kontostand=kontostand
      self.aenderung_kontostand=self.aktueller_zeitstempel()

  def daten_ausgeben(self):
      '''Kunden- und Kontodaten ausgeben'''

      print ("############################")
      print (f"# Kontoangaben {self} ")
      print ("############################")
      print ("Kontonummer:", self.kontonummer)
      print ("Kontostand:", "{:.2f}".format(self.kontostand))
      print ("per Stichtag:", self.aenderung_kontostand)
      print ()

  def aktueller_zeitstempel(self):
      '''Aktueller Zeitstempel erfassen'''

      now = datetime.datetime.now()
      return now.strftime("%d.%m.%Y %H:%M:%S:%f")

class Transaktionen(Konto):
  '''Subklasse Transaktion zum Ein- und Auszahlen'''

  def __init__(self,ktnr):
      super().__init__(ktnr)

  def einzahlen(self,betrag):
      '''Geld einzahlen'''

      self.kontostand+=betrag
      self.aenderung_kontostand=self.aktueller_zeitstempel()

  def auszahlen(self,betrag):
      '''Geld auszahlen'''

      self.kontostand-=betrag
      self.aenderung_kontostand=self.aktueller_zeitstempel()

class Twint(Transaktionen):
  '''Subklasse Twint für direkten Übertrag'''
 
  def __str__(self):
      return f"Konto {self.kontonummer}"

  def __lt__(self, other):
      return self.kontostand < other.kontostand

  def __gt__(self, other):
      return self.kontostand > other.kontostand

  def __sub__(self, other):
      return self.kontostand - other.kontostand

  def uebertrag(self, zielkonto, betrag):
      '''Geld übertragen'''

      self.kontostand-=betrag
      zielkonto.einzahlen(betrag)
      self.aenderung_kontostand=self.aktueller_zeitstempel()


#Objekt/Daten erfassen
konto1=Twint("12345-1")
konto1.kontostand_erfassen(200)
konto2=Twint("34876-2")
konto2.kontostand_erfassen(400)

#Geld einbezahlen
konto1.einzahlen(1000)

print("# Angaben vor Ausgleich\n")
konto1.daten_ausgeben()
konto2.daten_ausgeben()

#Konten mit Twint ausgleichen
if konto1 > konto2:
   diff=konto1-konto2
   ubt=diff/2
   konto1.uebertrag(konto2,ubt)
   print("# Es wurden", "{:.2f}".format(ubt), f"nach {konto2} übertragen\n")

if konto1 < konto2:
   diff=konto2-konto1
   ubt=diff/2
   konto2.uebertrag(konto1,ubt)
   print("# Es wurden", "{:.2f}".format(ubt), f"nach {konto1} übertragen")

print("# Angaben nach Ausgleich\n")
konto1.daten_ausgeben()
konto2.daten_ausgeben()
