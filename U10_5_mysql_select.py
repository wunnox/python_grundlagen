#!/usr/bin/python3
##############################################
#
# Name: U10_5_mysql_select.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Liest Daten aus mysql-DB aus
#
##############################################

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "kurs0", "kurs", "Enterprise")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Fetch a single row using fetchone() method.
cursor.execute("SELECT * FROM person")
for row in cursor:
    print(row[0], row[1], row[2], row[3])


# disconnect from server
db.close()
