#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
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

# tx=re.sub("^d","D",tx)
# tx=re.sub("Haus$","Stall",tx)
# tx=re.sub("^d","D",re.sub("Haus$","Stall",tx))

tx = re.sub(r'^d(.*)Haus$', r'D\1Stall', tx)

print(tx)
