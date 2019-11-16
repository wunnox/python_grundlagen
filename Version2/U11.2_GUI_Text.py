#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
##############################################
#
# Name: U11.2_GUI_Text.py
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

import Tkinter


def ende():
    main.destroy()


main = Tkinter.Tk()

# Main Part
b = Tkinter.Button(main, text="Ende", width=30, command=ende)
b2 = Tkinter.Label(
    main,
    text="Zum Beenden unten klicken",
    width=30,
    bg="yellow")

b2.pack()
b.pack()

# Endlosschleife
main.mainloop()
