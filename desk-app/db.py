import sqlite3 as sql
import pyscopg2

def create_table():
    conn = sql.connect("app_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quant, price):
    conn = sql.connect("app_db.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)",(item, quant, price))
    conn.commit()
    conn.close()

def view():
    conn = sql.connect("app_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    data = cur.fetchall()
    conn.close()
    return data

def delete(item):
    conn = sql.connect("app_db.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item = ?", (item,))
    conn.commit()
    conn.close()

def update(quant, price, item):
    conn = sql.connect("app_db.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quant, price, item))
    conn.commit()
    conn.close()

create_table()
