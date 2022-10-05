#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
##############################################
#
# Name: dns_einzel.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Abfragen eines DNS
#
##############################################

import socket

#Variabeln
ipadresse='192.168.1.150'

#DNS Abfrage
try:
   ns=socket.gethostbyaddr(ipadresse)
   print(ipadresse, ":", ns[0])
except:
   print(ipadresse, ":", "Keine Auflösung")

