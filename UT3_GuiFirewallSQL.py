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
datenbank = 'U7.5_Firewallog.db'
tabellenname = 'firelog'
titel = "Datenbank Firewall"

# Datenbank verbinden
connection = sqlite3.connect(datenbank)
cursor = connection.cursor()

# Funktion zu Button Ende


def ende():
    main.destroy()


def anzeigen(self):
    rownr = scvwert.get()
    sql = "select * from " + tabellenname
    cursor.execute(sql)
    row = cursor.fetchall()

    # Row 0
    re["text"] = rownr
    si["text"] = row[rownr][0]
    ti["text"] = row[rownr][1]
    po["text"] = row[rownr][2]
    pr["text"] = row[rownr][3]
    co["text"] = row[rownr][4]

    #Row -1
    rem1["text"] = rownr - 1
    sim1["text"] = row[rownr - 1][0]
    tim1["text"] = row[rownr - 1][1]
    pom1["text"] = row[rownr - 1][2]
    prm1["text"] = row[rownr - 1][3]
    com1["text"] = row[rownr - 1][4]

    #Row +1
    rep1["text"] = rownr + 1
    sip1["text"] = row[rownr + 1][0]
    tip1["text"] = row[rownr + 1][1]
    pop1["text"] = row[rownr + 1][2]
    prp1["text"] = row[rownr + 1][3]
    cop1["text"] = row[rownr + 1][4]

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
    text="Datensätze Firewall",
    bg="#FFFFFF").grid(
        row=0,
        column=0,
        columnspan=7,
    sticky="we")

# Zeile 1
tkinter.Label(main, text="Skala", width=7).grid(row=1, column=0, sticky="w")
tkinter.Label(main, text="Nr", width=4).grid(row=1, column=1, sticky="we")
tkinter.Label(
    main,
    text="Source IP",
    width=12).grid(
        row=1,
        column=2,
    sticky="we")
tkinter.Label(
    main,
    text="Target IP",
    width=12).grid(
        row=1,
        column=3,
    sticky="we")
tkinter.Label(main, text="Port", width=7).grid(row=1, column=4, sticky="we")
tkinter.Label(main, text="Prot.", width=7).grid(row=1, column=5, sticky="we")
tkinter.Label(main, text="Count", width=7).grid(row=1, column=6, sticky="we")

# Zeile 2
tkinter.Scale(main, width=20, length=200, orient="vertical", from_=0, to=anzrow - 1,
              resolution=1, tickinterval=1, label="Row",
              command=anzeigen, variable=scvwert).grid(row=2, column=0, rowspan=3)

rem1 = tkinter.Label(main, relief="sunken")
rem1.grid(row=2, column=1, sticky="we")
sim1 = tkinter.Label(main, relief="sunken")
sim1.grid(row=2, column=2, sticky="we")
tim1 = tkinter.Label(main, relief="sunken")
tim1.grid(row=2, column=3, sticky="we")
pom1 = tkinter.Label(main, relief="sunken")
pom1.grid(row=2, column=4, sticky="we")
prm1 = tkinter.Label(main, relief="sunken")
prm1.grid(row=2, column=5, sticky="we")
com1 = tkinter.Label(main, relief="sunken")
com1.grid(row=2, column=6, sticky="we")

re = tkinter.Label(main, borderwidth=1, anchor="w")
re.grid(row=3, column=1, sticky="we")
si = tkinter.Label(main, relief="sunken")
si.grid(row=3, column=2, sticky="we")
ti = tkinter.Label(main, relief="sunken")
ti.grid(row=3, column=3, sticky="we")
po = tkinter.Label(main, relief="sunken")
po.grid(row=3, column=4, sticky="we")
pr = tkinter.Label(main, relief="sunken")
pr.grid(row=3, column=5, sticky="we")
co = tkinter.Label(main, relief="sunken")
co.grid(row=3, column=6, sticky="we")

rep1 = tkinter.Label(main, relief="sunken")
rep1.grid(row=4, column=1, sticky="we")
sip1 = tkinter.Label(main, relief="sunken")
sip1.grid(row=4, column=2, sticky="we")
tip1 = tkinter.Label(main, relief="sunken")
tip1.grid(row=4, column=3, sticky="we")
pop1 = tkinter.Label(main, relief="sunken")
pop1.grid(row=4, column=4, sticky="we")
prp1 = tkinter.Label(main, relief="sunken")
prp1.grid(row=4, column=5, sticky="we")
cop1 = tkinter.Label(main, relief="sunken")
cop1.grid(row=4, column=6, sticky="we")

# Row 3
tkinter.Button(main, text="Ende", width=7, command=ende).grid(row=5, column=0)

main.mainloop()
