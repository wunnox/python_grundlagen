#!/usr/bin/python3
###################################################################
#
# Kapiteluebung:
# - Generieren Sie eine Zufallszahl zw. 10 und 200 und geben Sie
#   diese als Rechnung aus 
# - Mit der Funktion input() verlangen Sie anschliessend die Eingabe
#   eines Betrages als Zahlung
# - Anschliessend geben Sie eine Abrechnung mit Rechnung, Bezahlung
#   und Rückgeld aus
# - Schliessen Sie die Abrechnung mit folgendem Text aus einer Funktion ab:
#   "Besten Dank und beehren Sie uns bald wieder"
# - Ist die eingegebene Bezahlung zu tief, soll folgender Text erscheinen:
#   "Tut mir leid, aber diesen Artikel können Sie sich nicht leisten"
# - Sobald eine Abrechnung abgeschlossen ist, erfolgt die nächste Rechnung
# - Mit der Eingaben von 0 bricht das Script mit dem Dankessatz ab
# - Wird als Zahlung keine Zahl eingegeben, soll eine entsprechende Meldung
#   erscheinen und eine neue Rechnung gestellt werden.
#
###################################################################

#### Lösung: ####

import random

random.seed()

def abschluss():
    print("Besten Dank und beehren Sie uns bald wieder")

while True:
   rechnung = random.randint(10, 200)
   print("Die Rechnung beträgt:", rechnung)
   try:
      zahlung=int(input("Geben Sie Ihre Zahlung ein: "))
      if zahlung==0:
          print()
          abschluss()
          break
      print("###########")
      print("Abrechnung:")
      print("###########")
      print("Rechnung:", rechnung)
      print("Zahlung :", zahlung)
      differenz=zahlung-rechnung
      if differenz > 0:
          print("Sie kriegen",differenz,"zurück")
          abschluss()
      elif differenz==0:
          print("Passt genau")
          abschluss()
      else:
          print("Tut mir leid, aber diesen Artikel können Sie sich nicht leisten")
      print()
   except:
      print("\nDas war kein richtiger Betrag!!\n")


