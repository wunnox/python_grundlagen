##############################################
#
# Name: Bankkonto_6.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 22.07.2024
#
# Purpose: Einsatz von getter und setter
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
      self.__kontostand=kontostand
      self.aenderung_kontostand=now.strftime("%d.%m.%Y %H:%M:%S")

  def get_balance(self):
      '''Getter für Attribut __kontostand aufrufen'''

      return self.__kontostand

  def set_balance(self,betrag):
      '''Setter für Attribut __kontostand verändern'''

      self.__kontostand+=betrag

  balance = property(get_balance, set_balance)


class Transaktionen(Konto):
  '''Subklasse Transaktion zum Ein- und Auszahlen'''

  def __init__(self,ktnr):
      super().__init__(ktnr)

  def daten_ausgeben(self):
      '''Kunden- und Kontodaten ausgeben'''

      print ("######################")
      print ("# Kontoangaben       ")
      print ("######################")
      print ("Kontonummer:", self.kontonummer)
      print ("Kontostand:", "{:.2f}".format(self.balance))
      print ("per Stichtag:", self.aenderung_kontostand)
      print ()

  def einzahlen(self,betrag):
      '''Geld einzahlen'''

      now = datetime.datetime.now()
      self.balance=betrag
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

