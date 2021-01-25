import psycopg2
#connect to a database
#create a  cursor object
#write an sql query
#commit changes
#Close database connections
def create_table():
    conn = psycopg2.connect("dbname = 'newdb' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname = 'newdb' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)" , (item, quantity, price))
    conn.commit()
    conn.close()



def view():
    conn = psycopg2.connect("dbname = 'newdb' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'newdb' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()
    

def update(quantity,price,item):
    conn = psycopg2.connect("dbname = 'newdb' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

# update(5,10,'vivek')
print(view())
# insert("orange",5,70)
update(50,560,"first")
print(view())

