#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2616:18
# 文件名称：test.py
# 开发工具：PyCharm

import uuid

# Generate a new UUID value
k = uuid.uuid4()

# Do something with the event_id value
print(type(k))

a = 1 + int(k)
print(a)

print(type(str(k)))