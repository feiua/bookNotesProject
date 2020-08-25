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
from PIL import Image, ImageTk
import os

root = Tk()

textLabel = Label(root, text='你在看啥呢？')
textLabel.pack(side=LEFT)

fileName = os.path.abspath(r'\images\pic1.jpg')
imageFile = Image.open(fileName)
tkImage = ImageTk.PhotoImage(imageFile)

imgLabel = Label(root, image=tkImage)
imgLabel.pack()

root.mainloop()
