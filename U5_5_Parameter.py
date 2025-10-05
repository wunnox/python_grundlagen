####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches zählt, wieviele
# Parameter Sie auf der Kommandozeile angegeben haben.
#
####################################################

#### Lösung: ####
# KI-Prompt
# Erstellen Sie ein Python Script, welches zählt, wie viele Parameter auf der Kommandozeile angegeben wurden.
# Wenn kein Parameter eingegeben wurde, soll ein entsprechender Text ausgegeben werden
# Ansonsten soll die Anzahl Parameter angegeben werden.

import sys

l = len(sys.argv)

if l == 1:
    print("Es wurden keine Parameter angegeben")
else:
    print("Es wurden", l - 1, "Parameter angegeben")
