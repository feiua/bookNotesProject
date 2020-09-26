#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2616:18
# 文件名称：test.py
# 开发工具：PyCharm


import numpy as np



dtype = np.dtype([('date', 'uint32'), ('close', np.uint32), ('name', np.object)])
result = np.empty(shape=(0,), dtype=dtype)
result = np.append(result, np.array([(20180409, 50, "abcdef")], dtype=dtype))
print(result)
