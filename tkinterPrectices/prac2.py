# _*_ coding.utf-8 _*_
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：10:47 PM
# 文件名称：prac2.py
# 开发工具：PyCharm

"""
练习 label
"""

from tkinter import *
import os


def callback():
    var.set('美女好看吗？')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('你在看啥呢？')

textLabel = Label(frame1, textvariable=var,
                  justify=LEFT, padx=10)

textLabel.pack(side=LEFT)

fileName = os.path.abspath(
    r'D:\我的坚果云\编程\python\practices\myPractice4DataBase\tkinterPrectices\images\pic1.png')
image = PhotoImage(file=fileName)
imgLabel = Label(frame1, image=image)
imgLabel.pack(side=RIGHT)

button1 = Button(frame2, text='不看美女难道看你？', command=callback)
button1.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

root.mainloop()
