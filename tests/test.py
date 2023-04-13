#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2616:18
# 文件名称：test.py
# 开发工具：PyCharm

import tkinter as tk

root = tk.Tk()

# place frames
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

frame.columnconfigure(0, minsize=10)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, minsize=20)

right_frame = tk.Frame(frame, height=50, width=10)
right_frame.grid(row=0, column=2, sticky="nsew")

# place label and entry
label = tk.Label(frame, text="Label", width=10)
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, sticky="ew")

root.mainloop()
