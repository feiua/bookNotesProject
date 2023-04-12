#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2616:18
# 文件名称：test.py
# 开发工具：PyCharm

import sqlite3
import os
import uuid
import tkinter as tk
from tkinter import ttk

# the default database opened is "mydatabase.db"
conn = sqlite3.connect(r'D:/UserFiles/文档\GitHub/bookNotesProject/db/data/mydatabase.db')
c = conn.cursor()
c.execute('pragma table_info(event_table)')

# Get all headings of the table
col_names = c.fetchall()
col_names = [x[1] for x in col_names]

# Get all rows from the table
c.execute('SELECT * FROM event_table')
rows = c.fetchall()

conn.close()

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