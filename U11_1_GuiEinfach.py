#!/usr/bin/python3
##############################################
#
# Name: U11_1_GuiEinfach.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Erstellt ein einfaches GUI
#
##############################################

import tkinter

# Funktion zu Button Ende

def ende():
    main.destroy()

# Hauptfenster
main = tkinter.Tk()

# Button Ende
b = tkinter.Button(main, text="Ende", width=10, command=ende)
b.pack()

# Endlosschleife
main.mainloop()
