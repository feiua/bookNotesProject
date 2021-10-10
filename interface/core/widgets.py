#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : www.feiua.com
# 开发团队: 待君加入
# 开发人员：feiua
# 开发时间：2021/10/1023:13
# 文件名称：widgets.py
# 开发工具：PyCharm


from tkinter import *


root = Tk()


def callback():
    print('Hi')


menuBar = Menu(root)

# command
fileMenu = Menu(menuBar, tearoff=FALSE)
fileMenu.add_command(label='打开', command=callback)
fileMenu.add_command(label='保存', command=callback)
fileMenu.add_separator()
fileMenu.add_command(label='退出', command=root.quit)
menuBar.add_cascade(label='文件', menu=fileMenu)


root.config(menu=menuBar)

root.mainloop()