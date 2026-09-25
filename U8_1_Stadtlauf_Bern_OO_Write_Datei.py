####################################################
# Übung: Stadtlauf Bern OO – Wegdaten in Datei schreiben
#
# Öffnen Sie eine Datei zum Beschreiben. Bewegen Sie Marsi mit
# den Pfeiltasten durch die Stadt. Bei jeder Positionsänderung
# sollen die Wegdaten in die Datei geschrieben werden.
#
# Wenn Marsi steht, sollen keine weiteren Daten geschrieben werden.
# Schliessen Sie die Datei am Ende des Programms wieder.
#
# Die aufgezeichnete Datei kann anschliessend mit der Leseübung
# wiedergegeben werden.
####################################################

import stadtlauf_bern_oo_modul as sf
from U5_6_stadtlauf_Bern_check_text import check_text

run = True
marsi = sf.Figur("Marsi")
x, y = marsi.x, marsi.y

####################################################
# Hier kommt Ihr Code
# Datei zum Beschreiben öffnen.
# Tipp: w = open("Wegdaten_OO.txt", "w", encoding="utf-8")


# bis hier
####################################################

# Alte Position: Nur bei Bewegung wird ein Datensatz geschrieben.
x1, y1 = x, y

while run:
    x, y, left, right, run = marsi.check_key()
    text2show, xt, yt = check_text(x, y)
    sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

    ####################################################
    # Hier kommt Ihr Code
    # Datei mit Wegdaten beschreiben.
    # Speichern Sie x, y, left und right, getrennt mit ":".


    # bis hier
    ####################################################

sf.screen.bye()

####################################################
# Hier kommt Ihr Code
# Datei schliessen.


# bis hier
####################################################
