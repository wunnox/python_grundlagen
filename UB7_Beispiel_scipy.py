#!/usr/bin/python3
##############################################
#
# Name: UB7_Beispiel_scipy.py
#
# Author: Peter Christen /Digicomp
#
# Version: 1.0
#
# Date: 12.01.2016
#
# Purpose: Liest die wav-Datei UB7_Beispiel_singing-female.wav ein
#          und gibt diesen mit matplotlib aus.
#
##############################################

from scipy.io.wavfile import read
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np

# WAV-File
(fs, x) = read('UB7_Beispiel_singing-female.wav')

# Eingangssignal analysieren
print("Eingangssignal")
print("==============")
print("Frequenz", fs)
print("Samples", x.size)
print("Dauer", x.size / float(fs))
print("Max Wert", np.max(abs(x)))

# Ausschnitt aus wav nehmen
ss = 4.0  # Sek Start
es = 4.5  # Sek End

ss2 = int(ss * fs)
es2 = int(es * fs)
y = x[ss2:es2]

print()
print("Ausgangssignal")
print("==============")
print("Samples", y.size)
print("Dauer", y.size / float(fs))

# Ausschnitt in ein neues File schreiben
write('UB7_Beispiel_singing-female_ausschnitt.wav', fs, y)

# Plot Eingangssignal
t = np.arange(x.size) / float(fs)
plt.figure(1)
plt.subplot(211)
plt.title('Eingangssignal')
plt.ylabel('amplitude')
plt.plot(t, x)

# Plot Ausgangssignal
# t2=np.arange(y.size)/float(fs)
t2 = np.arange(ss2, es2) / float(fs)
plt.subplot(212)
plt.title('Ausgangssignal')
plt.xlabel('time in s')
plt.ylabel('amplitude')
plt.plot(t2, y)
plt.show()
