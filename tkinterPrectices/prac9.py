#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site: https://www.bilibili.com/video/BV1xs411Q799?p=76
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：2020-09-08 9:49 PM
# 文件名称：prac9.py
# 开发工具：PyCharm


"""
Message, Spinbox, PanedWindow, Toplevel 组件
"""

from tkinter import *


root = Tk()

# Message
w1 = Message(root, text='this is a message', width=100)
w1.pack()

w2 = Message(root, text='this is an another message', width=150)
w2.pack()

# Spinbox
w3 = Spinbox(root, from_=0, to=10)
w3.pack()

# PanedWindow
m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text='top pane')
m.add(top)

bottom = Label(m, text='bottom pane')
m.add(bottom)

m1 = PanedWindow(showhandle=True, sashrelief=SUNKEN)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text='left pane')
m1.add(left)

m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
m1.add(m2)

top2 = Label(m2, text='top2 pane')
m2.add(top2)

bottom2 = Label(m2, text='bottom2 pane')
m2.add(bottom2)


# TopLevel
def createTopLevel():
    top = Toplevel()
    top.attributes('alpha', 0.5)
    top.title('a top level text')

    msg = Message(top, text='topLevel message')
    msg.pack()


Button(root, text='create toplevel', command=createTopLevel).pack()

root.mainloop()

