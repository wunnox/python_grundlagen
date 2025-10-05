###################################################################
#
# Uebung:
# Erstellen Sie eine Endlosschlaufe in welcher Sie eine Variable
# hoch zählen und aktuellen Wert auf dem Bildschirm ausgeben.
# Brechen Sie die Schlaufe nach zehn Durchgängen ab.
#
###################################################################

#### Lösung: ####

# KI-Prompt

# Erstelle mit Python eine Endlosschleife, in welcher eine Variable hoch gezählt wird
# Der aktuelle Wert der Variable soll auf dem Bildschirm ausgegeben werden
# Die Schleife soll nach zehn Durchgängen abgebrochen werden

c = 0
while True:
    c += 1
    print(c)
    if c == 10:
        break
