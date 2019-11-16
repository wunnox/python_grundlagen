#!/usr/local/bin/python3
##############################################
#
# Name: Beispiele_json.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.11.2017
#
# Purpose: Beispiele mit Json
#
##############################################

import json

#Json2Python
jsonData = '{"name": "UM00365", "Nr.CPU": 4}'
pdict = json.loads(jsonData)

print ("#### Json2Python ####")
print (pdict)
print (pdict['name'])

#Python2Json
pdict = {'name': 'UM00365', 'Nr.CPU': 4}
jsonData = json.dumps(pdict)
print ("#### Python2Json ####")
print (jsonData)

#write Json-File
pdict = {'name': 'UM00365', 'Nr.CPU': 4}
with open('inventar.json', 'w') as outfile:
    json.dump(pdict, outfile)

#read Json-File
pdict = json.load(open('inventar.json'))
print ("#### Read Json ####")
print (pdict)
print (pdict['name'])

