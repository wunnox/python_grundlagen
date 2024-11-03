#!/Users/peter/opt/anaconda3/bin/python3
##############################################
#
# Name: U7_2_PrimRechner_Concurrent.py
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

from concurrent import futures
from time import perf_counter

max_probe = 30000
pc=[] # Liste für Primzahlenzähler

def primrechner(ps,pe):
    '''Primzahlen errechnen'''

    pc=[]
    print("Suche Primzahlen von",ps,"bis",pe)
    for z in range(ps,pe+1):    
        for z2 in range(2,z):
            if not z%z2: break
        else: pc.append(z)
    return pc

if __name__ == "__main__": 
    start = perf_counter()
    with futures.ProcessPoolExecutor(max_workers=3) as e:       ### Anzahl Prozesse
        chunk = 10000                                           ### Chunk Grösse
        fs = {e.submit(primrechner, *(n,n+chunk-1)): n for n in range(1,max_probe,chunk)}
        for f in futures.as_completed(fs):
            pc.extend(f.result())

    # Abschluss
    print(f"Es wurden {len(pc)} Primzahlen gefunden")
    end = perf_counter()
    print(f"Performance: {end - start} Sec")

