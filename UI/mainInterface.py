#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site: 
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：2020-09-09 10:54 PM
# 文件名称：mainInterface.py
# 开发工具：PyCharm


# from tkinter import ttk
from tkinter import *

# 建立主面板
root = Tk()

# 建立 ribbon

# 建立其他元素

# 建立表格
headersY = [1, 2, 3]  # 列表头
headersX = ['a', 'b', 'c']  # 行表头
tableFrame = Frame(root, width=len(headersY)*45, height=len(headersX)*35)  # 建立表格主面板
tableFrame.pack()

tableIndices = list()
for column in headersY:
    for row in headersX:
        pass
