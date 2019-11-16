#!/usr/local/bin/python3
##############################################
#
# Name: UebungGuiAbschluss.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 05.11.2015
#
# Purpose: Liest die Daten einer sqlite3-Datenbank ein und zeigt sie in einem GUI an
#
##############################################

import tkinter
import sqlite3

# Variabeln
datenbank = 'firma.db'
tabellenname = 'personen'
titel = "Datenbank Personen"

# Datenbank verbinden
connection = sqlite3.connect(datenbank)
cursor = connection.cursor()

# Funktion zu Button Ende


def ende():
    main.destroy()

# Funktion für Anzeige


def anzeigen(self):
    rownr = scvwert.get()
    sql = "select * from " + tabellenname
    cursor.execute(sql)
    row = cursor.fetchall()

    # Row 0
    re["text"] = rownr
    na["text"] = row[rownr][0]
    vn["text"] = row[rownr][1]
    pn["text"] = row[rownr][2]
    geh["text"] = row[rownr][3]
    geb["text"] = row[rownr][4]

    #Row -1
    rem1["text"] = rownr - 1
    nam1["text"] = row[rownr - 1][0]
    vnm1["text"] = row[rownr - 1][1]
    pnm1["text"] = row[rownr - 1][2]
    gehm1["text"] = row[rownr - 1][3]
    gebm1["text"] = row[rownr - 1][4]

    #Row +1
    rep1["text"] = rownr + 1
    nap1["text"] = row[rownr + 1][0]
    vnp1["text"] = row[rownr + 1][1]
    pnp1["text"] = row[rownr + 1][2]
    gehp1["text"] = row[rownr + 1][3]
    gebp1["text"] = row[rownr + 1][4]

# Main


# Bereich der Skala definieren
sql = "select count(*) from " + tabellenname
cursor.execute(sql)
row = cursor.fetchall()
anzrow = row[0][0]

main = tkinter.Tk()
main.wm_title(titel)

# Widget-Variablen
scvwert = tkinter.IntVar()
scvwert.set(0)

tkinter.Label(
    main,
    text="Datensätze Personal",
    bg="#FFFFFF").grid(
        row=0,
        column=0,
        columnspan=7,
    sticky="we")

# Zeile 1
tkinter.Label(main, text="Skala", width=7).grid(row=1, column=0, sticky="w")
tkinter.Label(main, text="Nr", width=7).grid(row=1, column=1, sticky="we")
tkinter.Label(main, text="Name", width=7).grid(row=1, column=2, sticky="we")
tkinter.Label(main, text="Vorname", width=7).grid(row=1, column=3, sticky="we")
tkinter.Label(
    main,
    text="Pers.Nr.",
    width=7).grid(
        row=1,
        column=4,
    sticky="we")
tkinter.Label(main, text="Gehalt", width=7).grid(row=1, column=5, sticky="we")
tkinter.Label(
    main,
    text="Geburtsdatum",
    width=10).grid(
        row=1,
        column=6,
    sticky="we")

# Zeile 2
tkinter.Scale(main, width=20, length=100, orient="vertical", from_=0, to=anzrow - 1,
              resolution=1, tickinterval=1, label="Row",
              command=anzeigen, variable=scvwert).grid(row=2, column=0, rowspan=3)

rem1 = tkinter.Label(main, width=4, relief="sunken")
rem1.grid(row=2, column=1, sticky="we")
nam1 = tkinter.Label(main, width=7, relief="sunken")
nam1.grid(row=2, column=2, sticky="we")
vnm1 = tkinter.Label(main, width=7, relief="sunken")
vnm1.grid(row=2, column=3, sticky="we")
pnm1 = tkinter.Label(main, width=7, relief="sunken")
pnm1.grid(row=2, column=4, sticky="we")
gehm1 = tkinter.Label(main, width=7, relief="sunken")
gehm1.grid(row=2, column=5, sticky="we")
gebm1 = tkinter.Label(main, width=10, relief="sunken")
gebm1.grid(row=2, column=6, sticky="we")

re = tkinter.Label(main, width=4, borderwidth=1, anchor="w")
re.grid(row=3, column=1, sticky="we")
na = tkinter.Label(main, width=7, relief="sunken")
na.grid(row=3, column=2, sticky="we")
vn = tkinter.Label(main, width=7, relief="sunken")
vn.grid(row=3, column=3, sticky="we")
pn = tkinter.Label(main, width=7, relief="sunken")
pn.grid(row=3, column=4, sticky="we")
geh = tkinter.Label(main, width=7, relief="sunken")
geh.grid(row=3, column=5, sticky="we")
geb = tkinter.Label(main, width=10, relief="sunken")
geb.grid(row=3, column=6, sticky="we")

rep1 = tkinter.Label(main, width=4, relief="sunken")
rep1.grid(row=4, column=1, sticky="we")
nap1 = tkinter.Label(main, width=7, relief="sunken")
nap1.grid(row=4, column=2, sticky="we")
vnp1 = tkinter.Label(main, width=7, relief="sunken")
vnp1.grid(row=4, column=3, sticky="we")
pnp1 = tkinter.Label(main, width=7, relief="sunken")
pnp1.grid(row=4, column=4, sticky="we")
gehp1 = tkinter.Label(main, width=7, relief="sunken")
gehp1.grid(row=4, column=5, sticky="we")
gebp1 = tkinter.Label(main, width=10, relief="sunken")
gebp1.grid(row=4, column=6, sticky="we")

# Row 3
tkinter.Button(main, text="Ende", width=7, command=ende).grid(row=5, column=0)

main.mainloop()
