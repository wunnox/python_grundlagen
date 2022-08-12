#!/usr/bin/python3
####################################################
#
# Uebung:
# Fügen Sie im File U11_1_GuiEinfach.py einen zweiten Button hinzu
# Dieser soll folgenende Eigenheiten haben:
#    - Er soll einen blauen Hintergrund mit weisser Schrift haben
#    - Beim drauf Klicken soll ein Browser mit der Seite der Digicomp gestartet werden
#
####################################################

#### Lösung: ####

import tkinter
import webbrowser

# Funktion zu Button Ende


def ende():
    main.destroy()


def browse():
    webbrowser.open("http://www.digicomp.ch")


# Hauptfenster
main = tkinter.Tk()

# Button Ende
b = tkinter.Button(main, text="Ende", width=10, command=ende)
b2 = tkinter.Button(main, text="Browser", command=browse)
b2['width'] = 10
b2['bg'] = "blue"
b2['fg'] = "white"
b.pack()
b2.pack()

# Endlosschleife
main.mainloop()
