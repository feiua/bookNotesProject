import sqlite3
import tkinter as tk
from tkinter import ttk


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

# Create a new window
root = tk.Tk()

# Create a frame to hold the table and buttons
frame = tk.Frame(root)
frame.pack(side="top", fill="both", expand=True)

# Create a table widget
table = ttk.Treeview(frame)
style = ttk.Style()
style.configure("Treeview.Heading", rowheight=400)
style.configure("Treeview", rowheight=30)
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
button = tk.Button(button_frame, text="")
button.configure(height=1)
button.pack()
# button.pack_forget()

# Create a button for each row in the table
for item in table.get_children():
    button = tk.Button(button_frame, text="Edit")
    button.pack(side="top", fill="x")

# Run the tkinter event loop
root.mainloop()
conn.close()