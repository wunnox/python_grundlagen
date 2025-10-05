####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches Ihr Alter
# (oder sonst eines) berechnet mit datetime.
#
####################################################

#### Lösung: ####
# KI-Promt
# Ich bin am 20.06.1965 geboren, erstellen ein Python Script, welches mein Alter in Jahren ausgibt.

import datetime

heute = datetime.datetime.now()
datum=heute.strftime("%d.%m.%Y %H:%M")
print ("Heutiges Datum:", datum)

diff=(heute-datetime.datetime(1965,6,20,16,0)).total_seconds()
print ("Sekunden seit meiner Geburt:", int(round(diff)))
print ("Tage seit meiner Geburt:", int(round(diff/86400,0)))
print ("Jahre seit meiner Geburt:", int(round(diff/86400/365.25,0)))
