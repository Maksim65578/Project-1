import sqlite3
import os

con = sqlite3.connect("products.db")

cur = con.cursor()


def add(*inf):
    print(inf)
    insert = """INSERT INTO
     products (title, price, number, descryption, picture)
     VALUES 
     (?, ?, ?, ?, ?);
     """
    cur.execute(insert, inf)
    con.commit()


def get(id):
    select = f"""SELECT title, price, number FROM products WHERE ID = {id}"""
    inf = cur.execute(select).fetchall()
    return list(inf)


def change(*inf):
    new_inf = list(inf[1:])
    new_inf.append(inf[0])
    data = tuple(new_inf)
    print(data)
    update = """UPDATE products
    SET title = ?,
    price = ?,
    number = ?,
    descryption = ?,
    picture = ?
    WHERE ID = ?"""
    cur.execute(update, data).fetchall()
    con.commit()


con.close()
