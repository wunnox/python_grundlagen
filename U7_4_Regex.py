####################################################
#
# Uebung:
# Verändern Sie folgenden Satz:
# "dies ist mein Haus und dies ist dein Haus"
# in:
# "Dies ist mein Haus und dies ist dein Stall"
#
# mit dem regex-Modul
#
####################################################

#### Lösung: ####
# KI-Propmt
# Erstellen ein Python Script, welches mit Regex den nachfolgenden Satz:
# "dies ist mein Haus und dies ist dein Haus"
# ändert in:
# "Dies ist mein Haus und dies ist dein Stall"

import re

tx = "dies ist mein Haus und dies ist dein Haus"

print(tx, "\n")

# Variante 1
# tx=re.sub("^d","D",tx)
# tx=re.sub("Haus$","Stall",tx)

# Variante 2
# tx=re.sub("^d","D",re.sub("Haus$","Stall",tx))

# Variante 3
tx = re.sub(r'^d(.*)Haus$', r'D\1Stall', tx)

print(tx)
