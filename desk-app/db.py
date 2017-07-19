import sqlite3 as sql

def connect():
    conn = sql.connect("faculty.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS faculty (id INTEGER PRIMARY KEY, name TEXT, position TEXT, username TEXT, passw TEXT, permit TEXT, dept TEXT)")
    conn.commit()
    conn.close()

def insert(name, position, username, passw, permit, dept):
    conn = sql.connect("faculty.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO faculty VALUES (NULL, ?, ?, ?, ?, ?, ?)", (name, position, username, passw, permit, dept))
    conn.commit()
    conn.close()

def view():
    conn = sql.connect("faculty.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM faculty")
    data = cur.fetchall()
    conn.close()
    return data

def search(permit="NO", name="", position="", username="", passw="", dept=""):
    conn = sql.connect("faculty.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM faculty WHERE permit = ? OR name = ?", (permit, name))
    data = cur.fetchall()
    conn.close()
    return data

def delete(id):
    conn = sql.connect("faculty.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM faculty WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, name, position, username, passw, permit, dept):
    conn = sql.connect("faculty.db")
    cur = conn.cursor()
    cur.execute("UPDATE faculty SET name = ?, position = ?, username = ?, passw = ?, permit = ?, dept = ? WHERE id = ?", (name, position, username, passw, permit, dept, id))
    conn.commit()
    conn.close()

connect()       #must always run whenever program is opened
