"""
项目名称：python pyqt5 mysql 学生管理系统
作者：bhml
时间：2022/11/28
代码功能：主界面和功能的设计与实现
"""

# 导入所需模块
import os
from PyQt5 import QtCore, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import *
import pandas as pd
from PyQt5.QtCore import Qt, pyqtSignal, QRect

from AddAdmin import AddAdmin
from EditAdmin import EditAdmin
from sqls import *
from db import *
import Config as C

# 全局变量
header_field = ['全选']  # 表头字段
global all_header_combobox  # 用来装行表头所有复选框
global all_class, class_dict, class_dict2
global data_list  # 存放数据库数据列表
global activate_menu  # 当前激活的菜单按钮

activate_menu = None  # 记录当前选中的菜单


# 自定义表头类
class CheckBoxHeader(QHeaderView):
    # 自定义 复选框全选信号
    select_all_clicked = pyqtSignal(bool)
    # 这4个变量控制列头复选框的样式，位置以及大小
    _x_offset = 21
    _y_offset = 10
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False  # 控制全选

    # paintSection 绘制部分，主要用于绘制复选框，主要设置QStyleOptionButton的状态
    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()
        self._y_offset = int((rect.height() - self._width) / 2.)
        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    # 覆写鼠标点击事件(点击全选框效果)
    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                    print(self.isOn)
                else:
                    self.isOn = True
                    print(self.isOn)
                    # 当用户点击了行表头复选框，发射 自定义信号 select_all_clicked()
                self.select_all_clicked.emit(self.isOn)
                self.updateSection(0)
        super(CheckBoxHeader, self).mousePressEvent(event)

    # 改变勾选状态
    def change_state(self, isOn):
        # 如果行表头复选框为勾选状态
        if isOn:
            # 将所有的复选框都设为勾选状态
            for i in all_header_combobox:
                i.setCheckState(Qt.Checked)
        else:
            for i in all_header_combobox:
                i.setCheckState(Qt.Unchecked)


# 界面设计与实现
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # 初始化界面
    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')  # 部件命名，设置样式用
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占12行2列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_label_1 = QtWidgets.QPushButton('欢迎您，' + C.USER[3])
        self.left_label_1.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("个人中心")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.users', color='white'), "学生管理")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(lambda: self.setRightWidget(C.FLAG_STUDENT))
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.id-card', color='white'), "成绩管理")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(lambda: self.setRightWidget(C.FLAG_GRADE))
        # 管理员账号
        if C.USER[0] == 1:
            self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.institution', color='white'), "班级管理")
            self.left_button_3.setObjectName('left_button')
            self.left_button_3.clicked.connect(lambda: self.setRightWidget(C.FLAG_CLASS))
            self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.user-secret', color='white'), "角色管理")
            self.left_button_4.setObjectName('left_button')
            self.left_button_4.clicked.connect(lambda: self.setRightWidget(C.FLAG_ADMIN))
        else:
            # 表格布局用于占位
            self.left_button_3 = QtWidgets.QPushButton()
            self.left_button_4 = QtWidgets.QPushButton()
        self.left_button_5 = QtWidgets.QPushButton()
        self.left_button_6 = QtWidgets.QPushButton()
        self.left_button_7 = QtWidgets.QPushButton()
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='white'), "修改资料")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(lambda: self.setRightWidget(C.FLAG_INFO))
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.sign-out', color='white'), "退出登录")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(lambda: self.logOut(True))
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 12, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 7, 0, 1, 3)

        # 设置样式
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                padding-bottom:2px;
                font-size:16px;
                font-weight:500;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button{
                width:20px;
                font-size:15px;
            }
            QPushButton#left_button:hover{font-weight:700;}
            QWidget#left_widget{
                background:#607d8b;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
            }
        ''')
        self.right_widget = None
        self.setRightWidget()
        self.main_layout.setSpacing(0)

    # 设置右方显示界面内容布局
    def setRightWidget(self, flag=C.FLAG_GRADE):
        # 学生管理
        if flag == C.FLAG_STUDENT:
            self.right_widget = self.student_management()
        # 成绩管理
        elif flag == C.FLAG_GRADE:
            self.right_widget = self.grade_management()
        # 班级管理（管理员）
        elif flag == C.FLAG_CLASS:
            self.right_widget = self.class_management()
        # 角色管理（管理员）
        elif flag == C.FLAG_ADMIN:
            self.right_widget = self.admin_management()
        # 修改信息
        elif flag == C.FLAG_INFO:
            self.right_widget = self.change_info()

    # 学生管理界面设计
    def student_management(self):
        global all_class, class_dict, class_dict2
        class_dict = {}
        class_dict2 = {}
        if self.right_widget:
            self.main_layout.removeWidget(self.right_widget)  # 移除已有右侧组件
        self.setWindowTitle('Python学生管理系统-学生管理')
        self.setLeftMenu(self.left_button_1)  # 标记选中
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.right_layout = self.verticalLayout
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第2列，占12行10列

        self.widget = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        # 班级列表下拉框
        self.cb = QComboBox(self)
        # 单个添加条目
        self.cb.addItem('All')
        # 多个添加条目
        all_class = self.getClassList()
        print(all_class)
        for class_ in all_class:
            # 添加班级字典
            class_dict[class_[0]] = class_[1]
            class_dict2[class_[1]] = class_[0]
            self.cb.addItem(str(class_[0]) + '.' + class_[1])
        print(class_dict)  # 班级字典
        print(class_dict2)
        # 传递改变条件的信号
        self.cb.currentIndexChanged[int].connect(lambda: self.getDataList(C.FLAG_STUDENT))  # 条目发生改变，发射信号，传递条目索引

        self.cb.setStyleSheet(''' text-align : center;
                                              height : 30px;
                                              padding-left: 5px;
                                              font : 12px  ''')
        self.horizontalLayout.addWidget(self.cb)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # 姓名输入框
        self.input_name = QtWidgets.QLineEdit(self.widget)
        self.input_name.setObjectName("input_name")
        self.horizontalLayout.addWidget(self.input_name)
        self.input_name.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')

        # 查询按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.getDataList(C.FLAG_STUDENT))
        self.pushButton_2.setStyleSheet(''' text-align : center;
                                              background-color : #03a9f4;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        # 空格
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        # 批量删除按钮
        self.pushButton_del = QtWidgets.QPushButton(self.widget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout.addWidget(self.pushButton_del)
        self.pushButton_del.clicked.connect(lambda: self.batchDelete(C.FLAG_STUDENT))
        self.pushButton_del.setStyleSheet(''' text-align : center;
                                              background-color : #f44336;
                                              height : 30px;
                                              width: 80px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        # 导入按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(lambda: self.open_file(C.FLAG_STUDENT))
        self.pushButton_3.setStyleSheet(''' text-align : center;
                                              background-color : #009688;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        # 导出按钮
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.data_export(C.FLAG_STUDENT))
        self.pushButton.setStyleSheet(''' text-align : center;
                                              background-color : #ff9800;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        # 内容区域====================================================================================
        self.verticalLayout.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)

        # 设置显示名
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "班级"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_del.setText(_translate("Form", "批量删除"))
        self.pushButton_3.setText(_translate("Form", "导入"))
        self.pushButton.setText(_translate("Form", "导出"))

        # 表头内容
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "学号"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "性别"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "班级"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "操作"))

        # 选择框
        header = CheckBoxHeader()  # 实例化自定义表头
        self.tableWidget.setHorizontalHeader(header)  # 设置表头
        header.select_all_clicked.connect(header.change_state)  # 行表头复选框单击信号与槽
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(5, 197)

        # 其余列宽设置
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)

        # 获取数据
        self.getDataList(C.FLAG_STUDENT)
        return self.right_widget

    # 成绩管理界面设计
    def grade_management(self):
        global all_class, class_dict, class_dict2
        class_dict = {}
        class_dict2 = {}
        if self.right_widget:
            self.main_layout.removeWidget(self.right_widget)  # 移除已有右侧组件
        self.setWindowTitle('Python学生管理系统-成绩管理')
        self.setLeftMenu(self.left_button_2)
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.right_layout = self.verticalLayout
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第2列，占12行10列

        self.widget = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        # 班级列表下拉框
        self.cb = QComboBox(self)
        # 单个添加条目
        self.cb.addItem('All')
        # 多个添加条目
        all_class = self.getClassList()
        for class_ in all_class:
            # 添加班级字典
            class_dict[class_[0]] = class_[1]
            class_dict2[class_[1]] = class_[0]
            self.cb.addItem(str(class_[0]) + '.' + class_[1])

        # 信号
        self.cb.currentIndexChanged[int].connect(lambda: self.getDataList(C.FLAG_GRADE))  # 条目发生改变，发射信号，传递条目索引

        self.cb.setStyleSheet(''' text-align : center;
                                              height : 30px;
                                              padding-left: 5px;
                                              font : 12px  ''')
        self.horizontalLayout.addWidget(self.cb)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # 姓名输入框
        self.input_name = QtWidgets.QLineEdit(self.widget)
        self.input_name.setObjectName("input_name")
        self.horizontalLayout.addWidget(self.input_name)
        self.input_name.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')
        # 查询按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.getDataList(C.FLAG_GRADE))
        self.pushButton_2.setStyleSheet(''' text-align : center;
                                              background-color : #03a9f4;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        # 批量清零按钮
        self.pushButton_del = QtWidgets.QPushButton(self.widget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout.addWidget(self.pushButton_del)
        self.pushButton_del.clicked.connect(lambda: self.batchDelete(C.FLAG_GRADE))
        self.pushButton_del.setStyleSheet(''' text-align : center;
                                              background-color : #f44336;
                                              height : 30px;
                                              width: 80px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        # 导入按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(lambda: self.open_file(C.FLAG_GRADE))
        self.pushButton_3.setStyleSheet(''' text-align : center;
                                              background-color : #009688;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        # 导出按钮
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.data_export(C.FLAG_GRADE))
        self.pushButton.setStyleSheet(''' text-align : center;
                                              background-color : #ff9800;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        self.verticalLayout.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tableWidget)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "班级"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_del.setText(_translate("Form", "批量清零"))
        self.pushButton_3.setText(_translate("Form", "导入"))
        self.pushButton.setText(_translate("Form", "导出"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "学号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "语文"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "数学"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "英语"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "总分"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "操作"))

        header = CheckBoxHeader()  # 实例化自定义表头
        self.tableWidget.setHorizontalHeader(header)  # 设置表头
        header.select_all_clicked.connect(header.change_state)  # 行表头复选框单击信号与槽
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setColumnWidth(4, 80)
        self.tableWidget.setColumnWidth(5, 80)
        self.tableWidget.setColumnWidth(7, 130)

        # 列宽
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)

        self.getDataList(C.FLAG_GRADE)
        return self.right_widget

    # 班级管理界面设计
    def class_management(self):
        global all_class, class_dict, class_dict2
        class_dict = {}
        class_dict2 = {}
        if self.right_widget:
            self.main_layout.removeWidget(self.right_widget)  # 移除已有右侧组件
        self.setWindowTitle('Python学生管理系统-班级管理')
        self.setLeftMenu(self.left_button_3)
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.right_layout = self.verticalLayout
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)

        self.widget = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 新增按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(lambda: self.createData(C.FLAG_CLASS))
        self.pushButton_3.setStyleSheet(''' text-align : center;
                                                      background-color : #009688;
                                                      height : 30px;
                                                      width: 80px;
                                                      border-style: outset;
                                                      border-radius: 5px;
                                                      color: #fff;
                                                      font : 12px  ''')
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # 班级输入框
        self.input_name = QtWidgets.QLineEdit(self.widget)
        self.input_name.setObjectName("input_name")
        self.horizontalLayout.addWidget(self.input_name)
        self.input_name.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')

        # 查询按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.getDataList(C.FLAG_CLASS, i=-1))
        self.pushButton_2.setStyleSheet(''' text-align : center;
                                              background-color : #03a9f4;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        # 批量删除按钮
        self.pushButton_del = QtWidgets.QPushButton(self.widget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout.addWidget(self.pushButton_del)
        self.pushButton_del.clicked.connect(lambda: self.batchDelete(C.FLAG_CLASS))
        self.pushButton_del.setStyleSheet(''' text-align : center;
                                              background-color : #f44336;
                                              height : 30px;
                                              width: 80px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        self.verticalLayout.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton_3.setText(_translate("Form", "新增班级"))
        self.label_2.setText(_translate("Form", "班级"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_del.setText(_translate("Form", "批量删除"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "班级名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "班级名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "操作"))

        header = CheckBoxHeader()  # 实例化自定义表头
        self.tableWidget.setHorizontalHeader(header)  # 设置表头
        header.select_all_clicked.connect(header.change_state)  # 行表头复选框单击信号与槽
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 510)

        self.tableWidget.verticalHeader().setDefaultSectionSize(32)

        self.getDataList(C.FLAG_CLASS, i=-1)
        return self.right_widget

    # 角色管理界面设计
    def admin_management(self):
        global all_class, class_dict, class_dict2
        class_dict = {}
        class_dict2 = {}
        if self.right_widget:
            self.main_layout.removeWidget(self.right_widget)  # 移除已有右侧组件
        self.setWindowTitle('Python学生管理系统-角色管理')
        self.setLeftMenu(self.left_button_4)
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.right_layout = self.verticalLayout
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)

        self.widget = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 新增按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(lambda: self.addAdmin())
        self.pushButton_3.setStyleSheet(''' text-align : center;
                                                              background-color : #009688;
                                                              height : 30px;
                                                              width: 80px;
                                                              border-style: outset;
                                                              border-radius: 5px;
                                                              color: #fff;
                                                              font : 12px  ''')
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # 姓名输入框
        self.input_name = QtWidgets.QLineEdit(self.widget)
        self.input_name.setObjectName("input_name")
        self.horizontalLayout.addWidget(self.input_name)
        self.input_name.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')

        # 查询按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.getDataList(C.FLAG_ADMIN, i=-1))
        self.pushButton_2.setStyleSheet(''' text-align : center;
                                              background-color : #03a9f4;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        # 批量删除按钮
        self.pushButton_del = QtWidgets.QPushButton(self.widget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout.addWidget(self.pushButton_del)
        self.pushButton_del.clicked.connect(lambda: self.batchDelete(C.FLAG_ADMIN))
        self.pushButton_del.setStyleSheet(''' text-align : center;
                                              background-color : #f44336;
                                              height : 30px;
                                              width: 80px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        self.verticalLayout.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton_3.setText(_translate("Form", "新增角色"))
        self.label_2.setText(_translate("Form", "用户名"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_del.setText(_translate("Form", "批量删除"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "备注"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "可管理班级"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "操作"))

        header = CheckBoxHeader()  # 实例化自定义表头
        self.tableWidget.setHorizontalHeader(header)  # 设置表头
        header.select_all_clicked.connect(header.change_state)  # 行表头复选框单击信号与槽
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 160)
        self.tableWidget.setColumnWidth(4, 240)

        self.tableWidget.verticalHeader().setDefaultSectionSize(32)

        self.getDataList(C.FLAG_ADMIN, i=-1)
        return self.right_widget

    # 修改资料界面设计
    def change_info(self):
        if self.right_widget:
            self.main_layout.removeWidget(self.right_widget)  # 移除已有右侧组件
        self.setWindowTitle('Python学生管理系统-资料修改')
        self.setLeftMenu(self.left_button_8)
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.right_widget.setStyleSheet(''' background-image : url('image/bg.png');
                                            background-position:center;
                                            background-repeat:no-repeat;''')

        self.right_layout = self.verticalLayout
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.widget = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.label_2)

        # 用户名输入框
        self.input_name = QtWidgets.QLineEdit(self.widget)
        self.input_name.setObjectName("input_name")
        self.input_name.setText(C.USER[1])
        self.horizontalLayout.addWidget(self.input_name)
        self.input_name.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')

        self.widget2 = QtWidgets.QWidget()
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.widget2)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(spacerItem2)
        self.label_pass0 = QtWidgets.QLabel(self.widget2)
        self.label_pass0.setText('  原密码')
        self.horizontalLayout2.addWidget(self.label_pass0)

        # 原密码输入框
        self.input_pass0 = QtWidgets.QLineEdit(self.widget2)
        self.input_pass0.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pass0.setPlaceholderText('请输入原密码')
        self.horizontalLayout2.addWidget(self.input_pass0)
        self.input_pass0.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')

        self.widget3 = QtWidgets.QWidget()
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.widget3)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout3.addItem(spacerItem3)
        self.label_pass1 = QtWidgets.QLabel(self.widget3)
        self.label_pass1.setText('  新密码')
        # 新密码输入框
        self.input_pass1 = QtWidgets.QLineEdit(self.widget3)
        self.input_pass1.setObjectName("input_pass1")
        self.input_pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pass1.setPlaceholderText('请输入新密码')
        self.horizontalLayout3.addWidget(self.label_pass1)
        self.horizontalLayout3.addWidget(self.input_pass1)
        self.input_pass1.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')

        self.widget4 = QtWidgets.QWidget()
        self.horizontalLayout4 = QtWidgets.QHBoxLayout(self.widget4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout4.addItem(spacerItem4)
        self.label_pass2 = QtWidgets.QLabel(self.widget4)
        self.label_pass2.setText('重复密码')
        # 重复密码输入框
        self.input_pass2 = QtWidgets.QLineEdit(self.widget4)
        self.input_pass2.setObjectName("input_pass2")
        self.input_pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pass2.setPlaceholderText('请重复新密码')
        self.horizontalLayout4.addWidget(self.label_pass2)
        self.horizontalLayout4.addWidget(self.input_pass2)
        self.input_pass2.setStyleSheet(''' height : 30px;
                                              border-style: outset;
                                              padding-left: 5px;
                                              border: 1px solid #ccc;
                                              border-radius: 5px;
                                              font : 12px  ''')
        self.widget5 = QtWidgets.QWidget()
        self.horizontalLayout5 = QtWidgets.QHBoxLayout(self.widget5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout5.addItem(spacerItem5)

        # 提交按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.widget5)
        self.pushButton_3.setObjectName("pushButton")
        self.horizontalLayout5.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(lambda: self.modifyPassw())
        self.pushButton_3.setStyleSheet(''' text-align : center;
                                                                      background-color : #009688;
                                                                      height : 30px;
                                                                      width: 80px;
                                                                      border-style: outset;
                                                                      border-radius: 5px;
                                                                      color: #fff;
                                                                      font : 12px  ''')
        # 修改按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.editUsername())
        self.pushButton_2.setStyleSheet(''' text-align : center;
                                              background-color : #03a9f4;
                                              height : 30px;
                                              width: 50px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(spacerItem)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout3.addItem(spacerItem)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout4.addItem(spacerItem)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout5.addItem(spacerItem)

        spacerItem = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(40, 300, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget2)
        self.verticalLayout.addWidget(self.widget3)
        self.verticalLayout.addWidget(self.widget4)
        self.verticalLayout.addWidget(self.widget5)

        spacerItem = QtWidgets.QSpacerItem(40, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton_3.setText(_translate("Form", "修改密码"))
        self.label_2.setText(_translate("Form", "用户名"))
        self.pushButton_2.setText(_translate("Form", "修改"))

        return self.right_widget

    # 设置行可编辑
    def editRow(self, id, flag, editable=True):
        """
        :param id: 数据库id
        :param flag: 1. 学生 2.班级 3.角色
        :param editable: 是否设置单元格可编辑，默认true
        :return:
        """
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            row = self.tableWidget.indexAt(button.parent().pos()).row()
            FLAGS = QtCore.Qt.ItemIsEnabled
            if editable:
                FLAGS = QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | FLAGS
                BUTTONS = self.buttonForRowEdit(id, flag)
            else:
                BUTTONS = self.buttonForRow(id, flag)

            if flag == C.FLAG_STUDENT:
                item2 = self.tableWidget.item(row, 2)
                item2.setFlags(FLAGS)
                item2 = self.tableWidget.item(row, 3)
                item2.setFlags(FLAGS)
                item2 = self.tableWidget.item(row, 4)
                item2.setFlags(FLAGS)
                item2 = self.tableWidget.item(row, 5)
                item2.setFlags(FLAGS)
                self.tableWidget.setCellWidget(row, 6, BUTTONS)
            elif flag == C.FLAG_GRADE:
                item2 = self.tableWidget.item(row, 3)
                item2.setFlags(FLAGS)
                item2 = self.tableWidget.item(row, 4)
                item2.setFlags(FLAGS)
                item2 = self.tableWidget.item(row, 5)
                item2.setFlags(FLAGS)
                self.tableWidget.setCellWidget(row, 7, BUTTONS)

    # 提交数据
    def submitData(self, id, flag):
        """
        :param id: 数据库id
        :param flag: 1. 学生 2.班级 3.角色
        :return:
        """
        global class_dict2
        # 调用sender()方法可以判断发送信号的信号源是哪一个
        button = self.sender()
        if button:
            # 确定位置
            row = self.tableWidget.indexAt(button.parent().pos()).row()
            # 学生管理
            if flag == C.FLAG_STUDENT:
                name = self.tableWidget.item(row, 2).text()
                number = self.tableWidget.item(row, 3).text()
                sex = '1' if self.tableWidget.item(row, 4).text() == '男' else '2'
                class_ = self.tableWidget.item(row, 5).text()
                if class_ not in class_dict2.keys():
                    QMessageBox.critical(self, '输入有误', "该班级不存在！")
                    return
                else:
                    try:
                        class_ = class_dict2[class_]
                        sql_execute(updateStudentById(id, name, number, sex, class_))
                        QMessageBox.about(self, '成功', "修改成功！")
                        self.editRow(id, flag, False)
                    except Exception as e:
                        print(e)
                        QMessageBox.critical(self, '编辑失败', "提交失败，请检查输入！")
                        return

            # 成绩管理
            elif flag == C.FLAG_GRADE:
                chinese = self.tableWidget.item(row, 3).text()
                math = self.tableWidget.item(row, 4).text()
                english = self.tableWidget.item(row, 5).text()
                if not chinese.isdigit() or not math.isdigit() or not english.isdigit():
                    QMessageBox.critical(self, '输入有误', "成绩只能为整数哦！")
                    return
                else:
                    try:
                        sql_execute(updateGradeById(id, chinese, math, english))
                        self.tableWidget.item(row, 6).setText(str(int(chinese) + int(math) + int(english)))
                        self.editRow(id, flag, False)

                    except Exception as e:
                        print(e)
                        QMessageBox.critical(self, '失败', "提交失败，请检查输入！")
                        return

    # 批量删除
    def batchDelete(self, flag):
        global all_header_combobox
        ids = [-1]
        for i in range(len(all_header_combobox)):
            try:
                if all_header_combobox[i].checkState() == 2:
                    if flag == C.FLAG_GRADE:
                        ids.append(self.tableWidget.item(i, 2).text())
                    else:
                        ids.append(self.tableWidget.item(i, 1).text())
            except Exception as e:
                print(e)
        if len(ids) == 1:
            QMessageBox.information(self, '失败', "未选择数据！")
            return
        self.deleteRow(ids, flag)

    # 删除数据
    def deleteRow(self, ids, flag):
        """
        :param ids: 数据库id列表
        :param flag: 1.学生 2.班级 3.角色 4.班级
        :return:
        """
        global all_header_combobox
        if flag == C.FLAG_GRADE:
            title = '清零'
            tips = '确定清零该学生成绩?' if len(ids) == 1 else '确定清零' + str(len(ids) - 1) + '个学生成绩?'
        else:
            title = '删除'
            tips = '确定删除该条数据?' if len(ids) == 1 else '确定删除' + str(len(ids) - 1) + '条数据?'

        reply = QMessageBox.question(self, title, tips, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if len(ids) <= 1:
                button = self.sender()
                if button:
                    # 确定位置的时候这里是关键
                    row = self.tableWidget.indexAt(button.parent().pos()).row()
                    if flag == C.FLAG_STUDENT:
                        result = sql_execute(delStudentById(ids[0]))
                        self.tableWidget.removeRow(row)
                        del all_header_combobox[row]
                    elif flag == C.FLAG_GRADE:
                        result = sql_execute(updateGradeById(ids[0], '0', '0', '0'))
                        self.tableWidget.item(row, 3).setText('0')
                        self.tableWidget.item(row, 4).setText('0')
                        self.tableWidget.item(row, 5).setText('0')
                        self.tableWidget.item(row, 6).setText('0')
                    elif flag == C.FLAG_CLASS:
                        result = sql_execute(getStudentByClassId(ids[0]))
                        if len(result) > 0:
                            QMessageBox.information(self, '失败', "该班级还有学生！请移除学生后再删除该班级。")
                            return
                        else:
                            sql_execute(delClassById(ids[0]))
                            self.tableWidget.removeRow(row)
                    elif flag == C.FLAG_ADMIN:
                        if ids[0] == 1:
                            QMessageBox.information(self, '失败', "超管账号不可删除！")
                            return
                        else:
                            sql_execute(delAdminById(ids[0]))
                            self.tableWidget.removeRow(row)

            else:
                errIds = []
                i = None
                for id in ids:
                    if flag == C.FLAG_STUDENT:
                        result = sql_execute(delStudentById(id))
                    elif flag == C.FLAG_GRADE:
                        result = sql_execute(updateGradeByNum(id, '0', '0', '0'))
                    elif flag == C.FLAG_CLASS:
                        result = sql_execute(getStudentByClassId(id))
                        if len(result) > 0:
                            errIds.append(id)
                            continue
                        else:
                            sql_execute(delClassById(id))
                    elif flag == C.FLAG_ADMIN:
                        if id == '1':
                            QMessageBox.information(self, '失败', "超管账号不可删除！")
                            continue
                        else:
                            sql_execute(delAdminById(id))
                        i = -1
                if flag == C.FLAG_CLASS:
                    if len(errIds) == 0:
                        QMessageBox.about(self, '操作完成', "成功删除班级%d个。" % (len(ids) - 1))
                    else:
                        QMessageBox.information(self, '操作完成',
                                                "成功删除班级%d个，失败%d个。\n失败班级id：%s\n这些班级内还有学生，无法删除，请移除学生后再进行该操作！"
                                                % (len(ids) - len(errIds) - 1, len(errIds), str(errIds)))
                    self.getDataList(flag=flag, i=-1)
                    return
                self.getDataList(flag=flag, i=i)

    # 查看详情
    def viewTable(self, id, flag):
        """
        :param id: 数据库id
        :param flag: xx管理
        :return:
        """
        if flag == C.FLAG_GRADE:
            result = sql_execute(getStudentById(id))
            result = result[0]
            sex = '男' if result[3] == 1 else '女'
            class_ = result[4]
            if class_ not in class_dict.keys():
                class_ = '/'
            else:
                class_ = class_dict[class_]
            total = result[5] + result[6] + result[7]
            str = 'id：%d\n姓名：%s        \n学号：%d\n性别：%s\n班级：%s\n语文成绩：%d\n数学成绩：%d\n英语成绩：%d\n总成绩：%d' \
                  % (result[0], result[1], result[2], sex, class_, result[5], result[6], result[7], total)

            QMessageBox.about(self, '详情', str)

    # 编辑、添加、提交、删除按钮
    def buttonForRow(self, id, flag, info=''):
        """
        :param id: 数据库中数据id
        :param flag: xx管理
        :param info: 其他附加信息
        :return:
        """
        widget = QWidget()

        # 编辑
        updateBtn = QPushButton('编辑')
        updateBtn.setStyleSheet(''' text-align : center;
                                              background-color : orange;
                                              height : 30px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')
        if flag == C.FLAG_CLASS:
            updateBtn.clicked.connect(lambda: self.editClass(id, info))
        elif flag == C.FLAG_ADMIN:
            updateBtn.clicked.connect(lambda: self.editAdmin(id))
        else:
            updateBtn.clicked.connect(lambda: self.editRow(id, flag))

        # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                        background-color : LightCoral;
                                        height : 30px;
                                        border-style: outset;
                                        border-radius: 5px;
                                        color: #fff;
                                        font : 13px; ''')
        deleteBtn.clicked.connect(lambda: self.deleteRow([id], flag))

        # 成绩管理
        if flag == C.FLAG_GRADE:
            updateBtn.setText("编辑")
            deleteBtn.setText("清零")
            # 查看
            viewBtn = QPushButton('详情')
            viewBtn.setStyleSheet(''' text-align : center;
                                      background-color : #5dc7f1;
                                      height : 30px;
                                      border-style: outset;
                                      border-radius: 5px;
                                      color: #fff;
                                      font : 13px; ''')

            viewBtn.clicked.connect(lambda: self.viewTable(id, flag))

        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        if flag == C.FLAG_GRADE:
            hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    # 添加提交、取消按钮
    def buttonForRowEdit(self, id, flag):
        """
        :param id: 数据库中数据id
        :param flag: xx管理
        :return:
        """
        widget = QWidget()
        # 提交
        updateBtn = QPushButton('提交')
        updateBtn.setStyleSheet(''' text-align : center;
                                              background-color : DarkSeaGreen;
                                              height : 30px;
                                              border-style: outset;
                                              border-radius: 5px;
                                              color: #fff;
                                              font : 12px  ''')

        updateBtn.clicked.connect(lambda: self.submitData(id, flag))

        # 取消
        cancelBtn = QPushButton('取消')
        cancelBtn.setStyleSheet(''' text-align : center;
                                        background-color : #aaa;
                                        height : 30px;
                                        border-style: outset;
                                        border-radius: 5px;
                                        color: #fff;
                                        font : 13px; ''')
        cancelBtn.clicked.connect(lambda: self.editRow(id, flag, False))

        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        hLayout.addWidget(cancelBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    # 获取并更新数据列表 i: 班级index
    def getDataList(self, flag, i=None):
        global all_class, data_list
        data_list = ()
        name = self.input_name.text()
        if i is None:
            i = self.cb.currentIndex()
        if i == 0:
            classIds = C.USER[4]
        elif i < 0:
            pass
        else:
            classIds = str(all_class[i - 1][0])
        if flag == C.FLAG_STUDENT:
            data_list = sql_execute(getStudentList(classIds, name))
        elif flag == C.FLAG_GRADE:
            data_list = sql_execute(getGradeList(classIds, name))
        elif flag == C.FLAG_CLASS:
            data_list = self.getClassList(name)
        elif flag == C.FLAG_ADMIN:
            data_list = sql_execute(getAdminList(name))
        self.addTableRow(flag, data_list)

    # 添加数据
    def addTableRow(self, flag, dataList):
        global all_header_combobox, class_dict
        all_header_combobox = []

        self.tableWidget.setRowCount(0)
        if len(dataList) == 0:
            self.tableWidget.setRowCount(1)
            item = QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setText("无数据")
            self.tableWidget.setItem(0, 0, item)
            return

        self.tableWidget.setRowCount(len(dataList))
        i = 0
        for data in dataList:
            if not (flag == C.FLAG_ADMIN and data[0] == 1):
                checkbox1 = QtWidgets.QCheckBox()
                # 将所有的复选框都添加到 全局变量 all_header_combobox 中
                all_header_combobox.append(checkbox1)
                # 1.实例化一个新布局
                hLayout = QtWidgets.QFormLayout()
                # 2.在布局里添加checkBox
                hLayout.addWidget(checkbox1)
                # 3.在布局里居中放置checkbox1
                hLayout.setAlignment(checkbox1, QtCore.Qt.AlignCenter)
                # 4.实例化一个QWidget（控件）
                widget = QtWidgets.QWidget()
                # 5.在QWidget放置布局
                widget.setLayout(hLayout)
                # 6.在tableWidget1放置widget
                self.tableWidget.setCellWidget(i, 0, widget)
            if flag == C.FLAG_STUDENT:
                item = QTableWidgetItem(str(data[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 1, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(data[1])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 2, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(data[2]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 3, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText('男' if data[3] == 1 else '女')
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 4, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(class_dict[data[4]])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 5, item)
                self.tableWidget.setCellWidget(i, 6, self.buttonForRow(data[0], C.FLAG_STUDENT))
            elif flag == C.FLAG_GRADE:
                item = QTableWidgetItem(str(data[1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 1, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(data[2]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 2, item)

                chinese = data[5] if data[5] is not None else 0
                math = data[6] if data[6] is not None else 0
                english = data[7] if data[7] is not None else 0
                total = chinese + math + english

                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(chinese))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 3, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(math))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 4, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(english))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 5, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(total))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 6, item)
                self.tableWidget.setCellWidget(i, 7, self.buttonForRow(data[0], C.FLAG_GRADE))
            elif flag == C.FLAG_CLASS:
                item = QTableWidgetItem(str(data[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 1, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(data[1]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 2, item)
                self.tableWidget.setCellWidget(i, 3, self.buttonForRow(data[0], C.FLAG_CLASS, info=data[1]))
            elif flag == C.FLAG_ADMIN:
                item = QTableWidgetItem(str(data[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 1, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(data[1]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 2, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(data[3]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 3, item)
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                try:
                    class_dict = {}
                    all_class = self.getClassList()
                    for class_ in all_class:
                        # 添加班级字典
                        class_dict[str(class_[0])] = class_[1]
                    classs = 'All'
                    if data[4] == '':
                        classs = '无'
                    elif data[4] != '0':
                        data4 = data[4].split(',')
                        classs = "/".join(class_dict[d] for d in data4)
                except Exception as e:
                    classs = 'err: 数据有误！'
                item.setText(classs)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 4, item)
                # 超管
                if data[0] == 1:
                    item = QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setText('无权限')
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 5, item)
                else:
                    self.tableWidget.setCellWidget(i, 5, self.buttonForRow(data[0], C.FLAG_ADMIN))
            i += 1

    # 获取班级列表
    def getClassList(self, name=''):
        print("获取班级列表")
        return sql_execute(getClassList(C.USER[4], name))

    # 设置左侧选中菜单按钮的样式
    def setLeftMenu(self, button):
        global activate_menu
        if activate_menu != None:
            activate_menu.setStyleSheet('''
                        width:20px;
                        font-size:15px;
                        ''')
        activate_menu = button
        button.setStyleSheet('''
                    width:20px;
                    font-size:15px;
                    border-left:4px solid #00bcd4;
                    font-weight:700;
                    ''')

    # 新增数据
    def createData(self, flag):
        if flag == C.FLAG_CLASS:
            text, okPressed = QInputDialog.getText(self, "新增班级", "班级名称:", QLineEdit.Normal, "")
            if okPressed and text != '':
                try:
                    sql_execute(insertClass(text))
                    QMessageBox.about(self, '成功', '新增班级成功！')
                    self.getDataList(flag, i=-1)
                except Exception as e:
                    QMessageBox.critical(self, '失败', '新增班级失败：\n' + e)

    # 编辑班级
    def editClass(self, id, old):
        text, okPressed = QInputDialog.getText(self, "编辑班级", "班级名称:", QLineEdit.Normal, old)
        if okPressed and text != '':
            try:
                sql_execute(updateClassById(id, text))
                QMessageBox.about(self, '成功', '班级编辑成功！')
                self.getDataList(C.FLAG_CLASS, i=-1)
            except Exception as e:
                QMessageBox.critical(self, '失败', '编辑班级失败：\n' + e)

    # 退出登录
    def logOut(self, tips=False):
        if tips:
            reply = QMessageBox.question(self, '退出登录', '确定要退出登录吗？', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply != QMessageBox.Yes:
                return
        gl_user = ()
        self.aw = C.LOGIN_WINDOW  # 创建主窗体对象，实例化Ui_MainWindow
        self.w = QMainWindow()  # 实例化QMainWindow类
        self.aw.setupUi(self.w)  # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
        self.w.show()  # 显示主窗体
        self.hide()

    # 修改用户名
    def editUsername(self):
        reply = QMessageBox.question(self, '修改用户名', '修改用户名后，需要重新登录。是否继续？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            username = self.input_name.text()
            sql_execute(updateUsernameById(C.USER[0], username))
            QMessageBox.about(self, '成功', '用户名修改成功！请重新登录。')
            self.logOut(False)
            # self.aw = Ui_MainWindow()  # 创建主窗体对象，实例化Ui_MainWindow
            # self.w = QMainWindow()  # 实例化QMainWindow类
            # self.aw.setupUi(self.w)  # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
            # self.w.show()  # 显示主窗体

    # 修改密码
    def modifyPassw(self):
        pass0 = self.input_pass0.text()
        pass1 = self.input_pass1.text()
        pass2 = self.input_pass2.text()
        if pass1 != pass2:
            QMessageBox.information(self, '错误', '两次密码输入不一致。')
            return
        else:
            if C.USER[2] != md5(pass0):
                QMessageBox.information(self, '错误', '原密码不正确！')
                return
            else:
                sql_execute(resetAdminPasswById(C.USER[0], pass1))
                QMessageBox.about(self, '成功', '密码修改成功！请重新登录。')
                self.logOut(False)

    # 编辑角色
    def editAdmin(self, id):
        self.aw = EditAdmin()  # 创建主窗体对象，实例化Ui_MainWindow
        self.w = QMainWindow()  # 实例化QMainWindow类
        self.aw.setupUi(self.w, id)  # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
        self.w.show()  # 显示主窗体

    # 新增角色
    def addAdmin(self):
        self.aw = AddAdmin()  # 创建主窗体对象，实例化Ui_MainWindow
        self.w = QMainWindow()  # 实例化QMainWindow类
        self.aw.setupUi(self.w)  # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
        self.w.show()  # 显示主窗体

    # 导入数据
    def open_file(self, flag):
        """
        :param flag: xx管理
        :return:
        """
        data_format = ''
        if flag == C.FLAG_STUDENT:
            data_format = '姓名/学号/性别/班级'
        elif flag == C.FLAG_GRADE:
            data_format = '姓名/学号/语文成绩/数学成绩/英语成绩'
        QMessageBox.information(self, '导入',
                                "请在弹出的文件选择框中选择数据文件（仅支持csv格式文件）！\n 数据格式：%s，从第2行开始读数据" % data_format)
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd()+'/data', "CSV Files(*.csv)")
        if fileName == '':
            return
        try:
            data = pd.read_csv(fileName)
        except Exception as e:
            data = pd.read_csv(fileName, encoding='gbk')
            print(e)

        success_count = fail_count = 0
        errText = ''

        for d in data.itertuples():
            try:
                # 学生管理
                if flag == C.FLAG_STUDENT:
                    sex = '1' if d[3] == '男' else '2'
                    class_ = d[4]
                    if class_ not in class_dict2.keys():
                        fail_count += 1
                        errText += '\n %s : 班级[%s]不存在/无权访问！' % (d[1], class_)
                        continue
                    else:
                        class_ = class_dict2[class_]
                        sql_execute(insertStudent(d[1], d[2], sex, class_))
                        success_count += 1
                elif flag == C.FLAG_GRADE:
                    sql_execute(updateGradeByNum(d[2], d[3], d[4], d[5]))
                    success_count += 1
            except Exception as e:
                fail_count += 1
                errText += '\n %s : %s' % (d[1], e)

        if fail_count > 0:
            QMessageBox.about(self, '导入完成',
                              "数据成功导入%d条，失败%d条。\n错误信息如下：%s" % (success_count, fail_count, errText))
        else:
            QMessageBox.about(self, '导入成功', "成功导入数据%d条！" % success_count)
        # 刷新列表
        self.getDataList(flag)

    # 数据导出
    def data_export(self, flag):
        """
        :param flag: xx管理
        :return:
        """
        global data_list
        self.getDataList(flag)
        filename = ''
        columns = []
        if flag == C.FLAG_STUDENT:
            filename = 'Students'
            columns = ['姓名', '学号', '性别', '班级']
        elif flag == C.FLAG_GRADE:
            filename = 'Grade'
            columns = ['姓名', '学号', '语文成绩', '数学成绩', '英语成绩', '总分', '排名']
        # 保存文件对话框
        file_path = QFileDialog.getSaveFileName(self, "数据导出", "data/%s.csv" % filename,
                                                "CSV Files(*.csv);;all files(*.*)")
        if file_path[0] == '':
            return
        try:
            save_data = pd.DataFrame(columns=columns)
            for index, data in enumerate(data_list):
                d = []
                if flag == C.FLAG_STUDENT:
                    sex = '男' if data[3] == 1 else '女'
                    class_ = data[4]
                    if class_ not in class_dict.keys():
                        class_ = '/'
                    else:
                        class_ = class_dict[class_]
                    d = [data[1], data[2], sex, class_]
                elif flag == C.FLAG_GRADE:
                    total = int(data[5]) + int(data[6]) + int(data[7])
                    d = [data[1], data[2], data[5], data[6], data[7], total, index + 1]
                save_data.loc[index] = d
            save_data.to_csv(file_path[0], index=False)
            QMessageBox.about(self, '成功', "数据成功导出至：%s" % file_path[0])
        except Exception as e:
            QMessageBox.critical(self, '保存失败', "保存失败：%s" % e)
            print(e)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


# 测试用入口
if __name__ == '__main__':
    main()
