####################################################
#
# Uebung:
# In folgendem Code gibt es einen Fehler.
# Prüfen Sie mal auf Zahlen über 50
# Verwenden Sie das Debugging Modul oder eine KI für die Analyse
#
####################################################

#### Lösung: ####
# KI-Prompt
# Das nachfolgende Python Script meldet bei jeder Rechnung, dass sie richtig sei, auch wenn es nicht stimmt. 
# Was ist in diesem Script falsch?

import pdb

# Eingabe einer Zahl
x = input(
    "Geben Sie eine Rechnung ein (Bsp. 10+20). Das Resultat muss zw. 1 - 50 liegen: ")

a = int(eval(x))
# pdb.set_trace()

print(f"Sie haben folgende Rechnung eingegeben: {x}")

# Auswertung
if a > 0 or a < 50:
    print("Richtig! Das Resultat liegt zw. 1 und 50")
else:
    print("Falsch, das Ergebnis ist nicht zw. 1 und 50")
