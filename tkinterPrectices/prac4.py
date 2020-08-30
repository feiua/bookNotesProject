#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-30 17:31
# @Author  : Jianfei Chen
# @Site    : 
# @File    : prac4.py
# @Software: PyCharm

"""
输入框组件练习
tkinter.Entry,
"""

from tkinter import *

root = Tk()


def func1():
    Label(root, text='the work: ').grid(row=0, column=0)
    Label(root, text='the author: ').grid(row=1, column=0)

    e1 = Entry(root)
    e2 = Entry(root)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    def show():
        print('the work: %s ' % e1.get())
        print('the author: %s ' % e2.get())

    Button(root, text='get information', width=10, command=show) \
        .grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Button(root, text='exit', width=10, command=root.quit) \
        .grid(row=2, column=1, sticky=E, padx=10, pady=5)


def func2():
    Label(root, text='account: ').grid(row=0, column=0)
    Label(root, text='password: ').grid(row=1, column=0)

    v1 = StringVar()
    v2 = StringVar()

    e1 = Entry(root, textvariable=v1)
    e2 = Entry(root, textvariable=v2, show='*')
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    def show():
        print('account: %s ' % e1.get())
        print('password: %s ' % e2.get())

    Button(root, text='go for it', width=10, command=show) \
        .grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Button(root, text='exit', width=10, command=root.quit) \
        .grid(row=2, column=1, sticky=E, padx=10, pady=5)


def func3():
    def test():
        if e1.get() == "小甲鱼":
            print("正确！")
            return True
        else:
            print("错误！")
            e1.delete(0, END)
            return False

    v = StringVar()

    e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=test)
    e2 = Entry(root)
    e1.pack(padx=10, pady=10)
    e2.pack(padx=10, pady=10)


def func4():
    v = StringVar()

    def test(content, reason, name):
        if content == "小甲鱼":
            print("正确！")
            print(content, reason, name)
            return True
        else:
            print("错误！")
            print(content, reason, name)
            return False

    testCMD = root.register(test)
    e1 = Entry(root, textvariable=v, validate="focusout",
               validatecommand=(testCMD, '%P', '%v', '%W'))
    e2 = Entry(root)
    e1.pack(padx=10, pady=10)
    e2.pack(padx=10, pady=10)


def func5():
    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()

    def test(content):
        return content.isdigit()

    testCMD = root.register(test)  # 这里不要改成 frame

    e1 = Entry(frame, textvariable=v1, validate="key", width=10,
               validatecommand=(testCMD, '%P')).grid(row=0, column=0)

    Label(frame, text='+').grid(row=0, column=1)

    e2 = Entry(frame, textvariable=v2, validate="key", width=10,
               validatecommand=(testCMD, '%P')).grid(row=0, column=2)

    Label(frame, text='=').grid(row=0, column=3)

    e3 = Entry(frame, textvariable=v3, state='readonly', width=10, ).grid(row=0, column=4)

    def calc():
        result = int(v1.get()) + int(v2.get())
        v3.set(str(result))

    Button(frame, text='result', command=calc) \
        .grid(row=1, column=2, padx=5, pady=5)


runcode = int(input('press 1 or 2 or 3 or 4 or 5: '))

if runcode == 1:
    func1()
elif runcode == 2:
    func2()
elif runcode == 3:
    func3()
elif runcode == 4:
    func4()
elif runcode == 5:
    func5()

root.mainloop()
