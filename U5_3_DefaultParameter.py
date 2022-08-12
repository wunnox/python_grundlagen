#!env python3
####################################################
#
# Uebung:
# Erstellen Sie eine Funktionen, welche folgende Angaben zu einem Zylinder berechnet:
# - den Umfang: r*2*3.14
# - die Grundfläche: r*r*3.14
# - das Volumen: r*r*3.14*h
#
# Es sollen r=radius und h=Höhe übergeben werden. Die Höhe soll einen Standardwert von 10 haben
# Sie sollten ein Resultat analog zu diesem kriegen (auf eine Kommastelle gerundet)::
#
#   Angaben Zylinder:
#   Umfang: 31.4
#   Fläche: 78.5
#   Volumen: 942.0
#
####################################################

#### Lösung: ####

def zylinder(r,h=10):
    pi=3.14
    umfang = round(r*2*pi,1)
    fläche = round(r**2*pi,1)
    volumen = round(r**2*pi*h,1)
    return umfang, fläche, volumen

u, f, v = zylinder(5,12)

print("Angaben Zylinder")
print("Umfang:", u)
print("Fläche:", f)
print("Volumen:", v)
