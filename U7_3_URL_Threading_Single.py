#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches drei Threads startet
# Der erste Thread läuft 8 Sekunden, der zweite 4 Sekunden und der dritte 6 Sekunden
# Nehmen Sie als Vorlage , die vorhergehenden Folie.
#
####################################################

#### Lösung: ####
import urllib.parse, urllib.request
from time import perf_counter

response=[]
wiki = 'https://de.wikipedia.org/wiki/'
laender = ['Schweiz', 'Deutschland', 'Frankreich', 'Italien', 'Österreich']
urls = [wiki + urllib.parse.quote(l) for l in laender]

def get_url(url):                                          ### Funktion
    try: 
        l = len(urllib.request.urlopen(url).read())
        response.append(f"{url:45}{l:>10d}")
    except: response.append(f"{url:45}Fehler")

start = perf_counter()

for url in urls:                                           ### Starten der Threads
    get_url(url)
for r in response:                                         ### Resultat auslesen
   print (r)

end = perf_counter()
print(f"Performance: {end - start} Sec")
