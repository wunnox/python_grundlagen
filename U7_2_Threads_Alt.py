#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches drei Threads startet
# Der erste Thread läuft 8 Sekunden, der zweite 4 Sekunden und der dritte 6 Sekunden
# Nehmen Sie als Vorlage , die vorhergehenden Folie.
#
####################################################

#### Lösung: ####

import time
import _thread

t = []

def show(c, s):
    t.append(c)
    print("Starte Thread", c, "mit", s, "Sek.")
    time.sleep(s)
    t.remove(c)

_thread.start_new_thread(show, (1, 12,))
time.sleep(0.5)
_thread.start_new_thread(show, (2, 22,))
time.sleep(0.5)
_thread.start_new_thread(show, (3, 18,))
time.sleep(0.5)
_thread.start_new_thread(show, (4, 14,))
time.sleep(0.5)
_thread.start_new_thread(show, (5, 21,))
time.sleep(0.5)
_thread.start_new_thread(show, (6, 19,))
time.sleep(0.5)
_thread.start_new_thread(show, (7, 15,))
time.sleep(0.5)
_thread.start_new_thread(show, (8, 18,))
time.sleep(0.5)
_thread.start_new_thread(show, (9, 13,))
time.sleep(0.5)
_thread.start_new_thread(show, (10, 14,))
time.sleep(0.5)

while t:
    print("Warte auf Ende der Threads", t)
    time.sleep(1)

print("Ende der Threads")
