#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches die folgenden Unicode Werte als Text liefert
#
# 272, 111, 114, 273, 101, 32, 272, 111, 107, 111, 118, 105, 263
#
#
####################################################

#### Lösung: ####

# Variante 1
name=''
for i in (272, 111, 114, 273, 101, 32, 272, 111, 107, 111, 118, 105, 263):
   name+=chr(i)
print(name)

# Variante 2
for i in (272, 111, 114, 273, 101, 32, 272, 111, 107, 111, 118, 105, 263):
   print(chr(i), end='')
print()


