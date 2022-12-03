#!/usr/bin/python

import sqlite3

###################################################################
# Uebung:
# Folgende Mitarbeiter müssen noch in die Tabelle "personen" eingefügt werden:
# Name: Schmitz, Peter, P-Nr:81343, Gehalt: 3750, Geburtsdatum: 12.04.1958
# Name: Müller, Hans, P-Nr: 6143, Gehalt: 3650, Geburtsdatum: 22.08.1960
#
###################################################################

#### Lösung: ####

# Verbindung und Cursor erzeugen
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE if not exists personen (name TEXT,vorname TEXT,personalnummer INTEGER PRIMARY KEY,gehalt FLOAT,geburtstag TEXT)")

# Datensatz erzeugen
cursor.execute(
    "INSERT INTO personen VALUES ('Schmitz','Peter', 8134, 3750, '12.04.1958')")
cursor.execute(
    "INSERT INTO personen VALUES ('Müller','Hans', 6143, 3650, '22.08.1960')")
cursor.execute(
    "insert into personen values ('Maier','Hans', 6714, 3500, '15.03.1962')")
cursor.execute(
    "insert into personen values ('Muster','Hans',8420,3400,'16.08.1985')")
cursor.execute(
    "insert into personen values ('Mertens','Julia', 2297, 3621.5, '30.12.1959')")

# Transaktion bestätigen und Verbindung schliessen
connection.commit()
connection.close()
