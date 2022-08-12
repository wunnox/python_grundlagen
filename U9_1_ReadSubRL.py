#!/usr/bin/python3
##############################################
#
# Name: U9_1_ReadSubRL.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.02.2018
#
# Purpose: Liest Daten auf Webseite und
#          liest zusätzliche Seiten ein
#
##############################################

import urllib.request
import re

# Variabeln
www_liste = []

# Hauptseite einlesen
for p in range(1, 15):
    # URL einlesen
    webseite = "http://www.verband-musikschulen.ch/de/20_musikschule-suchen/10_liste.htm?page=" + \
        str(p)
    u = urllib.request.urlopen(webseite)
    li = u.readlines()
    u.close()

    for element in li:
        if 'detailid' in element[:-1].decode():
            ids = re.findall('detailid=[0-9]+', element[:-1].decode())
            for i in ids:
                www_liste.append(
                    "http://www.verband-musikschulen.ch/de/20_musikschule-suchen/10_liste.htm" +
                    "?" +
                    i)

# Untersteiten einlesen
for wwwl in www_liste:
    u = urllib.request.urlopen(wwwl)
    li = u.readlines()
    u.close()
    s = set()
    for element in li:
        if 'www' in element[:-
                            1].decode() and 'musikzeitung.ch' not in element[:-1].decode():
            www = (re.findall('www\..+?\.ch', element[:-1].decode()))
            for w in www:
                s.add(w)
    if s:
        print(wwwl, " : ", s)
