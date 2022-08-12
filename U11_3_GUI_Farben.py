#!/usr/bin/python3
##############################################
#
# Name: U11_3_GUI_Farben.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 05.11.2015
#
# Purpose: Zeigt ein GUI mit verschiedenen Farben an
#
##############################################

import tkinter

# Funktion zu Button Ende

def ende():
    main.destroy()

# Hauptfenster
main = tkinter.Tk()
main.wm_title("Farbcodes")

# Frame
fra = tkinter.Frame(main)
b = tkinter.Button(fra, text="Ende", command=ende)
b["width"] = 60

# Frame 1
fr1 = tkinter.Frame(main)
fl1 = tkinter.Label(
    fr1,
    text="black oder #000000",
    width=30,
    bg="black",
    fg="white")
fl2 = tkinter.Label(fr1, text="white oder #FFFFFF", width=30, bg="white")
fl3 = tkinter.Label(
    fr1,
    text="blue oder #0000FF",
    width=30,
    bg="blue",
    fg="white")
fl4 = tkinter.Label(
    fr1,
    text="red oder #FF0000",
    width=30,
    bg="red",
    fg="white")

# Frame2
fr2 = tkinter.Frame(main)
f2l1 = tkinter.Label(fr2, text="green oder #008000", width=30, bg="green")
f2l2 = tkinter.Label(fr2, text="yellow oder #FFFF00", width=30, bg="yellow")
f2l3 = tkinter.Label(
    fr2,
    text="purple oder #8000080",
    width=30,
    bg="purple",
    fg="white")
f2l4 = tkinter.Label(fr2, text="gray oder #808080", width=30, bg="gray")

fra.pack(expand=1)
b.pack()

fr1.pack(side="left")
fl1.pack()
fl2.pack(pady=5)
fl3.pack()
fl4.pack(pady=5)

fr2.pack(side="right")
f2l1.pack()
f2l2.pack(pady=5)
f2l3.pack()
f2l4.pack(pady=5)

main.mainloop()
