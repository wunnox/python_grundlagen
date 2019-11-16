#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

log = os.popen("ping -c 1 google.com").readlines()

for zeile in log:
    print(zeile.replace("\n", ""))

# oder

if os.system("ping -c 1 google.com") == 0:
    print("IP ist erreichbar")
else:
    print("IP ist NICHT erreichbar")
