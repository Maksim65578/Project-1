import sqlite3
import os

con = sqlite3.connect("products.db")

cur = con.cursor()


def add(*inf):
    items = list(inf)
    a = ["'" + i + "'" for i in items]
    cur.execute(f"INSERT INTO products VALUES({', '.join(a)})")

    res = cur.execute("""SELECT * FROM products""").fetchall()
    return ID + 1


ID = add("Meat", "100", "5", "Amazing", "None")
print(ID)
ID = add("Meat", "100", "5", "Amazing", "None")
print(ID)

con.close()
