import sqlite3
#create connection exisitng db
conn = sqlite3.connect("new.db")
#create cursor for executing queries
cursor = conn.cursor()
#create your sql query
cursor.execute("INSERT INTO population VALUES('NYC', 'NY', 8200000)")	#notice the population field does not have 
#commit the sql query / changes to db   								#quotes around it as it's supposed to be an INT not a 'STRING'
conn.commit() 
#close the connection to the db
conn.close()