#!/usr/local/bin/python3
##############################################
#
# Name: U7.2_Check_URL_Single.py
#
# Purpose: Prüfen der Verfügbarkeit einiger URLs
#
##############################################

import urllib.request

response = []
urls = [
    "http://chp.ch",
    "http://cssgmbh.ch",
    "http://irgendeinedomain.ch",
    "http://zouberhuet.ch"]


def get_url(url):  # Funktion
    try:
        response.append(urllib.request.urlopen(url).read())
    except BaseException:
        response.append("Probleme mit " + url)


for url in urls:  # Starten der Threads
    get_url(url)

for r in response:  # Resultat auslesen
    if "Probleme" in str(r):
        print(r)
