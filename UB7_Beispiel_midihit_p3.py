##############################################
#
# Name: UB7_Beispiel_midihit_p3.py
#
# Author: Peter Christen / Digicomp
#
# Version: 2.0
#
# Date: 11.12.2015
#       04.10.2025 V2.0 Mit KI auf Python3 umgeschrieben
#
# Purpose: Erzeugt ein Zufalls midi-Song
#
##############################################

import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
import random
import os

# Konfigurationsdaten laden
configfile = 'UB7_Beispiel_midihit_p3.conf'

def include(configfile):
    if os.path.exists(configfile):
        with open(configfile) as f:
            config = {}
            exec(f.read(), config)
            return config
    else:
        print(configfile, "Existiert nicht")
        return None

config = include(configfile)

outfile = 'UB7_Beispiel_midihit.mid'
takt = 384
anztakt = 8
cycle = int(takt / 96)
anznote = anztakt * cycle

mid = MidiFile(type=1)
track = MidiTrack()
mid.tracks.append(track)

# Meta-Informationen
track.append(MetaMessage('track_name', name='Lead', time=0))
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(60), time=0))
track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
track.append(MetaMessage('key_signature', key='C', time=0))

# Song generieren – Beispielorientiert an Original
if config:
    kc = config['kc']
    rt = config['rt']
    lt = len(rt)
    ln = len(kc)
    no = 6
    stdo = 1
    time = 0
    cc = 0
    ta = takt

    for w in range(1, anznote+1):
        if stdo == 1:
            n = 6
            stdo = 0
        else:
            n = random.randint(0, ln-1)
        b = random.randint(0, lt-1)
        note = kc[n]
        duration = rt[b]
        velocity = 100

        # MIDI NoteOn
        track.append(Message('note_on', note=note, velocity=velocity, time=time))
        # MIDI NoteOff (nach duration = Anzahl Ticks bei 96 PPQ!)
        track.append(Message('note_off', note=note, velocity=velocity, time=duration))
        time = 0  # Nach erstem Event sofortige Taktfortschreibung

mid.save(outfile)
print(f'MIDI file saved as {outfile}')


