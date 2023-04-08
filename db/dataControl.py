import sqlite3
import os
import uuid


def insert_data(title, time, notes, location, image_paths):
    conn = sqlite3.connect(r'D:/UserFiles/文档\GitHub/bookNotesProject/db/data/mydatabase.db')
    c = conn.cursor()

    # Create a table to store the events
    c.execute('''CREATE TABLE IF NOT EXISTS event_table
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         event_id TEXT NOT NULL,
                         title TEXT NOT NULL,
                         time TEXT NOT NULL,
                         notes TEXT NOT NULL,
                         location TEXT NOT NULL);''')

    # Create a table to store the images
    conn.execute('''CREATE TABLE IF NOT EXISTS image_table
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     event_id TEXT NOT NULL,
                     name TEXT NOT NULL,
                     data BLOB NOT NULL,
                     FOREIGN KEY (event_id) REFERENCES event_table(event_id));''')

    # Insert the event data into the database
    event_id = uuid.uuid4()
    c.execute("INSERT INTO event_table (event_id, title, time, notes, location) VALUES (?, ?, ?, ?, ?)",
              (str(event_id), title, time, notes, location))
    print(event_id)

    # Read the image data from files
    for each_image_path in image_paths:
        with open(each_image_path, 'rb') as f:
            image_data = f.read()
        image_name = os.path.basename(each_image_path)
        conn.execute('INSERT INTO image_table (event_id, name, data) VALUES (?, ?, ?)',
                     (str(event_id), image_name, image_data))

    conn.commit()
    conn.close()