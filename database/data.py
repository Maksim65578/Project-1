import sqlite3
import os

con = sqlite3.connect("products.db")

cur = con.cursor()


def add():
    insert = """INSERT INTO products VALUES (0, 'demo-test', 10, 10, 'hehe','None')"""
    res = cur.execute(insert).fetchall()
    print(res)


def get(id):
    select = f"""SELECT (title, price, number) FROM products WHERE ID = {id}"""
    inf = cur.execute(select).fetchall()
    return inf


add()
print(get(0))

con.close()
