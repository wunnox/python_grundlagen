#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
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


def kreisfläche(r): return r * 2 * 3.14


print(kreisfläche(3))

# Lambda mit map-Funktion
c = [72, 97, 108, 108, 111]
m = list(map(lambda x: (chr(x)), c))
print(m)

# Lambda mit filter-Funktion
ungrad = list(filter(lambda x: x %
                     2, [random.randint(1, 1000) for i in range(10)]))
print(ungrad)
