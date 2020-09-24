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


# 表格类
class Table:
    def __init__(self, rowNum, colNum):
        self.cellDict = dict()
        self.colDict = dict()
        self.rowDict = dict()
        self.rowNum = rowNum
        self.colNum = colNum
        self.rowIDs = []
        self.colIDs = []

        # 初始化行 ID
        for v in range(rowNum):
            rowID = uuid.uuid1()
            self.rowIDs.append(rowID)
            self.rowDict[rowID] = []

        # 初始化列 ID
        for v in range(colNum):
            colID = uuid.uuid1()
            self.colIDs.append(colID)
            self.colDict[colID] = []

    # 添加行
    def addRow(self, rowHeader):
        pass

    # 添加列
    def addCol(self):
        pass


# 单元格类
class Cell:
    def __init__(self, id, rowID, colID, text):
        self.id = id  # 单元格索引的 ID
        self.rowID = rowID  # 对应行索引的 ID
        self.colID = colID  # 对应列索引的 ID
        self.text = text  # 显示在UI界面的文本


# 单元格中的标签
class CellNote:
    def __init__(self):
        self.id = uuid.uuid1()


# 创建表格
def createTable(rowNum, colNum):
    return Table()


# 创建单元格
def createCell(id, rowID, colID, text):
    return Cell(id, rowID, colID, text)
