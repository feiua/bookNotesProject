#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：11:14 PM
# 文件名称：prac7.py
# 开发工具：PyCharm

"""

"""

from tkinter import *

root = Tk()


def callback():
    print('Hi')


menuBar = Menu(root)

# command
fileMenu = Menu(menuBar, tearoff=TRUE)
fileMenu.add_command(label='打开', command=callback)
fileMenu.add_command(label='保存', command=callback)
fileMenu.add_separator()
fileMenu.add_command(label='退出', command=root.quit)
menuBar.add_cascade(label='文件', menu=fileMenu)

# checkbutton
openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()

checkMenu = Menu(menuBar, tearoff=False)
checkMenu.add_checkbutton(label='视角', command=callback, variable=openVar)
checkMenu.add_checkbutton(label='看上', command=callback, variable=saveVar)
checkMenu.add_separator()
checkMenu.add_checkbutton(label='看下', command=root.quit, variable=quitVar)
menuBar.add_cascade(label='检查', menu=checkMenu)

# radiobutton
editVar = IntVar()

editMenu = Menu(menuBar, tearoff=FALSE)
editMenu.add_radiobutton(label='剪切', command=callback, variable=editVar, value=1)
editMenu.add_radiobutton(label='拷贝', command=callback, variable=editVar, value=2)
editMenu.add_radiobutton(label='粘贴', command=callback, variable=editVar, value=3)
menuBar.add_cascade(label='编辑', menu=editMenu)

# 鼠标事件绑定
menuBarClick = Menu(root, tearoff=FALSE)
menuBarClick.add_command(label='撤销', command=callback)
menuBarClick.add_command(label='重做', command=root.quit)

frame = Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    menuBarClick.post(event.x_root, event.y_root)


frame.bind('<Button-3>', popup)

# menubutton
mb = Menubutton(root, text='Go', relief=RAISED)
mb.pack()

mbMenu = Menu(mb, tearoff=False)
mbMenu.add_checkbutton(label='1', command=callback, variable=openVar)
mbMenu.add_checkbutton(label='2', command=callback, variable=saveVar)
mbMenu.add_checkbutton(label='3', command=root.quit, variable=quitVar)

mb.config(menu=mbMenu)

root.config(menu=menuBar)

# optionMenu
variable1 = StringVar()
variable1.set('one')

w = OptionMenu(root, variable1, 'one', 'two', 'three')
w.pack()

# optionMenu 列表添加选项
OPTIONS = str(12345)
variable2 = StringVar()
variable2.set(OPTIONS[0])

list1 = OptionMenu(root, variable2, *OPTIONS)
list1.pack()

root.mainloop()
