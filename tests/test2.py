#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : unset
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2023-04-1313:18
# 文件名称：test2.py
# 开发工具：PyCharm

import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

frame.columnconfigure(1, weight=1)

label = tk.Label(frame, text="Label", width=10)
label.grid(row=0, column=0, sticky="e")

entry = tk.Entry(frame)
entry.grid(row=0, column=1, sticky="ew")

root.mainloop()
