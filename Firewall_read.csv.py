#!/usr/bin/python3
##############################################
#
# Name: U7_5_read_csv.py
#
# Author: Peter Christen
#
# Version: 1.1
#
# Date: 05.11.2015 V1.0
#
# Purpose: Liest ein cvs-File ein und schreibt Daten auf Bildschirm
#
##############################################

import csv

f = open("Firewall_Log_Auszug.csv", 'rU')
reader = csv.reader(f)
zeilen = list(reader)
l = len(zeilen)

for c in range(1, l):
    a = str(zeilen[c]).split(';')
    print(c, a[0].replace("['", ""), a[1], a[2], a[3], a[4])
f.close()
