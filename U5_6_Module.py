#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie ein Modul, welches folgende Angaben zu einem Zylinder berechnet:
# - den Umfang: r*2*3.14
# - die Grundfläche: r*r*3.14
# - das Volumen: r*r*3.14*h
#
####################################################

#### Lösung: ####

# Inhalt Datei U56_modul_Zylinder.py:
#####################################
#def zylinder(r,h=10):
#    pi=3.14
#    umfang = round(r*2*pi,1)
#    fläche = round(r**2*pi,1)
#    volumen = round(r**2*pi*h,1)
#    return umfang, fläche, volumen
#####################################

from U56_modul_Zylinder import zylinder

u, f, v = zylinder(5,12)

print("Angaben Zylinder")
print("Umfang:", u)
print("Fläche:", f)
print("Volumen:", v)
