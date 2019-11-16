#!/usr/bin/python
####################################################
#
# Uebung:
# Passen Sie dieses Programm so an, dass es mit Python2 funktioniert und es
# nicht über die Umlaute äöü stolpert
# Fuehren Sie das selbe Programm mit Python 3 aus, was muessen Sie noch anpassen?
#
####################################################

# Datei einlesen
r = open("U12.1_Umlaute.txt")
allezeilen = r.readlines()
r.close()

print "Inhalt Liste:\n", allezeilen
print ""
print "Inhalt Wert:\n", allezeilen[0]
