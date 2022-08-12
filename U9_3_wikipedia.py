#!/usr/bin/python3
##############################################
#
# Name: U9_3_wikipedia.py
#
# Author: Peter Christen
#
# Version: 1.1
#
# Date: 10.07.2020
#
# Purpose: Liest Städtenamen von der Seite "https://de.wikipedia.org/wiki/Schweiz" ein
#
##############################################

import urllib.request, re

# Verbindung zu einer URL
u = urllib.request.urlopen("https://de.wikipedia.org/wiki/Schweiz")

# Liest alle Zeilen in eine Liste
li = u.read()

# Schliesst die Verbindung
u.close()

li=li.decode()

stadtname={'Bern':0,'Basel':0,'Zürich':0}
for s in stadtname.keys():
   s2=s+" "
   stadtname[s]=len(re.findall(s2, li))

print("Anzahl Nennungen:")
fm = "{0:<8}{1:^3}{2:>4d}"

# Ausgabe der gefundenen Städte
for s,a in stadtname.items():
    print (fm.format(s,":",a))
