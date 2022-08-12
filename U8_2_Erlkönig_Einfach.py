#!/usr/bin/python3
###################################################################
#
# Uebung:
# In vorliegender Ballade "Erlkönig" hat es einen Fehler.
# Die "er" am Zeilenanfang sollten mit einem Grossbuchstaben anfangen
# Öffnen Sie das File "Erloenig.txt" zum Lesen und Schreiben
# Ändern Sie die entsprechenden Charakter "e" direkt auf "E" auf den 
# Positionen 76 und 111
#
###################################################################

#### Lösung: ####

#File öffnen und einlesen
d = open("Erlkoenig.txt", "r+")
allezeilen = d.readlines()

#e auf E anpassen
d.seek(79)
print(d.tell())
d.write('E')
d.seek(114)
print(d.tell())
d.write('E')
d.close()
