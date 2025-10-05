##############################################
#
# Name: U7_4_PrimRechner_Pool.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.08.2024
#
# Purpose: Errechnet die Primzahlen innerhalb eines definierten Zahlenbereiches
#
##############################################

# Module
from time import perf_counter
from multiprocessing import Pool,Pipe

# Variabeln
pc = []  # Liste für Primzahlenzähler
pia, pib = Pipe()  # Pipe für Primzahlen erstellen

# Funktionen
def primrechner(data):
    print("Suche Primzahlen von", data[0], "bis", data[1])
    for z in range(data[0], data[1] + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break

    data[2].send(len(pc))
    #data[2].close()

def pool_handler():
    p = Pool(3)
    p.map(primrechner, [(1,17000,pia),(17001,24000,pia),(24001,30000,pia)])

if __name__ == '__main__':
    # Prozess starten
    start = perf_counter()
    pool_handler()


    # Abschluss
    anzahlprimzahlen=0
    while pib.poll():
        anzahlprimzahlen = anzahlprimzahlen + pib.recv()

    print(f"Es wurden {anzahlprimzahlen} Primzahlen gefunden")
    end = perf_counter()
    print(f"Performance: {end - start} Sec")
