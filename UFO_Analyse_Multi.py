#!/usr/local/bin/python3
##############################################
#
# Name: UFO_Analyse.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.07.2017
#
# Purpose: Analysiert Bilder auf mögliche UFO Vorkommnisse
#          Mit Multiprozess-Funktion
#
##############################################

from multiprocessing import Process, Pipe
import os
import time

# Variabeln
limite = 95  # Ab diesem Grünwert wird das Pixel erfasst
maxproz = 4  # Wenn mehr als soviele Prozesse gestartet wurden, wird eine Warteschlaufe eingeführt
warten = 5  # Solange dauert die Warteschlaufe bei zuvielen Prozessen
bilder = os.listdir('Bilder_UFOs')  # Verzeichnisse mit Bildern
ap, bp = Pipe()  # Pipe erstellen
proz = []  # Liste für gestartete Prozesse

# Funktionen


def analyse(f):
    '''
    Analysiert ein Bild auf auffällige Veränderungen und markiert diese
    '''

    # Diese Module werden erst hier geladen, damit der Prozess eine
    # vollständige Umgebung hat
    import PIL
    import numpy as np
    import matplotlib.pyplot as plt

    # Prozess-ID in Pipe schreiben
    pid = os.getpid()
    prozcont = "Start." + str(pid)
    ap.send(prozcont)

    if 'IMG' in f:
        #print ('Prozess:', pid, 'für Bild', f)
        bild = 'Bilder_UFOs/' + f
        img = np.array(PIL.Image.open(bild))

        # Prüfen ob es entsprechende Anomalien in Bild gibt, wenn ja sofort
        # markieren
        if (img[:, :, 1:2] < limite).sum() > 500:
            print("UFO-Alarm:", f)
            fig = plt.figure()
            toptit = 'UFO Alarm in Bild ' + f
            fig.suptitle(toptit)
            plt.subplot(211)
            plt.title('Original')
            plt.imshow(img)
            c = (img[:, :, 1] < limite).sum()
            img[:, :, 0][img[:, :, 1] < limite] = 200
            ax = plt.subplot(212)
            plt.title('Anomalien')
            titel2 = str(c) + " Pixel erkannt"
            plt.imshow(img)
            ax.text(0.95, 0.01, titel2,
                    verticalalignment='bottom', horizontalalignment='right',
                    transform=ax.transAxes,
                    color='red', fontsize=10)

            plt.subplots_adjust(hspace=0.5, wspace=1.0)
            bildname = 'tmp/' + 'UFO_' + f
            fig.savefig(bildname)
        else:
            print(bild, "ist harmlos")

        # Meldung zum Abschluss des Prozesses senden
        prozcont = "Stop." + str(pid)
        ap.send(prozcont)


def check_pid():
    '''
    Prozess-ID aufnehmen und am Schluss wieder löschen
    '''
    pid = bp.recv().split('.')
    if pid[0] == 'Start':
        proz.append(pid[1])
    else:
        proz.remove(pid[1])

    # Prüfen ob maximale Anzahl Prozesse erreicht ist
    if len(proz) >= maxproz:
        print(
            "Es sind",
            len(proz),
            "Prozesse am Laufen, warte für",
            warten,
            "Sekunden")
        time.sleep(warten)


# Main
# Bilder auflisten
for f in bilder:
    px = Process(target=analyse, args=(f,))
    px.start()
    check_pid()
