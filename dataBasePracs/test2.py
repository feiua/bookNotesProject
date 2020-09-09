# _*_ coding.utf-8 _*_
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：11:22 AM
# 文件名称：test2.py
# 开发工具：PyCharm

"""
练习pymysql 的增、改、删
视频教程链接：https://www.bilibili.com/video/av541476646?p=25
"""

# 增加数据 刘德华 56 男 数据到 数据库goods--中students 表中
# 修改数据 小王 的名字为 小王吧 数据库goods--中students 表中
# 删除数据 李磊 数据库goods--中students 表中

# 导包
import pymysql

# 连接mysql服务器
connc = pymysql.connect(
                # mysql服务端IP，默认127.0.0.1/localhost-真实IP
                host='localhost',
                user='root',
                password="root",
                database='goods',
                port=3306,
                charset='utf8')

# 创建游标对象
cur = connc.cursor()

try:
    # 编写 增、改、删 sql语句
    # 增加数据 刘德华 56 男 数据
    sql_add = 'insert into students values(%s, %s, %s, %s)'
    add_data = [0, '刘德华', 56, '男']
    # 修改数据 小王 的名字为 小王吧
    sql_update = 'update students set name=%s where name="小王"'
    update_data = ['小王吧']
    # 删除数据 李磊
    sql_delete = 'delete from students where name=%s'
    delete_data = ['李磊']

    # 使用游标对象执行SQL
    cur.execute(sql_add, add_data)
    cur.execute(sql_update, update_data)
    cur.execute(sql_delete, delete_data)

    # 提交操作
    connc.commit()

except Exception as e:
    print(e)
    # 数据回滚
    connc.rollback()

finally:
    # 关闭游标对象
    cur.close()

    # 关闭连接
    connc.close()
    print('All SQL are executed.')
