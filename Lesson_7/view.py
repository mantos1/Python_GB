import sqlite3
conn = sqlite3.connect('data.db')
cur = conn.cursor()

def get_view_phonebook():
    cur.execute("SELECT * FROM phonebook ORDER BY name")
    data = cur.fetchall()
    for r in data:
        print(f"{r[1]}: {r[2]}")
    conn.close()