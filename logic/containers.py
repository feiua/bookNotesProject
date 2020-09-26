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


class MyClass:
    def __init__(self, ID):
        self.ID = ID


df = pd.DataFrame(data=[], index=['a', 'c'], columns=['1', '2'])

print(df.loc['a', '1'])
