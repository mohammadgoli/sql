#!/usr/bin/python
#importin from csv 
import csv 
import sqlite3

table = sqlite3.connect('thetable.db')

crs = table.cursor()

data = csv.reader(open('employees.csv', 'r'))

#crs.execute("CREATE TABLE emp(first TEXT, last TEXT)")

crs.executemany("INSERT INTO emp(first, last) VALUES (?, ?)", data)

table.commit()

table.close()

