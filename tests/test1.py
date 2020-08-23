'''
练习pymysql 的查询
视频教程链接：https://www.bilibili.com/video/av541476646?p=24&spm_id_from=333.788.b_6d756c74695f70616765.24
'''

# 导包
import pymysql


try:
    # 连接mysql数据库的服务
    connc = pymysql.connect(
                # mysql服务端IP，默认127.0.0.1/localhost-真实IP
                host='localhost',
                user='root',
                password="root",
                database='goodds',
                port=3306,
                charset='utf8')

    # 创建游标对象
    cur = connc.cursor()

    # 编写SQL语句
    sql = 'select * from students;'

    # 使用游标对象去调用SQL
    cur.execute(sql)

    # 获取查询的结果 --print()
    result = cur.fetchall()
    print(result)

    # 关闭游标对象
    cur.close()

    # 关闭连接
    connc.close()
except Exception as e:
    print(e)
