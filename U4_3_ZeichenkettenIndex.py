###################################################################
#
# Uebung:
# Setzen Sie die Variable d="frische Fische fischt Fischers Fritz"
# Zählen Sie die Anzahl Buchstaben "i" in diesem Satz und geben Sie
# den Wert auf dem Bildschirm aus
# Geben Sie das letzte Word in der Variable d auf dem Bildschirm aus
# Das Resultat soll so aussehen: 5 i, Fritz
#
###################################################################

#### Lösung: ####

d = "frische Fische fischt Fischers Fritz"

print(d.count("i"), "i,", d[-5:])
