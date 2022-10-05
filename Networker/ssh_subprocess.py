#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
##############################################
#
# Name: ssh_subprocess.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 03.11.2018 1.0
#
# Purpose: Ausführen eines ssh Kommandos auf einem Remote-Server
#
##############################################

import subprocess

#SSH-Kommando auf remote Host starten
#print("ssh-Kommando auf remote Host starten")
print("ssh-Kommando auf remote Host starten")
ssh = subprocess.Popen(["ssh", "pi@192.168.1.50", "ls -l max"],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

#Irgend etwas anders machen
print("Mache etwas anderes:")
print([x for x in range(10)])

#Auswerten des Resultates
print("Ergebnis von ssh abfragen und ausgeben:")
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()

    #Fehlermeldungen sollen rot angezeigt werden
    print ('\033[0;31m')
    for e in error:
       print ("ERROR:", e[:-1].decode('utf8'))
    print('\033[0;30m')
else:
    for r in result:
       print (r[:-1].decode('utf8'))
