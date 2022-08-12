#!/usr/bin/python3
####################################################
#
# Datumsberechnungen mit Modul datetime
#
####################################################
import datetime

heute = datetime.datetime.now()
datum=heute.strftime("%d.%m.%Y %H:%M")
kw=heute.strftime("%V")
print ("Heutiges Datum:", datum)
print ("Aktuelle Kalenderwoche:", kw)

diff=(heute-datetime.datetime(1965,6,20,16,0)).total_seconds()
print ("Sekunden seit meiner Geburt:", int(round(diff)))
print ("Tage seit meiner Geburt:", int(round(diff/86400,0)))
print ("Jahre seit meiner Geburt:", int(round(diff/86400/365,0)))
