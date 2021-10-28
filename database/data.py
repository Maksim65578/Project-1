import sqlite3
import os

global con, cur


def open():
    global con, cur
    con = sqlite3.connect("database/products.db")
    cur = con.cursor()


def add(*inf):
    open()
    print(inf)
    insert = """INSERT INTO
     products (title, price, number, descryption, picture)
     VALUES 
     (?, ?, ?, ?, ?);
     """
    cur.execute(insert, inf)
    con.commit()
    close()


def get():
    open()
    select = """SELECT title, price, number FROM products"""
    inf = cur.execute(select).fetchall()
    close()
    print(inf)
    return list(inf)


def change(*inf):
    open()
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
    close()


def close():
    con.close()
