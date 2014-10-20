#create a sqlite3 database and table

#import sqllite3
import sqlite3

#create a new database
conn = sqlite3.connect("new.db")

#create a cursor object used to execuet SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population
	(city TEXT, state TEXT, population INT)
	""")

#close the database connection
conn.close()