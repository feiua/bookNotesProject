#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-31 11:08
# @Author  : Jianfei Chen
# @Site    : 
# @File    : prac6.py
# @Software: PyCharm

"""
Text 组件练习
"""

from tkinter import *

root = Tk()


def func1():
    textWidget1 = Text(root, width=30, height=2)
    textWidget1.pack()

    textWidget1.insert(INSERT, 'some add \n')
    textWidget1.insert(END, 'some add2')

    def show():
        print('Oh, a hit...')

    b1 = Button(textWidget1, text='here we go', command=show)
    textWidget1.window_create(INSERT, window=b1)


def func2():
    textWidget1 = Text(root, width=30, height=50)
    textWidget1.pack()

    photo1 = PhotoImage(
        file=r'E:\PythonCode\practices\myPractice4DataBase'
             r'\tkinterPrectices\images\pic1.png')

    def show():
        textWidget1.image_create(END, image=photo1)

    b1 = Button(textWidget1, text='here we go', command=show)
    textWidget1.window_create(INSERT, window=b1)


# tag 练习
def func3():
    textWidget1 = Text(root, width=30, height=5)
    textWidget1.pack()

    textWidget1.insert(INSERT, 'something bigger than yourself')

    textWidget1.tag_add('tag1', '1.7', '1.12', '1.14')
    textWidget1.tag_config('tag1', background='yellow', foreground='red')
    # 如果新建一个 tag 会覆盖掉旧的 tag
    textWidget1.tag_add('tag2', '1.7', '1.12', '1.14')
    textWidget1.tag_config('tag2', foreground='blue')

# tag 事件绑定
def func4():
    textWidget1 = Text(root, width=30, height=5)
    textWidget1.pack()

    textWidget1.insert(INSERT, 'something bigger than yourself')

    textWidget1.tag_add('link', '1.7', '1.5')
    textWidget1


runcode = int(input('Press 1 or 2: '))

if runcode == 1:
    func1()
elif runcode == 2:
    func2()
elif runcode == 3:
    func3()

root.mainloop()
