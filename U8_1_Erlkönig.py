#!/usr/bin/python
###################################################################
#
# Uebung:
# In vorliegender Ballade "Erlkönig" hat es einen Fehler.
# Die "er" am Zeilenanfang sollten mit einem Grossbuchstaben anfangen
# Lesen Sie das File "Erlkoenig.txt" ein und korrigieren Sie den Fehler
# Schreiben Sie die korrekte Ballade in das File "Erlkoenig2.txt"
#
###################################################################

#### Lösung: ####

import re

# Datei einlesen
r = open("Erlkoenig.txt")
allezeilen = r.readlines()
r.close()

# Neue Datei zum schreiben öffnen
w = open("Erlkoenig2.txt", "w")
for zeile in allezeilen:
    w.write(re.sub("^er", "Er", zeile))
w.close()
