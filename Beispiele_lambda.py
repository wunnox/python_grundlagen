#!/usr/bin/python3
##############################################
#
# Name: Beispiel_lambda.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.11.2017
#
# Purpose: Beispiele der Lambda-Funktion
#
##############################################

import random

# Standard Lambda-Funktion
kreisfläche = lambda r: r**2*3.14
print (kreisfläche(3))

# Lambda mit map-Funktion
liste=[3, 5, 12]
f = list(map(lambda r: (r**2*3.14), liste))
print(f)

# Lambda mit filter-Funktion
ungrad = list(filter(lambda x: x%2, [random.randint(1, 1000) for i in range(10)]))
print(ungrad)
