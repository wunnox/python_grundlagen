##############################################
#
# Name: U6_2_Bankkonto_Dokumentation.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 30.01.2026
#
# Purpose: Programm zum Verwalten von Bankkonten mit Dokumentation
#
##############################################

import datetime
import time
import sys


def dokumentation():
    from pathlib import Path

    header = "Dokumentation Script "+Path(__file__).name
    header_size = len(header)
    print("#"*(header_size+4))
    print("#", header, "#")
    print("#"*(header_size+4))
    print()
    print("Programm zum Verwalten von Bankkonten")

    print(Konto.__doc__)
    print(Konto.kontostand_erfassen.__doc__)
    print(Konto.daten_ausgeben.__doc__)

    print(Transaktionen.__doc__)
    print(Transaktionen.einzahlen.__doc__)
    print(Transaktionen.auszahlen.__doc__)
    print()
    # print("Anwendung")
    # print("=========")
    # print()
    # parser.print_help() #-> gut bei Verwendung des Modules argpars

# Klassen


class Konto:
    '''
    Klasse Konto
    ============
    Klasse um initialen Betrag zu erfassen und Daten zu Konten auszugeben

    Beinhaltet folgende Methoden:
     - kontostand_erfassen(self,kontostand)
     - daten_ausgeben(self)

    Details zu Methoden
    ===================
    '''

    # Konstruktor Methode
    def __init__(self, ktnr):
        self.kontonummer = ktnr

    # Weitere Methode
    def kontostand_erfassen(self, kontostand):
        '''
        Methode kontostand_erfassen
         - Initialer Kontostand für ein Konto erfassen
        '''

        now = datetime.datetime.now()
        self.kontostand = kontostand
        self.aenderung_kontostand = now.strftime("%d.%m.%Y %H:%M:%S")

    def daten_ausgeben(self):
        '''
        Methode daten_ausgeben
         - Daten zu einem Konto ausgeben
        '''

        print("######################")
        print("# Kontoangaben       ")
        print("######################")
        print("Kontonummer:", self.kontonummer)
        print("Kontostand:", "{:.2f}".format(self.kontostand))
        print("per Stichtag:", self.aenderung_kontostand)
        print()


class Transaktionen(Konto):
    '''
    Subklasse Transaktion 
    =====================
    Subklasse der Klases Konto Beträge auf die Konten ein- und auszahlen zu können

    Beinhaltet folgende Methoden:
     - einzahlen(self,betrag)
     - auszahlen(self,betrag)

    Details zu Methoden
    ===================
    '''

    def einzahlen(self, betrag):
        '''
        Methode einzahlen
         - Geld auf ein Konto einzahlen
        '''

        now = datetime.datetime.now()
        self.kontostand += betrag
        self.aenderung_kontostand = now.strftime("%d.%m.%Y %H:%M:%S")

    def auszahlen(self, betrag):
        '''
        Methode auszahlen
        - Geld von einen Konto auszahlen
        '''

        now = datetime.datetime.now()
        self.kontostand -= betrag
        self.aenderung_kontostand = now.strftime("%d.%m.%Y %H:%M:%S")

# Main Part


if len(sys.argv) > 1:
    # Dokumentation anzeigen
    dokumentation()
    exit()


# Objekt/Daten erfassen
konto1 = Transaktionen("12345-1")
konto1.kontostand_erfassen(200)

# Daten ausgeben
konto1.daten_ausgeben()

time.sleep(2)

# Geld einbezahlen
konto1.einzahlen(1000)
konto1.daten_ausgeben()

time.sleep(2)

# Geld auszahlen
konto1.auszahlen(500)
konto1.daten_ausgeben()
