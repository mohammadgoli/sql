#!/usr/bin/python
import sqlite3

with sqlite3.connect('thetable.db') as db:
	crs = db.cursor()

	crs.execute("""SELECT DISTINCT population.city,
		population.population,
					regions.region FROM population, regions
					WHERE population.city = regions.city ORDER BY population.city ASC
					""")
	rows = crs.fetchall()

	for r in rows:
		print r[0], r[1], r[2]
