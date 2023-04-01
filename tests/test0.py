import sqlite3


def insert_data(time, location, person, event, image):
    conn = sqlite3.connect('D:/UserFiles/文档\GitHub/bookNotesProject/db/data/mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mytable
                 (time TEXT, location TEXT, person TEXT, event TEXT, image BLOB)''')
    c.execute("INSERT INTO mytable (time, location, person, event, image) VALUES (?, ?, ?, ?, ?)",
              (time, location, person, event, image))
    conn.commit()
    conn.close()

