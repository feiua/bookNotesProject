#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-30 20:52
# @Author  : Jianfei Chen
# @Site    : 
# @File    : prac5.py
# @Software: PyCharm

"""
Listbox、Scale 组件练习
"""

from tkinter import *

master = Tk()


def func1():
    theLB = Listbox(master, selectmode=EXTENDED)
    theLB.pack()

    for item in ['1', '2', '3', '4']:
        theLB.insert(END, item)

    theButton = Button(master, text='delete',
                       command=lambda x=theLB: x.delete(ACTIVE)).pack()


def func2():
    theLB = Listbox(master, selectmode=EXTENDED)
    theLB.pack()

    for item in range(11):
        theLB.insert(END, item)


def func3():
    sb = Scrollbar(master)
    sb.pack(side=RIGHT, fill=Y)

    lb = Listbox(master, yscrollcommand=sb.set)

    for item in range(100):
        lb.insert(END, item)

    lb.pack(side=LEFT, fill=BOTH)

    sb.config(command=lb.yview)


def func4():
    sc1 = Scale(master, from_=0, to=42,
                tickinterval=5,  # 刻度设置
                resolution=5,  # 精度设置
                length=200)
    sc1.pack()

    sc2 = Scale(master, from_=0, to=200, orient=HORIZONTAL,
                tickinterval=10, length=600)
    sc2.pack()

    def show():
        print(sc1.get(), sc2.get())

    Button(master, text='get position', command=show).pack()


runcode = int(input('press 1 or 2 or 3 or 4: '))

if runcode == 1:
    func1()
elif runcode == 2:
    func2()
elif runcode == 3:
    func3()
elif runcode == 4:
    func4()

master.mainloop()
