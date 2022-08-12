#!/usr/bin/python3
####################################################
#
# Uebung:
# Lesen Sie mit einem Python Script nur die Daten von
# Julia Merten aus und schreiben Sie diese in eine Datei
#
####################################################

#### Lösung: ####
import sqlite3

# Verbindung und Cursor erzeugen
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL-Abfrage
personalnummer = 2297
# cursor.execute("SELECT * FROM personen where personalnummer=2297)
#cursor.execute("SELECT * FROM personen where personalnummer=:pn",{"pn":personalnummer})
cursor.execute("SELECT * FROM personen where personalnummer=?",
               (personalnummer,))

# File öffnen
d = open("Ausgabe_DB.txt", "w")

# Ausgabe des Ergebnisses
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2], dsatz[3], dsatz[4])
    eintrag = str(dsatz[0]) + "," + str(dsatz[1]) + "," + \
        str(dsatz[2]) + "," + str(dsatz[3]) + "," + str(dsatz[4]) + "\n"
    d.write(eintrag)
d.close()

# Datenbank schliessen
connection.close()
