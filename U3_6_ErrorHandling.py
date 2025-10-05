###################################################################
#
# Uebung:
# Lesen Sie mit der Funktion raw_input() eine Zahl in eine Variable.
# Addieren Sie den Wert 5 und geben Sie die Summe aus.
# Stellen Sie sicher, dass eine falsche Eingabe kein Programmabbruch
# bewirkt, sondern eine entsprechende Meldung ausgegeben wird.
#
###################################################################

#### Lösung: ####

# KI-Prompt
# Erstelle ein Python Script, welches mit der Funktion input() eine Zahl in eine Variable einliest
# Dieser Zahl soll anschliessend 5 addiert und das Resultat auf dem Bildschirm ausgegeben werden
# Stelle sicher, dass bei einer falschen Eingaben das Programm nicht abbricht.
# Stattdessen soll es eine entsprechende Meldung ausgeben und die Zahl 10 mit fünf addieren

# Eingabe
z = input("Bitte geben Sie eine ganze Zahl ein: ")

# Versuch der Berechnung
try:
    z=int(z)
    print(z + 5)

# Fehler bei Umwandlung
except Exception as e:
    print(z, "ist keine Zahl - Fehlermeldung:", e)
    print(f"Stattdessen wird 10 + 5 ausgegeben: {10 + 5}")
