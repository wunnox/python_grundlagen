#! env python3
##############################################
#
# Name: socket_client.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Verbindet auf einen remote Port und sendet Daten
#
##############################################

import socket

#Variabeln
port=10000
host="localhost"

# TCP/IP Socket erstellen
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Auf remote Port verbinden
server_address = (host, port)
print ("Erstelle Verbindung mit", server_address)
sock.connect(server_address)

# Daten senden
while True:
   message=input('-> ')
   if message=='quit':
      break
   print ("Sende Meldung:", message)
   sock.sendall(bytes(message, 'utf-8'))
