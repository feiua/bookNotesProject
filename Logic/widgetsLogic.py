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


# 表格类
class Table:
    def __init__(self, colHeaders, rowHeaders):
        self.cellDict = dict()
        columnDict = dict()
        rowDict = dict()


# 单元格类
class Cell:
    def __init__(self, id, rowID, colID, text):
        self.id = id
        self.rowID = rowID
        self.colID = colID
        self.text = text


# 添加行
def addRow():
    pass


# 添加列
def addCol():
    pass


# 创建表格
def createTable(rowHeaders=None, colHeaders=None, ):
    return Table()
