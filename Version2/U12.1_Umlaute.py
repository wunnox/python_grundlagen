#!/usr/bin/python
####################################################
#
# Uebung:
# Passen Sie dieses Programm so an, dass es mit Python2 funktioniert
# Fuehren Sie das selbe Programm mit Python 3 aus, was muessen Sie noch anpassen?
#
####################################################

#Datei einlesen
r = open("U12.1_Umlaute_äöü.txt")
allezeilen = r.readlines()
r.close()

print "Inhalt Liste:", allezeilen
print "Inhalt Wert:", allezeilen[0]
