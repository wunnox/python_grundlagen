import sqlite3

# Verbindung und Cursor erzeugen
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()


# Tabelle erzeugen
cursor.execute(
    "CREATE TABLE personen(name TEXT,vorname TEXT,personalnummer INTEGER PRIMARY KEY,gehalt FLOAT,geburtstag TEXT)")

# Transaktion bestätigen und Verbindung schliessen
connection.commit()
connection.close()
