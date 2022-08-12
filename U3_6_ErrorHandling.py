#!/usr/bin/python3
###################################################################
#
# Uebung:
# Lesen Sie mit der Funktion raw_input() eine Zahl in eine Variable.
# Addieren Sie den Wert 5 und geben Sie die Summe aus.
# Stellen Sie sicher, dass eine falsche Eingabe kein Programmabbruch
# bewirkt, sonder eine entsprechende Meldung ausgegeben wird.
#
###################################################################

#### Lösung: ####

# Eingabe
z = input("Bitte geben Sie eine ganze Zahl ein: ")

# Versuch der Berechnung
try:
    z=int(z)
    print(z + 5)

# Fehler bei Umwandlung
except Exception:
    print(z, "ist keine Zahl")
