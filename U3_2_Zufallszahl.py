###################################################################
#
# Uebung:
# Beauftragen Sie die KI mit folgender Aufgabe:
# Es soll eine Zufallszahl zwischen 100 und 1000 in die Variable „z“ geschrieben werden
# Es sollen 5 zur Variable „z“ hinzu addiert und das Ganze mit 2 multipliziert werden
# Das Ergebnis soll durch 3 als ganzzahlige Division und als Modulo-Division auf dem Bildschirm ausgegeben werden.

###################################################################

#### Lösung: ####
# KI-Prompt
# Erstelle ein Python Script, welches folgende Funktionen ausführt:
# - Generiere eine Zufallszahl zwischen 100 und 1000, schreiben diese in die Variable „z“
# - Addiere 5 zur Variable „z“ hinzu und multipliziere den Wert mit 2
# - Teile das Ergebnis durch 3 und gib das Resultat einmal als ganzzahlige Division und einmal als Modulo-Division auf dem Bildschirm aus

# Modul random importieren
import random

# Zufallswerte und Berechnung
z = random.randint(100, 1000)

# Zufallswerte und Berechnung
z=(z+5)*2

# Ausgabe
print(f"Resultat ganzzahlig: {z//3}, modulo: {z%3}")
