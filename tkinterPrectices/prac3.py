# _*_ coding.utf-8 _*_
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：9:32 PM
# 文件名称：prac3.py
# 开发工具：PyCharm

"""
checkbutton 练习
"""

from tkinter import *


root = Tk()

v = IntVar()

c = Checkbutton(root, text='test', variable=v)
c.pack()

l = Label(root, textvariable=v)
l.pack()

root.mainloop()
