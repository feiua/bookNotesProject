#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2023-03-3013:53
# 文件名称：gtp_version.py
# 开发工具：PyCharm

import tkinter as tk
from tkinter import ttk

# Create a new window
root = tk.Tk()

# Create a table widget
table = ttk.Treeview(root)

# Define the columns
table['columns'] = ('name', 'age', 'gender')

# Format the columns
table.column('#0', width=0, stretch=tk.NO)
table.column('name', anchor=tk.CENTER, width=100)
table.column('age', anchor=tk.CENTER, width=100)
table.column('gender', anchor=tk.CENTER, width=100)

# Create the headings
table.heading('#0', text='', anchor=tk.CENTER)
table.heading('name', text='Name', anchor=tk.CENTER)
table.heading('age', text='Age', anchor=tk.CENTER)
table.heading('gender', text='Gender', anchor=tk.CENTER)

# Add the data
table.insert(parent='', index='end', iid=0, values=('John', 25, 'Male'))
table.insert(parent='', index='end', iid=1, values=('Jane', 30, 'Female'))

# Pack the table into the window
table.pack()

# Run the tkinter event loop
root.mainloop()