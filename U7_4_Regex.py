#!/usr/bin/python3
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
