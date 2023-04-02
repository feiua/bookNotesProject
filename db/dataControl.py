import sqlite3


def insert_data(title, time, notes, location, image):
    conn = sqlite3.connect(r'D:/UserFiles/文档\GitHub/bookNotesProject/db/data/mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mytable
                     (title TEXT, time TEXT, notes TEXT, location TEXT, image BLOB)''')
    c.execute("INSERT INTO my_table (title, time, notes, location, image) VALUES (?, ?, ?, ?, ?)",
              (title, time, notes, location, image))
    conn.commit()
    conn.close()
