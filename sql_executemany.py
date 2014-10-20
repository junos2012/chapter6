#if you need to execute many of the same SQL statements you can use the#
#executemany() method 

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	cities = [
	('boston', 'MA', 6000000),
	('chicago', 'IL', 2700000),
	('houston', 'TX', 1500000),
	('pheonix', 'AZ', 2100000)
	]

	#insert data into table
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)