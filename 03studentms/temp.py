import os
from PyQt5 import QtCore, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import *
import pandas as pd
from PyQt5.QtCore import Qt, pyqtSignal, QRect
import Config as C


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


    # 学生管理界面设计
    def student_management(self):
        self.right_layout = self.verticalLayout
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第2列，占12行10列

        self.widget = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # 内容区域
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
