def Distanzen(bern=125, basel=85, luzern=51):
    chur = 119
    bern = bern + chur
    basel = basel + chur
    luzern = luzern + chur
    return bern, basel, luzern
