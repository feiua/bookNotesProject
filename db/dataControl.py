import sqlite3
import os


def insert_data(title, time, notes, location, image_path):
    conn = sqlite3.connect(r'D:/UserFiles/文档\GitHub/bookNotesProject/db/data/mydatabase.db')
    c = conn.cursor()

    # Create a table to store the events
    c.execute('''CREATE TABLE IF NOT EXISTS event_database
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         title TEXT NOT NULL,
                         time TEXT NOT NULL,
                         note TEXT NOT NULL,
                         location TEXT NOT NULL);''')

    # Create a table to store the images
    conn.execute('''CREATE TABLE IF NOT EXISTS images
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     event_id INTEGER NOT NULL,
                     name TEXT NOT NULL,
                     data BLOB NOT NULL,
                     FOREIGN KEY (event_id) REFERENCES events(id));''')

    # Insert the event data into the database
    c.execute("INSERT INTO my_table (title, time, notes, location) VALUES (?, ?, ?, ?, ?)",
              (title, time, notes, location))
    event_id = conn.lastrowid

    # Read the image data from files
    for image_path in image_path:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_name = os.path.basename(image_path)
        conn.execute('INSERT INTO images (event_id, name, data) VALUES (?, ?, ?)',
                     (event_id, image_name, image_data))

    c.execute('''CREATE TABLE IF NOT EXISTS mytable
                         (title TEXT, time TEXT, notes TEXT, location TEXT, image BLOB)''')
    c.execute("INSERT INTO my_table (title, time, notes, location, image) VALUES (?, ?, ?, ?, ?)",
              (title, time, notes, location, image))
    conn.commit()
    conn.close()