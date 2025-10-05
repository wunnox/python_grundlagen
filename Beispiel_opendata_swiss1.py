###################################################################
#
# Beispiel:
# Daten von opendata.swiss
# Liste aller Ladestationen in der Schweiz herunterladen
# Link: https://opendata.swiss/de/dataset/ladestationen-fuer-elektroautos
#
###################################################################

#### Lösung: ####
# KI-Prompt
# Erstellen ein Python Script, welches die JSON Daten unter nachfolgendem Link herunterlädt und mit pprint in eine Datei schreibt. 
# Link: https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/ch.bfe.ladestellen-elektromobilitaet.json

import requests
from pprint import pprint

url = "https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/ch.bfe.ladestellen-elektromobilitaet.json"

response = requests.get(url)

ladestellen = response.json()

with open("ladestellen.txt", "w", encoding="utf-8") as f:
    pprint(ladestellen, stream=f)




