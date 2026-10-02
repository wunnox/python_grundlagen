####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches Ihr Alter
# (oder sonst eines) berechnet mit datetime.
#
####################################################

#### Lösung: ####
# KI-Promt
# Ich bin am 20.06.1965 geboren, erstellen ein Python Script mit datetime, welches mein Alter in Jahren ausgibt.

from datetime import date

geburtstag = date(1965, 6, 20)
heute = date.today()

alter = heute.year - geburtstag.year

# Falls der Geburtstag dieses Jahr noch bevorsteht: ein Jahr abziehen
if (heute.month, heute.day) < (geburtstag.month, geburtstag.day):
    alter -= 1

print(f"Du bist {alter} Jahre alt.")
