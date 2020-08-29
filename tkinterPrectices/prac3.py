<<<<<<< HEAD
# _*_ coding.utf-8 _*_
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：9:32 PM
# 文件名称：prac3.py
# 开发工具：PyCharm
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-29 19:19
# @Author  : Jianfei Chen
# @Site    : 
# @File    : prac3.py
# @Software: PyCharm
>>>>>>> c0639242b98080ee77b24909dd1690b6d4e963f8

"""
checkbutton 练习
"""

from tkinter import *


<<<<<<< HEAD
root = Tk()

v = IntVar()

c = Checkbutton(root, text='test', variable=v)
c.pack()

l = Label(root, textvariable=v)
l.pack()

root.mainloop()
=======
# 普通版
def normalButton():
    root = Tk()

    v = IntVar()

    c = Checkbutton(root, text='test1', variable=v)
    c.pack()

    l = Label(root, textvariable=v)
    l.pack()

    root.mainloop()
    return

# 循环版
def circleButton():
    root = Tk()

    GIRLS = ['1', '2', '3', '4']

    v = []

    for girl in GIRLS:
        v.append(IntVar())
        b = Checkbutton(root, text=girl, variable=v[-1])
        b.pack(anchor=W)

    root.mainloop()
    return

# radiobutton
def rButton():
    root = Tk()

    LANGS = [
        ('Python', 1),
        ('Perl', 2),
        ('Ruby', 3),
        ('Lua', 4)
    ]

    v = IntVar()
    v.set(1)

    for lang, num in LANGS:
        Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)\
            .pack(fill=X)

    # Radiobutton(root, text='1', variable=v, value=1).pack(anchor=W)
    # Radiobutton(root, text='2', variable=v, value=2).pack(anchor=W)
    # Radiobutton(root, text='3', variable=v, value=3).pack(anchor=W)
    root.mainloop()

# 组合
def combination():
    root = Tk()

    group = LabelFrame(root, text='what do you want?', padx=5, pady=5)
    group.pack(padx=10, pady=10)

    LANGS = [
        ('Python', 1),
        ('Perl', 2),
        ('Ruby', 3),
        ('Lua', 4)
    ]

    v = IntVar()

    for lang, num in LANGS:
        Radiobutton(group, text=lang, variable=v, value=num) \
            .pack(fill=X)

    root.mainloop()

runCode = int(input('press 1 or 2 or 3 or 4: '))

if runCode==1:
    normalButton()
elif runCode==2:
    circleButton()
elif runCode==3:
    rButton()
elif runCode==4:
    combination()
>>>>>>> c0639242b98080ee77b24909dd1690b6d4e963f8
