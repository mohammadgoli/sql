#!/usr/bin/python
#insert command 

import sqlite3 

table = sqlite3.connect("thetable.db")

crs = table.cursor()

cities = [
		('Boston', 'MA', 600000),
		('Chicago', 'IL', 2700000),
		('Hoston', 'TX', 2100000),
		('Phoenix', 'AZ', 1500000)
		 ]

crs.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

table.commit()

table.close()


