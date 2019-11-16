import mysql.connector

# Verbindung und Cursor erzeugen
connection = mysql.connector.connect(user='kurs0', password='kurs',
                                     host='192.168.154.36',
                                     database='firma')

cursor = connection.cursor()
