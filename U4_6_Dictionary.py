####################################################
#
# Uebung:
# Erstellen Sie ein Dictionary mit folgenden Angaben:
#   1234-1	Zopf
#   2345-1	Gipfeli
#   3456-1	Tessiner
#   4567-1	Weggli

# Lesen Sie das Dictionary ein und erzeugen Sie damit folgende Ausgabe
# Art.Nr Artikel
# 1234-1 Zopf
# 2345-1 Gipfeli
# 3456-1 Tessiner
# 4567-1 Weggli
#
####################################################

#### Lösung: ####

# KI-Prompt
# Erstelle ein Python Script, welches folgende Aufgaben erfüllt:
# - Erstellen Sie ein Dictionary mit folgenden Angaben:
#     1234-1  Zopf
#     2345-1  Gipfeli
#     3456-1  Tessiner
#     4567-1  Weggli

# - Lesen Sie das Dictionary ein und erzeugen Sie damit folgende Ausgabe
#    Art.Nr Artikel
#    1234-1 Zopf
#    2345-1 Gipfeli
#    3456-1 Tessiner
#    4567-1 Weggli


artikel = {"1234-1":"Zopf","2345-1":"Gipfeli","3456-1":"Tessiner","4567-1":"Weggli"}

print("Art.Nr Artikel")
for artnr,art in artikel.items():
    print(artnr, art)
