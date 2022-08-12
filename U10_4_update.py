#!/usr/bin/python
###################################################################
#
# Uebung:
# Passen Sie die Tabelle "personen" wie folgt an:
# Mertens Julia verdient neu 3700
# Maier Hans hat das Unternehmen verlassen und kann gelöscht werden
#
###################################################################

#### Lösung: ####

import sqlite3

# Verbindung und Cursor erzeugen
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Lohn von Mertens Julia anpassen
personalnr = 2297
gehalt = 3700
#cursor.execute("update personen set gehalt=:ge where personalnummer=:pn",{"pn":personalnr,"ge":gehalt})
cursor.execute(
    "update personen set gehalt=? where personalnummer=?",
    (gehalt,
     personalnr))

# Müller Hans aus DB löschen
personalnr = 8420

sql = "delete from personen where personalnummer=" + str(personalnr)
cursor.execute(sql)

#cursor.execute("delete from personen where personalnummer=:pn",{"pn":personalnr})
#cursor.execute("delete from personen where personalnummer=?",(personalnr,))


# Transaktion bestätigen und Verbindung schliessen
connection.commit()
connection.close()
