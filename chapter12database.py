import sqlite3
conn = sqlite3.connect('database.db')
curs = conn.cursor()
conn.close()