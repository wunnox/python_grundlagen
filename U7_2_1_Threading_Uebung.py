#!/usr/bin/python3
##############################################
#
# Name: U7_2_1_Threading_Uebung.py
#
# Purpose: Erstellt 10 Threads mit sleep Prozessen variabler Dauer
#          Verwendet Semaphores um Ausgaben voneinander zu trennen
#
##############################################

import threading
import random
import time

threads = []
pool_sema = threading.BoundedSemaphore()

def start_sleep(tc):  # Funktion
    threads.append(tc)
    n = random.randint(10, 20)
    with pool_sema:
        print("Starte Thread " + str(tc) + " sleeping for " + str(n) + " seconds")
    time.sleep(n)
    with pool_sema:
        print("Thread " + str(tc) + " beendet")
    threads.remove(tc)

for tc in range(10):  # Starten der Threads
    t = threading.Thread(target=start_sleep, args=(tc,))
    t.start()

while threads:
    pass

print("Alle Threads beendet")
