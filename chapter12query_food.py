import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE id="01009"'
print(query)

curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names,row):
        print('%s: %s'%pair)
    print()