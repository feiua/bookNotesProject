from tkinter import *

root = Tk()

global SCREENWIDTH, SCREENHEIGHT, ALPHABET
SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()

# 菜单
menuBar = Menu(root)


def callback():
    print('Hi')


fileMenu = Menu(menuBar, tearoff=TRUE)
fileMenu.add_command(label='打开', command=callback)
fileMenu.add_command(label='保存', command=callback)
fileMenu.add_separator()
fileMenu.add_command(label='退出', command=root.quit)
menuBar.add_cascade(label='文件', menu=fileMenu)

# 新建项目属性设置界面
frame1 = Frame(root, ).pack()

