####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches drei Threads startet
# Der erste Thread läuft 8 Sekunden, der zweite 4 Sekunden und der dritte 6 Sekunden
# Nehmen Sie als Vorlage , die vorhergehenden Folie.
#
####################################################

#### Lösung: ####
from time import perf_counter
from concurrent import futures
import urllib.parse, urllib.request

response=[]
wiki = 'https://de.wikipedia.org/wiki/'
laender = ['Schweiz', 'Deutschland', 'Frankreich', 'Italien', 'Österreich']
urls = [wiki + urllib.parse.quote(l) for l in laender]

def get_url(url):
    try: 
        l = len(urllib.request.urlopen(url).read())
        response.append(f"{url:45}{l:>10d}")
    except: response.append(f"{url:45}Fehler")

start = perf_counter()

with futures.ThreadPoolExecutor() as e:
    res = e.map(get_url, urls)                              ### Starten der Threads

for r in response:print (r)                                 ### Resultat auslesen

end = perf_counter()
print(f"Performance: {end - start} Sec")

