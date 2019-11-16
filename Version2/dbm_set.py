#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Name: dbm_set.py
#
# Author: Peter Christen
#
# Version: 1.1
# 
# Date: 16.07.2014 - V1.0 Original
# Date: 26.10.2015 - V1.1 Anpassung für Schulungsbeispiel
#
# Purpose: Setzt Beispieldaten auf aktuellen Wert
#
##############################################

import string, sys, os, pyodbc, datetime

pfad="/Users/tgdchpe1/scripts/Python/"
pyodbc.pooling = True
connection = pyodbc.connect("DRIVER={/Library/ODBC/FileMaker ODBC.bundle/Contents/MacOS/fmodbc.so};SERVER=localhost;DATABASE=Schulung;UID=python;PWD=python12")
cursor = connection.cursor()

######## Start Functions

def datconv(dat):
    dat=str(dat)
    dat=dat.split("-")
    dat=dat[2]+"."+dat[1]+"."+dat[0]
    return dat

######## End Functions

#Neue Termine generieren
today = datetime.date.today()
TSID1=today - datetime.timedelta(days=-today.weekday(), weeks=20)
TPE1=today - datetime.timedelta(days=-today.weekday(), weeks=26)
TPA1=today - datetime.timedelta(days=-today.weekday(), weeks=25)
TPG1=today - datetime.timedelta(days=-today.weekday(), weeks=22)
TSID1=datconv(TSID1)
TPE1=datconv(TPE1)
TPA1=datconv(TPA1)
TPG1=datconv(TPG1)

TSID2=today - datetime.timedelta(days=-today.weekday(), weeks=18)
TPE2=today - datetime.timedelta(days=-today.weekday(), weeks=26)
TPA2=today - datetime.timedelta(days=-today.weekday(), weeks=24)
TPG2=today - datetime.timedelta(days=-today.weekday(), weeks=20)
TSID2=datconv(TSID2)
TPE2=datconv(TPE2)
TPA2=datconv(TPA2)
TPG2=datconv(TPG2)

TSID3=today - datetime.timedelta(days=-today.weekday(), weeks=16)
TPE3=today - datetime.timedelta(days=-today.weekday(), weeks=20)
TPA3=today - datetime.timedelta(days=-today.weekday(), weeks=18)
TPG3=today - datetime.timedelta(days=-today.weekday(), weeks=17)
TSID3=datconv(TSID3)
TPE3=datconv(TPE3)
TPA3=datconv(TPA3)
TPG3=datconv(TPG3)

TSID4=today - datetime.timedelta(days=-today.weekday(), weeks=6)
TPE4=today - datetime.timedelta(days=-today.weekday(), weeks=10)
TPA4=today - datetime.timedelta(days=today.weekday(), weeks=3)
#TPG4=today - datetime.timedelta(days=-today.weekday(), weeks=7)
TSID4=datconv(TSID4)
TPE4=datconv(TPE4)
TPA4=datconv(TPA4)
#TPG4=datconv(TPG4)
TPG4=""

TSID5=today - datetime.timedelta(days=-today.weekday(), weeks=3)
TPE5=today - datetime.timedelta(days=-today.weekday(), weeks=9)
TPA5=today - datetime.timedelta(days=-today.weekday(), weeks=6)
TPG5=today - datetime.timedelta(days=-today.weekday(), weeks=4)
TSID5=datconv(TSID5)
TPE5=datconv(TPE5)
TPA5=datconv(TPA5)
TPG5=datconv(TPG5)

TSID6=today + datetime.timedelta(days=-today.weekday(), weeks=2)
TPE6=today - datetime.timedelta(days=-today.weekday(), weeks=4)
TPA6=today - datetime.timedelta(days=-today.weekday(), weeks=2)
TPG6=" "
TSID6=datconv(TSID6)
TPE6=datconv(TPE6)
TPA6=datconv(TPA6)

TSID7=today + datetime.timedelta(days=-today.weekday(), weeks=4)
TPE7=today - datetime.timedelta(days=-today.weekday(), weeks=1)
TPA7=" "
TPG7=" "
TSID7=datconv(TSID7)
TPE7=datconv(TPE7)

TV8=today + datetime.timedelta(days=today.weekday(), weeks=10)
TB8=today + datetime.timedelta(days=today.weekday(), weeks=16)
TV9=today + datetime.timedelta(days=today.weekday(), weeks=8)
TB9=today + datetime.timedelta(days=today.weekday(), weeks=15)
TV10=today + datetime.timedelta(days=-today.weekday(), weeks=3)
TB10=today + datetime.timedelta(days=-today.weekday(), weeks=14)
TV8=datconv(TV8)
TB8=datconv(TB8)
TV9=datconv(TV9)
TB9=datconv(TB9)
TV10=datconv(TV10)
TB10=datconv(TB10)

TSID8=TSID9=TSID10=" "
TPE8=TPE9=TPE10=" "
TPA8=TPA9=TPA10=" "
TPG8=TPG9=TPG10=" "
zr1=zr2=zr3=zr4=zr5=zr6=zr7=" "
zr8="V: "+TV8+" B: "+TB8
zr9="V: "+TV9+" B: "+TB9
zr10="V: "+TV10+" B: "+TB10

#print TSID1,TSID2,TSID3,TSID4,TSID5,TSID6,TSID7,zr8,zr9

cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID1'",(TSID1,TPE1,TPA1,TPG1,zr1))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID2'",(TSID2,TPE2,TPA2,TPG2,zr2))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID3'",(TSID3,TPE3,TPA3,TPG3,zr3))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID4'",(TSID4,TPE4,TPA4,TPG4,zr4))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID5'",(TSID5,TPE5,TPA5,TPG5,zr5))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID6'",(TSID6,TPE6,TPA6,TPG6,zr6))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID7'",(TSID7,TPE7,TPA7,TPG7,zr7))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID8'",(TSID8,TPE8,TPA8,TPG8,zr8))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID9'",(TSID9,TPE9,TPA9,TPG9,zr9))
cursor.execute("update DBM set Termin=?,PME=?,PMA=?,PMG=?,Zeitfenster=? where SID='SID10'",(TSID10,TPE10,TPA10,TPG10,zr10))

connection.commit()
cursor.close()
