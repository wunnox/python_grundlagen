###################################################################
#
# Uebung:
# Öffnen Sie die Datenbank firma.db in der Shell mit dem Statement sqlite3
# Fügen Sie der Tabelle "personen" folgenden Eintrag hinzu
# Name: Hans Muster, P-Nr: 8420, Lohn: 3400, Geburtstag 16.08.1985
# Ändern Sie den Lohn von Hans Muster auf 3800
# Hans Muster verlässt das Unternehmen wieder, also löschen Sie ihn aus der DB.
#
###################################################################

#### Lösung: ####

insert into personen values("Müller", "Hans", 8420, 3400, "16.08.1985")

update personen set gehalt = 3800 where personalnummer = 8420
replace into personen values("Müller", "Hans", 8420, 3800, "16.08.1985")

delete from personen where personalnummer = 8420
