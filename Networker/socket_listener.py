#! env python3
##############################################
#
# Name: socket_listener.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Startet einen tcp-Listener und wartet auf Daten
#
##############################################

import socket

#Variabeln
port=10000

# TCP/IP Socket erstellen
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket mit einem Port verbinden
server_address = ('localhost', port)
print ("Starte Listener auf Port:",port)
sock.bind(server_address)

# Auf eingehende Verbindungen warten
sock.listen(1)
print ("Warte auf Verbindung")

while True:
    connection, client_address = sock.accept()

    while True:
       data = connection.recv(16)
       if data:
          try:
             print ("Eingehende Daten von", client_address, ":", data.decode('utf8'))
          except:
             print ("Verbindungsabbruch")
       else:
          break
   
