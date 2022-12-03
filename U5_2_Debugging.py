#!/usr/bin/python3
####################################################
#
# Uebung:
# In folgendem Code gibt es einen Fehler.
# Prüfen Sie mal auf Zahlen über 50
# Verwenden Sie das Debugging Modul für die Analyse
#
# # Eingabe einer Rechnung
# x = input("Geben Sie eine Rechnung ein (Bsp. 10+20). Das Resultat muss zwischen 1 - 50 liegen: ")
# a=eval(str(x))
#
# #Auswertung
# if a>0 or a<50:
#      print "Richtig!"
# else:
#      print "Falsch, das Ergebnis ist nicht zw. 1 und 50"
#
####################################################

#### Lösung: ####
import pdb

# Eingabe einer Zahl
x = input(
    "Geben Sie eine Rechnung ein (Bsp. 10+20). Das Resultat muss zw. 1 - 50 liegen: ")

a = eval(str(x))
# pdb.set_trace()

# Auswertung
if a > 0 or a < 50:
    print("Richtig!")
else:
    print("Falsch, das Ergebnis ist nicht zw. 1 und 50")
