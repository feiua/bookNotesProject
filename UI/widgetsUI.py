#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : NA
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2019:11
# 文件名称：widgetsUI.py
# 开发工具：PyCharm


from tkinter import *


class CellUI:
    def __init__(self, master, text='NA'):
        self.master = master
        self.label = Label(self.master, text=text, relief=SUNKEN)
        pass


