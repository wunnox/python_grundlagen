#!/usr/local/bin/python3
##############################################
#
# Name: U7.2_PrimRechner_Multiprocessing.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.07.2017
#
# Purpose: Verteilt eine Berechnung von Primzahlen auf mehrere Prozesse
#
##############################################

from multiprocessing import Process, Pipe

# Variabeln
pc = []  # Liste für Primzahlenzähler
pia, pib = Pipe()  # Pipe für Primzahlen erstellen

# Funktionen


def primrechner(ps, pe):

    # Berechnung erstellen
    print("Suche Primzahlen von", ps, "bis", pe)
    for z in range(ps, pe + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    pia.send(len(pc))


# Prozesse starten
px = Process(target=primrechner, args=(1, 17000))
px.start()
px = Process(target=primrechner, args=(17001, 24000))
px.start()
px = Process(target=primrechner, args=(24001, 30000))
px.start()

# Abschluss
anzahlprimzahlen = pib.recv()
anzahlprimzahlen = anzahlprimzahlen + pib.recv()
anzahlprimzahlen = anzahlprimzahlen + pib.recv()
print("Es wurden", anzahlprimzahlen, "Primzahlen gefunden")
