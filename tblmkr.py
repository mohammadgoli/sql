import sqlite3 

table = sqlite3.connect("thetable.db")

crs = table.cursor()

crs.execute("""CREATE TABLE population
				(city TEXT, state TEXT, population INT)
				""")
table.close()
