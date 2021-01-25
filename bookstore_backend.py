import sqlite3  

class Database:

    def __init__(self):
        #init is a constructor
        #when we call this class this function will work automatically
        #but for other functions, It is required to call the function.
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()
        conn.close()


    def insert(self,title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        conn.commit()
        conn.close()


    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("select * from book where  title =? OR author=? OR year=? OR isbn =?",(title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows


    def delete(self,id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()
        

    def update(self,id="",title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id = ?", (title, author, year, isbn,id))
        conn.commit()
        conn.close()



