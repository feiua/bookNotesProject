#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2614:33
# 文件名称：containers.py
# 开发工具：PyCharm

"""
自建容器 包
"""

import numpy as np
import pandas as pd
import uuid


class MyTable:
    def __init__(self, cellClass=None, *args, **kwargs):
        """
        初始化
        :param args: 用于实例化 cell 的参数
        :param kwargs:
        colNum: 列总数
        rowNum: 行总数
        colNames: 列名称
        rowNames: 行名称
        """
        self.cellDict = dict()
        self.col2CellDict = dict()  # 通过 column 索引 cell
        self.row2CellDict = dict()  # 通过 row 索引 cell
        self.cell2ColDict = dict()  # 通过 cell 索引 column
        self.cell2RowDict = dict()  # 通过 cell 索引 row
        self.rowNameDict = dict()  # 通过 ID 索引行名称
        self.colNameDict = dict()  # 通过 ID 索引列名称

        if kwargs.keys() & ('colNum', 'rowNum'):
            self.rowNum = kwargs['colNum']
            self.colNum = kwargs['rowNum']
            for rowName in range(self.rowNum):
                self.rowNameDict[uuid.uuid1()] = str(rowName)
            for colName in range(self.colNum):
                self.colNameDict[uuid.uuid1()] = str(colName)
        if kwargs.keys() & ('colNames', 'rowNames'):
            for rowName in kwargs['rowNames']:
                self.rowNameDict[uuid.uuid1()] = str(rowName)
            for colName in kwargs['colNames']:
                self.colNameDict[uuid.uuid1()] = str(colName)

        for rowID in self.rowNameDict.keys():
            self.row2CellDict[rowID] = []
            for colID in self.colNameDict.keys():
                self.col2CellDict[colID] = []
                cellID = uuid.uuid1()
                if cellClass:
                    cell = cellClass(args)
                    self.cellDict[cellID] = cell
                self.row2CellDict[rowID].append(cellID)
                self.col2CellDict[colID].append(cellID)
                self.cell2RowDict[cellID] = rowID
                self.cell2ColDict[cellID] = colID

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass


if __name__ == "__main__":
    m = MyTable(colNum=1, rowNum=2)
    print(m.rowNum, m.colNum)
