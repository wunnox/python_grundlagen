#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

f = open("Firewall_Log_Auszug.csv", 'rU')
reader = csv.reader(f)
zeilen = list(reader)
l=len(zeilen)

for c in range(1,l) :
  a=str(zeilen[c]).split(';')
  print c, a[0].replace("['",""), a[1], a[2], a[3], a[4]
f.close()
