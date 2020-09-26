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
import pandas


# 表格类
class Table:
    def __init__(self, rowNum, colNum):
        self.rowNum = rowNum
        self.colNum = colNum
        self.cellDict = dict()
        self.col3CellDict = dict()  # 通过 column 索引 cell
        self.row2CellDict = dict()  # 通过 row 索引 cell
        self.cell2ColDict = dict()  # 通过 cell 索引 column
        self.cell2RowDict = dict()  # 通过 cell 索引 row
        self.rowIDs = []
        self.colIDs = []

        # 初始化行 ID
        for v in range(rowNum):
            rowID = uuid.uuid1()
            self.rowIDs.append(rowID)
            self.row2CellDict[rowID] = []

        # 初始化列 ID
        for v in range(colNum):
            colID = uuid.uuid1()
            self.colIDs.append(colID)
            self.col3CellDict[colID] = []

        # 初始化 Cell 与 行列的索引关系
        for rowID, rowCellIDs in self.row2CellDict.items():
            for colID, colCellIDs in self.col3CellDict.items():
                cellID = uuid.uuid1()
                cell = createCell(id=cellID, rowID=rowID, colID=colID)
                self.cellDict[cellID] = cell
                self.cell2RowDict[cellID] = rowID
                self.cell2ColDict[cellID] = colID
                rowCellIDs.append(cellID)
                colCellIDs.append(cellID)

    # 添加行
    def addRow(self, rowHeader):
        pass

    # 添加列
    def addCol(self):
        pass


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


# 创建表格
def createTable(rowNum, colNum):
    return Table()


# 创建单元格
def createCell(id, rowID, colID):
    return Cell(id, rowID, colID)
