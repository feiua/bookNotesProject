#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2616:18
# 文件名称：test.py
# 开发工具：PyCharm


import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Resizable Entry")

# Create Toplevel window
top = tk.Toplevel(root)
top.title("Resizable Entry")

# Create Entry widget
entry = tk.Entry(top)
entry.grid(row=0, column=0, sticky="nsew")

# Configure grid
top.grid_rowconfigure(0, weight=1)
top.grid_columnconfigure(0, weight=1)

# Run main loop
root.mainloop()
