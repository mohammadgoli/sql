#!/usr/bin/python
import sqlite3

with sqlite3.connect('thetable.db') as db:
	crs = db.cursor()
	crs.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City'")
	print "\nNEW DATA:\n"

	crs.execute("DELETE FROM population WHERE city = 'Boston'")
	crs.execute("SELECT * FROM population")


	rows = crs.fetchall()

	for row in rows:
		print row[0], row[1], row[2]