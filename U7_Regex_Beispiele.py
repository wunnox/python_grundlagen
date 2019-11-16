#!/usr/local/bin/python3
#############################################
#
# Name: U7_Regex_Beispiele.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Regex Beispiele
#
##############################################

import re

tx = "Haus und Mus und Laus"
print("0: Basistext", tx)
print("1: (re)     ", re.sub("Maus", "x", tx))
print("1: (replace)", tx.replace("Maus", "x"))
print("2: (re)     ", re.sub("[H|M]aus", "x", tx))
print("2: (replace)", tx.replace("[H|M]aus", "x"))
print("6: (re)     ", re.sub("^.aus", "x", tx))
print("7: (re)     ", re.sub("[A-Z].+us(?=\W)", "x", tx))

print()

y = "In diesen 3 Strassen gibt es 33 Häuser mit 333 Fenster"
print(y)
print("Direkt 33:   ", re.sub('33', "65", y))
print("3+       :", re.sub('3+', "65", y))
print("33?      :", re.sub('33?', "65", y))
print("3{2}     :", re.sub('3{2}', "65", y))
print("\W33\W   :", re.sub('\W33\W', "65", y))

print()
print("Wort Grenze:", re.sub('(?<=\W)33(?=\W)', "65", y))

# http://www.tutorialspoint.com/python/python_reg_expressions.htm
