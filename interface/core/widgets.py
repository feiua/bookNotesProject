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


def createNewFile():
    top = Toplevel()
    top.title('Python')

    Label(top, text='the work: ').grid(row=0, column=0)
    Label(top, text='the author: ').grid(row=1, column=0)

    e1 = Entry(top)
    e2 = Entry(top)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    def show():
        print('the work: %s ' % e1.get())
        print('the author: %s ' % e2.get())

    Button(top, text='get information', width=10, command=show) \
        .grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Button(top, text='exit', width=10, command=top.destroy) \
        .grid(row=2, column=1, sticky=E, padx=10, pady=5)


menuBar = Menu(root)

# command
fileMenu = Menu(menuBar, tearoff=FALSE)
fileMenu.add_command(label='新建', command=createNewFile)
fileMenu.add_command(label='打开', command=callback)
fileMenu.add_command(label='保存', command=callback)
fileMenu.add_separator()
fileMenu.add_command(label='退出', command=root.quit)
menuBar.add_cascade(label='文件', menu=fileMenu)





root.config(menu=menuBar)

root.mainloop()
