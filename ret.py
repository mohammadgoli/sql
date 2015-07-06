#!/usr/bin/python
#sql retriver 
import sqlite3

with sqlite3.connect('thetable.db') as db:
	crs = db.cursor()
	crs.execute("SELECT first, last FROM emp")

	rows = crs.fetchall()

	for row in rows:
		print row
