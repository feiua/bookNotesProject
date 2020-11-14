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
        self.rowNameList = []  # rowName 的有序列表
        self.colNameList = []  # colName 的有序列表

        if kwargs.keys() & ('colNum', 'rowNum'):
            self.rowNum = kwargs['colNum']
            self.colNum = kwargs['rowNum']
            for rowName in range(self.rowNum):
                rowName = str(uuid.uuid1())
                self.rowNameList.append(rowName)
            for colName in range(self.colNum):
                colName = str(uuid.uuid1())
                self.colNameList.append(colName)
        if kwargs.keys() & ('colNames', 'rowNames'):

            self.rowNameList = list(kwargs['rowNames'])
            self.colNameList = list(kwargs['colNames'])

        for rowName in self.rowNameList:
            self.row2CellDict[rowName] = []
            for colID in self.colNameList:
                self.col2CellDict[colID] = []
                cellID = rowName + colID
                if cellClass:
                    cell = cellClass(*args, **kwargs)
                    self.cellDict[cellID] = cell
                self.row2CellDict[rowName].append(cellID)
                self.col2CellDict[colID].append(cellID)
                self.cell2RowDict[cellID] = rowName
                self.cell2ColDict[cellID] = colID

    def __getitem__(self, *args, **kwargs):
        itemID = ''
        if kwargs:
            itemID = kwargs['row'] + kwargs['column']
        else:
            for each in args:
                itemID += each
        return self.cellDict[itemID]

    def __setitem__(self, **kwargs):
        itemID = kwargs['row'] + kwargs['column']
        self.cellDict[itemID] = kwargs['value']


if __name__ == "__main__":
    class MC:
        def __init__(self, a, b, **kwargs):
            self.a = a
            self.b = b

    k = (1,2,3,4)
    print(type(list(k)))
    print(list(k))

