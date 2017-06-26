import sqlite3 as sql

def connect():
    conn = sql.connect("student.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS marks (id INTEGER PRIMARY KEY, course TEXT, credits INTEGER, int1 REAL, int2 REAL, int3 REAL, labself REAL)")
    conn.commit()
    conn.close()

def insert(course, credits, int1, int2, int3, labss):
    conn = sql.connect("student.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO marks VALUES (NULL, ?, ?, ?, ?, ?, ?)", (course, credits, int1, int2, int3, labss))
    conn.commit()
    conn.close()

def view():
    conn = sql.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM marks")
    data = cur.fetchall()
    conn.close()
    return data

def search(course="", credits="", int1="", int2="", int3="", labss=""):
    conn = sql.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM marks WHERE course = ? OR credits = ?", (course, credits))
    data = cur.fetchall()
    conn.close()
    return data

def delete(id):
    conn = sql.connect("student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM marks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, course, credits, int1, int2, int3, labss):
    conn = sql.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE marks SET course = ?, credits = ?, int1 = ?, int2 = ?, int3 = ?, labself = ? WHERE id = ?", (course, credits, int1, int2, int3, labss, id))
    conn.commit()
    conn.close()

connect()       #must always run whenever program is opened
