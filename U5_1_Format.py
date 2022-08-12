#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie vier Kolonnen mit den km Distanzen von
# Zürich nach Bern (125), Luzern (51.4) und Basel (85.2).
#
# Verwenden Sie das format-Kommando dafür
#
# Beispiel:
# Von       Nach       Distanz
# Zuerich   Bern        125.00  km
#
####################################################

#### Lösung: ####
print("{0:<10}{1:<10}{2:>8}".format("Von", "Nach", "Distanz"))
fm = "{0:<10}{1:<10}{2:>8.2f}{3:>4}"

print(fm.format('Zuerich', 'Bern', 125.0, 'km'))
print(fm.format('Zuerich', 'Luzern', 51.4, 'km'))
print(fm.format('Zuerich', 'Basel', 85.2, 'km'))
