####################################################
#
# Uebung:
# Das Python Script „UB7_2_singing_V2.py“ ist in der Version Python 2
# Konvertieren Sie das Script nach Python 3
# Erstellen Sie dafür das Verzeichnis p3 mit dem Kommando „mkdir p3“
# Was müssen Sie am Schluss noch manuell anpassen, damit das Script läuft?
#
####################################################

mkdir p3

2to3 - wno p3 UB7_2_singing_V2.py

# Anschliessend muss noch die erste Zeile angepasst werden
# von /usr/bin/python -> /usr/bin/python3
#
# Auch müssen die Zeilen mit ss2=ss*fs und es2=es*fs neu mit einer int-Funktion
# versehen werden -> ss2=int(ss*fs) , es2=int(es*fs)
