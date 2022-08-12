#!/usr/bin/python3
###################################################################
#
# Uebung:
# Lesen Sie die URL "http://www.cssgmbh.ch/cssgmbh/Beispiele/url_lesen.htm" ein
# Prüfen Sie, ob die Seite den Text "Hallo Python" beinhaltet
# Wenn ja, geben Sie den Text aus: "Seite ist ok"
# Ansonsten geben Sie den Text aus: "Seite ist nicht ok"
#
# SSLContext Parameter funktioniert erst ab Python3.4
#
###################################################################

#### Lösung: ####

import ssl
import urllib.request

context = ssl.SSLContext()
context.verify_mode = ssl.CERT_NONE

# URL einlesen
u = urllib.request.urlopen("https://www.cssgmbh.ch/cssgmbh/Beispiele/url_lesen.htm", context=context)
li = u.readlines()
u.close()

# Prüfe auf spezifischen Inhalt
e = "Seite ist nicht ok"
for element in li:
    if b"Hallo Python" in element:
        e = "Seite ist ok"

print(e)
