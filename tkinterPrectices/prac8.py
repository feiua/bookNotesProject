#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : https://www.bilibili.com/video/BV1xs411Q799?p=75
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：2020-09-0812:19 AM
# 文件名称：prac8.py
# 开发工具：PyCharm

"""
事件绑定
"""

from tkinter import *


root = Tk()


def button_1(event):
    print('Button-1', event.x, event.y)


def keeey(event):
    print(event.char)


def motion(event):
    print('motion:', event.x, event.y)


frame = Frame(root, width=200, height=200)
frame.bind('<Button-1>', button_1)

frame.bind('<Key>', keeey)
frame.focus_set()

frame.bind('<Motion>', motion)
frame.pack()

root.mainloop()
