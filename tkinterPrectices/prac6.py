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
import webbrowser
import hashlib

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

    textWidget1.tag_add('link', '1.7', '1.16')
    textWidget1.tag_config('link', foreground='blue', underline=True)

    def show_hand_cursor(event):
        textWidget1.config(cursor='arrow')

    def show_xterm_cursor(event):
        textWidget1.config(cursor='xterm')

    def click(event):
        webbrowser.open(r'http://www.fishc.com')

    textWidget1.tag_bind('link', '<Enter>', show_hand_cursor)
    textWidget1.tag_bind('link', '<Leave>', show_xterm_cursor)
    textWidget1.tag_bind('link', '<Button-1>', click)


def func5():
    textWidget1 = Text(root, width=40, height=5)
    textWidget1.pack()

    textWidget1.insert(INSERT, 'something bigger than yourself')
    contents = textWidget1.get('1.0', END)

    def getSig(contents):
        m = hashlib.md5(contents.encode())
        return m.digest()

    sig = getSig(contents)

    def check():
        contents = textWidget1.get('1.0', END)
        if sig != getSig(contents):
            print('Warming, the contents has been changed!')

    Button(root, text='check', command=check).pack()


def func6():
    textWidget1 = Text(root, width=40, height=5)
    textWidget1.pack()

    textWidget1.insert(INSERT, 'something bigger than yourself')

    def getIndex(textWidget, index):
        return tuple(map(int, str.split(textWidget.index(index), '.')))

    start = '1.0'
    while True:
        pos = textWidget1.search('o', start, stopindex=END)
        if not pos:
            break
        print('The position is: ', getIndex(textWidget1, pos))
        start = pos + '+1c'


def func7():
    textWidget1 = Text(root, width=40, height=5, undo=True)
    textWidget1.pack()

    textWidget1.insert(INSERT, 'something bigger than yourself')

    def show():
        textWidget1.edit_undo()

    Button(root, text='undo', command=show).pack()


runcode = int(input('Press 1 or 2, 3, 4, 5, 6, 7: '))

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
elif runcode == 6:
    func6()
elif runcode == 7:
    func7()

root.mainloop()
