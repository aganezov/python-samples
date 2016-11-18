# -*- coding: utf-8 -*-
from collections import namedtuple
import sqlite3


Entry = namedtuple("DBEntry", ['age', 'name'])


conn = sqlite3.connect("../example.db")
c = conn.cursor()

for row in c.execute("SELECT * from JBGWUTable1 WHERE JBAge < 30"):
    print(Entry(row))


























# print("First selection")
for row in c.execute("SELECT * from JBGWUTable1 ORDER BY JBAge"):
    pass

# print("Second selection")
for row in c.execute("SELECT * from JBGWUTable1 WHERE JBAge < 30 ORDER BY length"):
    pass
