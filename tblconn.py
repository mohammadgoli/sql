#!/usr/bin/python
import sqlite3

with sqlite3.connect('thetable.db') as db:
	crs = db.cursor()

	#crs.execute("""CREATE TABLE regions
				#(city TEXT, region TEXT)
				#""")
	cities = [
			('New York City', 'Northeast'),
			('San Francisco', 'West'),
			('Chicago', 'Midwest'),
			('Houston', 'South'),
			('Phoenix', 'West'),
			('Boston', 'Northeast'),
			('Los Angeles', 'West'),
			('Houston', 'South'),
			('Philadelphia', 'Northeast'),
			('San Antonio', 'South'),
			('San Diego', 'West'),
			('Dallas', 'South'),
			('San Jose', 'West'),
			('Jacksonville', 'South'),
			('Indianapolis', 'Midwest'),
			('Austin', 'South'),
			('Detroit', 'Midwest')
			]


	crs.executemany("INSERT INTO regions VALUES(?, ?)", cities)

	crs.execute("SELECT * FROM regions ORDER BY region ASC")

	rows = crs.fetchall()

	for r in rows: 
		print r[0], r[1]