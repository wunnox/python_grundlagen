#!/usr/bin/python3
####################################################
#
# Uebung:
# Lesen Sie mit einem Python Script nur die Daten von
# Julia Merten aus und schreiben Sie diese in eine Datei
#
####################################################

#### Lösung: ####
import mysql.connector

# Verbindung und Cursor erzeugen
connection = mysql.connector.connect(user='kurs0', password='kurs',
                                     host='192.168.154.36',
                                     database='firma')
cursor = connection.cursor()

# SQL-Abfrage
personalnummer = 2297
cursor.execute("SELECT * FROM personen where personalnummer=2297")

# Ausgabe des Ergebnisses
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2], dsatz[3], dsatz[4])

# Datenbank schliessen
connection.close()
