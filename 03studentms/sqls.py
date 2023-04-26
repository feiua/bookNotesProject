"""
项目名称：python pyqt5 mysql 学生管理系统
作者：bhml
时间：2022/11/28
代码功能：集中存放项目中用到的SQL语句
"""
from db import md5


# 01登录
def login(username, password):
    password = md5(password)
    return "select * from admin where a_username='%s' and a_password='%s'" % (username, password)


# 02根据id查询班级列表
def getClassList(idStr, name=""):
    """
    :param idStr: id，多个用','分隔。0表示获取所有数据
    :return:
    """
    sql = "select * from class_ where c_name like '%" + name + "%'"
    if idStr == "0":
        pass
    else:
        sql += " and c_id in (" + idStr + ")"
    return sql


# 03获取学生信息
def getStudentById(id):
    """
    :param id: s_id 学生id
    :return:
    """
    sql = "select * from student where s_id=" + str(id)
    return sql


# 04查询一个班的学生信息
def getStudentByClassId(id):
    """
    :param id: 班级id
    :return:
    """
    sql = "select * from student where s_class=" + str(id)
    return sql


# 05查询学生信息（通过班级，姓名）
def getStudentList(classids, name):
    """
    :param classids: 学生所在班级id，多个用逗号间隔。0表示获取所有数据
    :return:
    """
    sql = "select * from student where s_realname like '%" + name + "%'"
    if classids == "0":
        pass
    else:
        sql += " and s_class in (" + classids + ")"
    sql += " order by s_number"
    return sql


# 06获取学生成绩列表（通过总分排序）
def getGradeList(classids, name):
    """
    :param classids: 学生所在班级id，多个用逗号间隔。0表示获取所有数据
    :return:
    """
    sql = "select * from student where s_realname like '%" + name + "%'"
    if classids == "0":
        pass
    else:
        sql += " and s_class in (" + classids + ")"
    sql += " order by s_chinese + s_math + s_english DESC"
    return sql


# 07获取管理员列表
def getAdminList(name):
    """
    :param name: 用户名
    :return:
    """
    sql = "select * from admin where a_username like '%" + name + "%'"
    sql += " order by a_id"
    return sql


# 08获取管理员信息
def getAdminById(id):
    """
    :param id: 管理员id
    :return:
    """
    sql = "select * from admin where a_id=" + str(id)
    return sql


# 09通过学生id删除学生信息
def delStudentById(id):
    sql = "delete from student where s_id=" + str(id)
    return sql


# 10通过班级id删除班级信息
def delClassById(id):
    sql = "delete from class_ where c_id = " + str(id)
    return sql


# 11通过id删除用户信息
def delAdminById(id):
    sql = "delete from admin where a_id = " + str(id)
    return sql


# 12通过id删除批量学生信息
def delStudentByIds(ids):
    sql = "delete from student where s_id in " + ids
    return sql


# 13更新学生信息
def updateStudentById(id, name, number, sex, class_):
    sql = "update student set s_realname='%s',s_number=%s,s_sex=%s,s_class=%s where s_id=" % (
        name, number, sex, class_) + str(id)
    return sql


# 14更新学生成绩信息（通过id）
def updateGradeById(id, chinese, math, english):
    sql = "update student set s_chinese=%s,s_math=%s,s_english=%s where s_id=" % (chinese, math, english) + str(id)
    return sql


# 15更新学生成绩信息（通过学号）
def updateGradeByNum(num, chinese, math, english):
    sql = "update student set s_chinese=%s,s_math=%s,s_english=%s where s_number=" % (chinese, math, english) + str(num)
    return sql


# 16更新班级信息（通过id）
def updateClassById(id, name):
    sql = "update class_ set c_name='%s' where c_id=" % name + str(id)
    return sql


# 17更新用户信息（通过id）
def updateAdminById(id, username, mark, classids):
    sql = "update admin set a_username='%s',a_mark='%s',a_classid='%s' where a_id=" \
          % (username, mark, classids) + str(id)
    return sql


# 18更新用户名（通过id）
def updateUsernameById(id, username):
    sql = "update admin set a_username='%s' where a_id=" % username + str(id)
    return sql


# 19重置用户密码（通过id）
def resetAdminPasswById(id, password):
    password = md5(password)
    sql = "update admin set a_password='%s' where a_id=" % password + str(id)
    return sql


# 20添加学生信息
def insertStudent(name, number, sex, class_):
    sql = "insert into student (s_realname,s_number,s_sex,s_class) VALUES ('%s',%s,%s,%s)" % (
        name, str(number), sex, str(class_))
    return sql


# 21添加班级信息
def insertClass(name):
    sql = "insert into class_ (c_name) VALUES ('%s')" % name
    return sql


# 22添加用户信息
def insertAdmin(username, password, mark, classids):
    password = md5(password)
    sql = "insert into admin (a_username,a_password,a_mark,a_classid) VALUES " \
          "('%s','%s','%s','%s')" % (username, password, mark, classids)
    return sql


# 测试
if __name__ == "__main__":
    print(getClassList("1,2,3"))
