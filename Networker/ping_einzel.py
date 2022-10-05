#!/usr/bin/python3
##############################################
#
# Name: ping_einzel.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Sendet ein ping an eine IP-Adresse
#
##############################################

import os

#Variabeln
host='192.168.1.150'

response = os.system("ping -c 1 -t 2 " + host + ">/dev/null 2>&1")
if response == 0:
   print (host, "is alive")
else:
   print (host, "not reachable")

