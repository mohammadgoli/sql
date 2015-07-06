#!/usr/bin/python
import sqlite3

with sqlite3.connect('thetable.db') as db:
	crs = db.cursor()

	sql = {'avg' : "SELECT avg(population) FROM population",
			'max' : "SELECT max(population) FROM population",
			'min' : "SELECT min(population) FROM population",
			'sum' : "SELECT sum(population) FROM population",
			'cnt' : "SELECT count(city) FROM population" }

	for keys, values in sql.iteritems():

		crs.execute(values)
		res = crs.fetchone()

		print keys + ":" , res[0]
		
