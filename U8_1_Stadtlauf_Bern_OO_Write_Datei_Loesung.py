####################################################
# Musterlösung: Stadtlauf Bern OO – Wegdaten in Datei schreiben
####################################################

import stadtlauf_bern_oo_modul as sf
from U5_6_stadtlauf_Bern_check_text import check_text

run = True
marsi = sf.Figur("Marsi")
x, y = marsi.x, marsi.y

# Datei zum Beschreiben öffnen.
w = open("Wegdaten_OO.txt", "w", encoding="utf-8")

# Alte Position: Nur bei Bewegung wird ein Datensatz geschrieben.
x1, y1 = x, y

while run:
    x, y, left, right, run = marsi.check_key()
    text2show, xt, yt = check_text(x, y)
    sf.redrawGameWindow(text2show, xt, yt - 15, marsi)

    # Daten nur schreiben, wenn sich die Position verändert hat.
    if x != x1 or y != y1:
        wegpunkt = f"{x}:{y}:{left}:{right}\n"
        w.write(wegpunkt)
        x1, y1 = x, y

w.close()
sf.screen.bye()
