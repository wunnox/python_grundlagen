#!/usr/local/bin/python3
#############################################
#
# Name: U7_Thread-Modul.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Starten von Threads
#
##############################################

import time
import _thread

t = []


def show(c, s):
    t.append(c)
    print("Starte Thread", c, "mit", s, "Sek.")
    time.sleep(s)
    t.remove(c)


_thread.start_new_thread(show, (1, 3,))
time.sleep(0.5)
_thread.start_new_thread(show, (2, 5,))
time.sleep(0.5)

while t:
    print("Warte auf Ende der Threads", t)
    time.sleep(1)

print("Ende der Threads")
