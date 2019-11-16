#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

# Verbindung und Cursor erzeugen
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()


# Tabelle erzeugen
cursor.execute(
    "CREATE TABLE personen(name TEXT,vorname TEXT,personalnummer INTEGER PRIMARY KEY,gehalt FLOAT,geburtstag TEXT)")

# Transaktion bestätigen und Verbindung schliessen
connection.commit()
connection.close()
