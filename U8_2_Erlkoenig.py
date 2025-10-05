###################################################################
#
# Uebung:
# In vorliegender Ballade "Erlkönig" hat es einen Fehler.
# Die "er" am Zeilenanfang sollten mit einem Grossbuchstaben anfangen
# Öffnen Sie das File "Erloenig.txt" zum Lesen und Schreiben
# Ändern Sie die entsprechenden Charakter "e" direkt auf "E" auf den 
#
###################################################################

#### Lösung: ####
# KI-Prompt
# Erstelle ein Python Script, welches in der Datei Erlkoenig.txt die kleinen "er" am
# Zeilenanfang direkt auf "Er" ändert. Die Datei soll zum Lesen und Schreiben geöffnet werden.

filename = "Erlkoenig.txt"

with open(filename, "r+") as f:
    lines = f.readlines()
    f.seek(0)        # Zurück an den Anfang der Datei
    f.truncate()     # Datei-Inhalt löschen

    for line in lines:
        if line.startswith("er"):
            line = "Er" + line[2:]
        f.write(line)

