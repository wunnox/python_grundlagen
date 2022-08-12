#!/usr/bin/python3
###################################################################
#
# Uebung:
# In vorliegender Ballade "Erlkönig" hat es einen Fehler.
# Die "er" am Zeilenanfang sollten mit einem Grossbuchstaben anfangen
# Öffnen Sie das File "Erloenig.txt" zum Lesen und Schreiben
# Ändern Sie die entsprechenden Charakter "e" direkt auf "E"
#
###################################################################

#### Lösung: ####

import re

pos = []
# Datei zum Lesen und Schreiben öffnen
d = open("Erlkoenig.txt", "r+")
zeile = d.readline()
while zeile:
    if re.findall('^e.+', zeile):
        l = len(zeile)
        l = l + len(re.findall(r'[^\x00-\x7f]', zeile))
        pos.append(d.tell() - l)
    zeile = d.readline()

for p in pos:
    d.seek(p)
    d.write("E")

d.close()
quit()
