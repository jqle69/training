import sqlite3
import os
import pydoc

#os.remove("Cust.db")
conn = sqlite3.connect("Cust.db")

cur = conn.cursor()

cur.execute('''CREATE TABLE inventory (
    itemid integer primary key not null,
    itemname text not null,
    price real null)''')

conn.commit()

cur.execute('''INSERT INTO inventory (itemid, itemname, price)
    VALUES("hammer", 4.00)''')

cur.execute('''INSERT INTO inventory (itemid, itemname, price)
    VALUES("tape", 1.99)''')
#conn.commit()
cur.execute('''SELECT * FROM inventory''')
results = cur.fetchall()

for row in results:
    print(f"{row[0]:0 }")
#conn.close()

