# Welcome to Cursor



# 1. Try generating with command K on a new line. Ask for a pytorch script of a feedforward neural network
# 2. Then, select the outputted code and hit chat. Ask if there's a bug. Ask how to improve.
# 3. Try selecting some code and hitting edit. Ask the bot to add residual layers.
# 4. To try out cursor on your own projects, go to the file menu (top left) and open a folder.

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