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
import threading
import time

# Variabeln
pc = []
threads = []

# Funktionen
def primrechner(tc, ps, pe):
    print("Thread", tc, ": Starte von", ps, "bis", pe)
    threads.append(tc)
    for z in range(ps, pe + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break

    threads.remove(tc)
    return

# Start Threads
t = threading.Thread(target=primrechner, args=(1, 1, 17000))
t.start()
t = threading.Thread(target=primrechner, args=(2, 17001, 24000))
t.start()
t = threading.Thread(target=primrechner, args=(3, 24001, 30000))
t.start()

# Auf Abschluss der Threads warten
while threads:
    pass

# Abschluss
print("Es wurden", len(pc), "Primzahlen gefunden")
