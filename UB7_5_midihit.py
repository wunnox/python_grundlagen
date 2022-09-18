#!/usr/bin/python
##############################################
#
# Name: UB7_5_midihit.py
#
# Author: Peter Christen / Digicomp
#
# Version: 1.0
#
# Date: 11.12.2015
#
# Purpose: Erzeugt ein Zufalls midi-Song
#
##############################################

#
# http://old.mxm.dk/products/public/pythonmidi/

import smidi
import os
import random

# Variabeln
configfile = 'UB7_5_midihit.conf'
outfile = 'UB7_5_midihit.mid'
root = 2
domi = 6
takt = 384
anztakt = 8
cycle = takt / 96
anznote = anztakt * cycle
akkord = 0

# Funktionen
def include(configfile):
    if os.path.exists(configfile):
        exec(compile(open(configfile).read(), configfile, 'exec'))
    else:
        print(configfile, "Existiert nicht")

def play(c, s, n, t):
    # c=Channel, s=Start time, t=Duration Time, n=Note
    #
    m.update_time(s)
    m.note_on(channel=c, note=n, velocity=100)  # single note
    if akkord == 1:
        m.update_time(0)
        m.lyric(ak[ak2])
    m.update_time(t)
    m.note_off(channel=c, note=n, velocity=100)  # stop it after t
    m.update_time(0)

include(configfile)

# Main
m = smidi.MidiOutFile(outfile)
m.header(format=0, nTracks=2, division=96)
m.start_of_track(n_track=0)
m.key_signature(0, 0)
m.time_signature(4, 2, 24, 8)
m.instrument_name('Piano')
m.sequence_name('Lead')
m.copyright('Peters Song')
m.tempo(500000)  # 60M/BPM

lt = len(rt)
ltkl = len(rtkl)
ln = len(kc)
ta = takt
cc = 0
cct = 1
z = 0
go = 1
sta = 0
no = 6
stdo = 1
rtz = 0

# Song erstellen
for w in range(1, anznote + 1):
    if stdo == 1:
        n = 6
        stdo = 0
    else:
        n = random.randint(0, ln - 1)

    if rtz == 0:
        b = random.randint(0, ltkl - 1)
    else:
        b = random.randint(0, lt - 1)

    if n > no:
        if n - no > 3:
            n = n - int((n - no) / 1.618)
    elif no > n:
        if no - n > 3:
            n = n + int((no - n) / 1.618)

    no = n

    cc = cc + 1
    ta = ta - rt[b]

    if cc == 4:
        if ta <= 0:
            taa = rt[b] + ta
            play(0, 0, kc[n], taa)
            z = z + taa
        elif rt[b] > ta:
            play(0, 0, kc[n], rt[b])
            z = z + rt[b]
        else:
            play(0, 0, kc[n], rt[b])
            z = z + rt[b]

        if ta > 0:
            sta = ta
            z = z + sta

        cct = cct + 1
        cc = 0
        z = 0
        ta = takt
        go = 1
        rtz = 0
    elif cc == 3:
        if go == 1:
            if ta == 0:
                play(0, 0, kc[n], rt[b])
                z = z + rt[b]
                go = 0
            elif rt[b] > ta:
                if ta < 0:
                    taa = rt[b] + ta
                    go = 0
                    play(0, 0, kc[n], taa)
                    z = z + taa
                else:
                    play(0, 0, kc[n], rt[b])
                    z = z + rt[b]
            else:
                play(0, 0, kc[n], rt[b])
                z = z + rt[b]
            rtz = 1
    elif cc == 2:
        if ta == 0:
            play(0, 0, kc[n], rt[b])
            z = z + rt[b]
            go = 0
        else:
            play(0, 0, kc[n], rt[b])
            z = z + rt[b]
    else:
        akkord = 1
        ak2 = kc[n]
        play(0, sta, kc[n], rt[b])
        akkord = 0
        sta = 0
        z = z + rt[b]

m.end_of_track()
m.eof()
