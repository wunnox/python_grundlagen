#!/usr/bin/python3
##############################################
#
# Uebung:
# Erstellen Sie ein Programm, welches fünf Prozesse startet
# Die Prozesse sollen nur aus einem sleep-Kommando bestehen
# Die sleep-Time soll per Zufallszahl zwischen 10 und 20 Sekunden liegen
#
##############################################

#### Lösung: ####

from multiprocessing import Process, Pipe
import random
import time

# Variabeln
pia, pib = Pipe()  # Pipe erstellen

# Funktionen

def start_sleep(pc,pia):
    n = random.randint(10, 20)
    print("Starte sleep mit", n, "Sekunden")
    time.sleep(n)
    pia.send(pc)
    pia.close()

if __name__ == '__main__':
    # Prozesse starten
    for pc in range(5):
        px = Process(target=start_sleep, args=(pc,pia))
        px.start()

    # Abschluss
    for pc in range(5):
        resp = pib.recv()
