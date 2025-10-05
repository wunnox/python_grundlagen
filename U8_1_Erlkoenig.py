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
# KI-Prompt
# Erstelle ein Python Script, welches die Textdatei Erlkoenig.txt einliest, die beiden "er"
# am Zeilenanfang auf "Er" ändert und den ganzen Text in die Datei Erlkoenig2.txt ausgibt

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
