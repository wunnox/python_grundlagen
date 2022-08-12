#!/usr/bin/python3
##############################################
#
# Name: U7_2_PrimRechner_Multiprocessing.py
#
# Author: Peter Christen
#
# Version: 1.1
#
# Date: 10.07.2017
# Change: 31.03.2021 : V1.1 : Anpassungen für neue Python Versionen
#
# Purpose: Verteilt eine Berechnung von Primzahlen auf mehrere Prozesse
#
##############################################

from multiprocessing import Process, Pipe

# Variabeln
pc = []  # Liste für Primzahlenzähler
pia, pib = Pipe()  # Pipe für Primzahlen erstellen

# Funktionen

def primrechner(ps, pe, pia):

    # Berechnung erstellen
    print("Suche Primzahlen von", ps, "bis", pe)
    for z in range(ps, pe + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    pia.send(len(pc))
    pia.close()

if __name__ == '__main__':
    # Prozesse starten
    px = Process(target=primrechner, args=(1, 17000, pia))
    px.start()
    px = Process(target=primrechner, args=(17001, 24000, pia))
    px.start()
    px = Process(target=primrechner, args=(24001, 30000, pia))
    px.start()

    # Abschluss
    anzahlprimzahlen = pib.recv()
    anzahlprimzahlen = anzahlprimzahlen + pib.recv()
    anzahlprimzahlen = anzahlprimzahlen + pib.recv()
    print("Es wurden", anzahlprimzahlen, "Primzahlen gefunden")

