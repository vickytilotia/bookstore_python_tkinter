import sqlite3  
#connect to a database
#create a  cursor object
#write an sql query
#commit changes
#Close database connections

conn = sqlite3.connect("lite.db")
cur = conn.cursor()
cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
conn.commit()
conn.close()