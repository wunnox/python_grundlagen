#!/usr/bin/python3
##############################################
#
# Name: os_beispiele.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Beispiele mit dem Modul os
#
##############################################

import os

print("System Typ:", os.name)
print("Arbeitsverzeichnis:",os.getcwd())

if os.path.isfile('delete.log'):
   print("Lösche Datei delete.log") 
   os.remove('delete.log')
else:
   print("Datei delete.log gibt es nicht")

