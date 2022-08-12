#!/usr/bin/python3
##############################################
#
# Name: U11_2_GUI_Text.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Erstellt ein GUI it einem Textfeld
#
##############################################

import tkinter

def ende():
    main.destroy()

main = tkinter.Tk()

# Main Part
b = tkinter.Button(main, text="Ende", width=30, command=ende)
b2 = tkinter.Label(
    main,
    text="Zum Beenden unten klicken",
    width=30,
    bg="yellow")

b2.pack()
b.pack()

# Endlosschleife
main.mainloop()
