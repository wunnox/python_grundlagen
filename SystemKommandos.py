#!/usr/local/bin/python3

import os

log = os.popen("ping -c 1 google.com").readlines()

for zeile in log:
    print(zeile.replace("\n", ""))

# oder

if os.system("ping -c 1 google.com") == 0:
    print("IP ist erreichbar")
else:
    print("IP ist NICHT erreichbar")
