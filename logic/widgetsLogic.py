#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2112:36
# 文件名称：widgetsLogic.py
# 开发工具：PyCharm


"""
表格组件的逻辑
"""

import uuid
from tkinter import *
import numpy as np
import pandas


root = Tk()

# 构造一些全局变量
global SCREENWIDTH, SCREENHEIGHT, ALPHABET
SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()

ALPHABET = [chr(i) for i in np.arange(65, 91)]


def createUI(root):
    """
    创建 UI 界面
    :param root:
    :return:
    """

    # 放置主界面
    rootWidth = int(0.8 * SCREENWIDTH)
    rootHeight = int(0.8 * SCREENHEIGHT)
    placePrompt = "{width}x{height}+{distance_H}+{distance_V}".format(
        width=rootWidth,
        height=rootHeight,
        distance_H=int((SCREENWIDTH - rootWidth)/2),
        distance_V=int((SCREENHEIGHT - rootHeight)/2)
    )
    root.geometry(placePrompt)

    # 创建菜单栏
    menuBar = Menu(root)

    def callback():
        pass

    fileMenu = Menu(menuBar, tearoff=TRUE)
    fileMenu.add_command(label='打开', command=callback)
    menuBar.add_cascade(label='文件', menu=fileMenu)

    root.config(menu=menuBar)

    # 创建类容界面
    frame = Frame(root)
    frame.pack()

    # 创建行title标号（类似于excel的行标 "A, B, C..."）

    root.mainloop()


createUI(root)


# 单元格类
class Cell:
    def __init__(self, id, rowID, colID):
        self.id = id  # 单元格索引的 ID
        self.rowID = rowID  # 对应行索引的 ID
        self.colID = colID  # 对应列索引的 ID


# 单元格中的标签
class CellNote:
    def __init__(self):
        self.id = uuid.uuid1()


# 创建单一便签
class Sticker:
    def __init__(self, master, text, pic, backcolor, fontColor, ):
        self.master = master

    pass



# 创建单元格
def createCell(id, rowID, colID):
    return Cell(id, rowID, colID)


class MyRow:
    def __init__(self, master, headLabel):
        self.head = Label(master=master, text=headLabel)
        self.headLabel = headLabel
