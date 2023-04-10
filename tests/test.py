#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2616:18
# 文件名称：test.py
# 开发工具：PyCharm

import sqlite3
import tkinter as tk
from tkinter import ttk

# Connect to the database
conn = sqlite3.connect('path/to/database.db')
c = conn.cursor()

# Create a new window
root = tk.Tk()

# Create a table widget
table = ttk.Treeview(root)

# Define the columns
table['columns'] = ('id', 'name', 'age', 'gender')

# Format the columns
table.column('#0', width=0, stretch=tk.NO)
table.column('id', anchor=tk.CENTER, width=100)
table.column('name', anchor=tk.CENTER, width=100)
table.column('age', anchor=tk.CENTER, width=100)
table.column('gender', anchor=tk.CENTER, width=100)

# Create the headings
table.heading('#0', text='', anchor=tk.CENTER)
table.heading('id', text='ID', anchor=tk.CENTER)
table.heading('name', text='Name', anchor=tk.CENTER)
table.heading('age', text='Age', anchor=tk.CENTER)
table.heading('gender', text='Gender', anchor=tk.CENTER)

# Retrieve the data from the database
c.execute('SELECT * FROM mytable')
rows = c.fetchall()

# Add the data to the table
for row in rows:
    table.insert(parent='', index='end', iid=row[0], values=row)

# Pack the table into the window
table.pack()

# Run the tkinter event loop
root.mainloop()

# Close the database connection
conn.close()