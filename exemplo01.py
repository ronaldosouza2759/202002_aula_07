import sqlite3

conn = sqlite3.connect('exemplo.db')
c = conn.cursor()
c.execute('''create table texte(data text, qtde real)''')

c.execute("Insert into teste values('2020-09-25', 7)")

conn.commit()
conn.close()