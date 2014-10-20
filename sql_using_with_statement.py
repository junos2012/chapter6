#tidier way of executing commands on a SQL db using with statement and executemany()
import sqlite3

with sqlite3.connect("new.db") as connection:		#using the with keywork will commit your changes to the db automatically
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 8000000)")
	c.execute("INSERT INTO population VALUES('Leeds', 'WY', 6000000)")