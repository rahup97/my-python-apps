import sqlite3 as sql

class Database:

    def __init__(self):
        self.conn = sql.connect("student.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS marks (id INTEGER PRIMARY KEY, course TEXT, credits INTEGER, int1 REAL, int2 REAL, int3 REAL, labself REAL)")
        self.conn.commit()


    def insert(self, course, credits, int1=0, int2=0, int3=0, labss=0):
        self.cur.execute("INSERT INTO marks VALUES (NULL, ?, ?, ?, ?, ?, ?)", (course, credits, int1, int2, int3, labss))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM marks")
        data = self.cur.fetchall()
        return data

    def search(self, course="", credits="", int1="", int2="", int3="", labss=""):
        self.cur.execute("SELECT * FROM marks WHERE course = ? OR credits = ?", (course, credits))
        data = self.cur.fetchall()
        return data

    def delete(self, id):
        self.cur.execute("DELETE FROM marks WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, course, credits, int1, int2, int3, labss):
        self.cur.execute("UPDATE marks SET course = ?, credits = ?, int1 = ?, int2 = ?, int3 = ?, labself = ? WHERE id = ?", (course, credits, int1, int2, int3, labss, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
