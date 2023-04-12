import sqlite3
import os
import uuid
import tkinter as tk
from tkinter import ttk


def insert_data(title, time, notes, location, image_paths):
    conn = sqlite3.connect(r'D:/UserFiles/文档\GitHub/bookNotesProject/db/data/mydatabase.db')
    c = conn.cursor()

    # Create a table to store the events
    c.execute('''CREATE TABLE IF NOT EXISTS event_table
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         event_id TEXT NOT NULL,
                         title TEXT NOT NULL,
                         time TEXT NULL,
                         notes TEXT NULL,
                         location TEXT NULL);''')

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

def get_table_data(database_path):
    # the default database opened is "mydatabase.db"
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute('pragma table_info(event_table)')

    # Get all headings of the table
    col_names = c.fetchall()
    col_names = [x[1] for x in col_names]

    # Get all rows from the table
    c.execute('SELECT * FROM event_table')
    rows = c.fetchall()

    conn.close()

    return col_names, rows

    # Create a new window to show data from database
    root = tk.Tk()
    root.title("Notepad")

    # Create a frame to hold the table and buttons
    frame = tk.Frame(root)
    frame.pack(side="top", fill="both", expand=True)

    # Create a table widget
    style = ttk.Style()
    style.configure("Treeview.Heading", rowheight=400)
    style.configure("Treeview", rowheight=30)
    table = ttk.Treeview(frame)
    table.pack(side="left", fill="both", expand=True)

    # Define the columns
    table['columns'] = col_names

    # Format the columns
    table.column('#0', width=0, stretch=tk.NO)
    for col_name in col_names:
        table.column(str(col_name), anchor=tk.CENTER, width=100)

    # Create the headings
    table.heading('#0', text='', anchor=tk.CENTER)
    for col_name in col_names:
        table.heading(str(col_name).lower(), text=str(col_name), anchor=tk.CENTER)

    # Add the data to the table
    for row in rows:
        table.insert(parent='', index='end', iid=row[0], values=row)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(frame)
    button_frame.pack(side="right", fill="y")
    tk.Frame(button_frame, height=25).pack(side="top", fill="x")

    # Create a button for each row in the table
    for item in table.get_children():
        button = tk.Button(button_frame, text="Edit")
        button.configure(width=5, height=1)
        button.pack(side="top", fill="x")

    # Run the tkinter event loop
    root.mainloop()


    pass