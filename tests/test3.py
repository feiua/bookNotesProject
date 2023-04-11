import sqlite3

# the default database opened is "mydatabase.db"
conn = sqlite3.connect(r'D:/UserFiles/文档\GitHub/bookNotesProject/db/data/mydatabase.db')
c = conn.cursor()
c.execute('pragma table_info(event_table)')
data = c.fetchall()
col_names = [x[1] for x in data]
print(col_names)

# print rows of event_table
c.execute('SELECT * FROM event_table')
rows = c.fetchall()
for row in rows:
    print(row)


conn.close()
