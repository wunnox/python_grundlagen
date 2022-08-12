#!/usr/bin/python3
###################################################################
#
# Uebung:
# Erstellen Sie folgendes Tupel:
# a=('Petra','Hans','Fred','Hans','Ursula','Robert','Petra','Ursula','Hans')
# Geben Sie die obigen Namen auf dem Bildschirm so aus, dass jeder
# Name nur einmal erscheint.
#
###################################################################

#### Lösung: ####

a = ('Petra', 'Hans', 'Fred', 'Hans', 'Ursula', 'Robert', 'Petra', 'Ursula', 'Hans')
s = set(a)
for n in s:
    print(n)
