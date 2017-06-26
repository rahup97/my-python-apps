import psycopg2 as psy

def create_table():
    conn = psy.connect("dbname = 'database1' user = 'postgres' password = 'post123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quant, price):
    conn = psy.connect("dbname = 'database1' user = 'postgres' password = 'post123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quant, price))              #to prevent SQL injections
    conn.commit()
    conn.close()

def view():
    conn = psy.connect("dbname = 'database1' user = 'postgres' password = 'post123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    data = cur.fetchall()
    conn.close()
    return data

def delete(item):
    conn = psy.connect("dbname = 'database1' user = 'postgres' password = 'post123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item = %s", (item,))
    conn.commit()
    conn.close()

def update(quant, price, item):
    conn = psy.connect("dbname = 'database1' user = 'postgres' password = 'post123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quant, price, item))
    conn.commit()
    conn.close()


create_table()
print(view())
