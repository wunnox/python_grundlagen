#!/usr/bin/python3
####################################################
#
# Uebung:
# Erstellen Sie folgendes Tupel: 
# tup=('Peter','Hans','Fred','Hans','Ursula','Rob','Ursula')
#
# Listen Sie jeden Namen in obigem Tupel nur einmal auf gefolgt von einer Zahl, 
# die angibt, wie oft dieser Name im Tupel vorkommt. 
# Lösen Sie die Aufgabe einmal mit einem Dictionary und einmal mit einem Set.
#
# Geben Sie das Resultat auf dem Bildschirm aus
#
####################################################

#### Lösung: ####

tup = ('Peter', 'Hans', 'Fred', 'Hans', 'Ursula', 'Robert', 'Ursula')
dic = {}

#Version 1
for name in tup:
    if name in dic.keys():
        dic[name] += 1
    else:
        dic[name] = 1

'''
#Version 2
for name in tup:
    if name not in dic.keys():
        dic[name]=tup.count(name)

#Version 3
s=set(tup)
for name in s:
    dic[name]=tup.count(name)
'''

#Ausgabe
for name, wert in dic.items():
    print(name, wert)


