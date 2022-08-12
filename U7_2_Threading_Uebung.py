#!/usr/bin/python3
##############################################
#
# Name: U7_2_Threading_Uebung.py
#
# Purpose: Erstellt 10 Threads mit sleep Prozessen variabler Dauer
#
##############################################

import threading
import random
import time

response = []
threads = []

def start_sleep(tc):  # Funktion
    threads.append(tc)
    n = random.randint(10, 20)
    print("Starte sleep mit", n, "Sekunden")
    time.sleep(n)
    threads.remove(tc)

for tc in range(10):  # Starten der Threads
    t = threading.Thread(target=start_sleep, args=(tc,))
    t.start()

while threads:
    pass  # Auf Ende der Threads warten
print("Alle Threads beendet")
