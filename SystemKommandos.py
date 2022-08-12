#!/usr/bin/python3
##############################################
#
# Name: SystemKommandos.py
#
# Author: Peter Christen
#
# Version: 1.1
#
# Date: 05.11.2015 V1.0
#
# Purpose: Beispiele mit os.popen und os.system
#
##############################################

import os

log = os.popen("ping -c 1 google.com").readlines()

for zeile in log:
    print(zeile.replace("\n", ""))

# oder

if os.system("ping -c 1 google.com") == 0:
    print("IP ist erreichbar")
else:
    print("IP ist NICHT erreichbar")
