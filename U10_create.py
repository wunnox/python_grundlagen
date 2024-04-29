import sqlite3

# Verbindung und Cursor erzeugen
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Tabelle erzeugen
cursor.execute("CREATE TABLE personen(name TEXT,vorname TEXT,personalnummer INTEGER PRIMARY KEY,gehalt FLOAT,geburtstag TEXT)")

# Daten einfügen
cursor.execute("insert or ignore into personen values('Maier', 'Hans', 6714, 3500, '15.03.1962')")
cursor.execute("insert or ignore into personen values('Muster', 'Hans', 8420, 3400, '16.08.1985')")
cursor.execute("insert or ignore into personen values('Mertens', 'Julia', 2297, 3621.5, '30.12.1959')")
cursor.execute("insert or ignore into personen values('Schmitz', 'Peter', 8133, 3750, '12.04.1958')")
cursor.execute("insert or ignore into personen values('Müller', 'Hans', 9430, 3650, '22.08.1960')")

# Transaktion bestätigen und Verbindung schliessen
connection.commit()
connection.close()
