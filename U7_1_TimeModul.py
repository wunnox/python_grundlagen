####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches Ihr Alter
# (oder sonst eines) berechnet mit time.
#
####################################################

#### Lösung: ####
# KI-Promt
# Ich bin am 20.06.1965 geboren, erstellen ein Python Script mit dem Modul time, welches mein Alter in Jahren ausgibt.

import time

dztupel = (1965, 6, 20, 0, 0, 0, 0, 0, 0)
ltgeburt = time.localtime(time.mktime(dztupel))
ltheute = time.localtime()  # Aktuell
alter = ltheute[0] - ltgeburt[0]
print("Ich bin", alter, "Jahre alt")
