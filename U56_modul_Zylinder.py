def zylinder(r,h=10):
    pi=3.14
    umfang = round(r*2*pi,1)
    fläche = round(r**2*pi,1)
    volumen = round(r**2*pi*h,1)
    return umfang, fläche, volumen
