"""
项目名称：python pyqt5 mysql 学生管理系统
作者：bhml
时间：2022/11/28
代码功能：一、登录界面与功能实现
"""
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from main import MainUi
from sqls import *

from db import *
import Config as C


# 界面与登录功能的设计与实现
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 350, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setBaseSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(27)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 140, 181, 31))
        font = QtGui.QFont("Microsoft YaHei")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 91, 31))
        font = QtGui.QFont("Microsoft YaHei")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 91, 31))
        font = QtGui.QFont("Microsoft YaHei")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 190, 181, 31))
        font = QtGui.QFont("Microsoft YaHei")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 280, 160, 40))
        font = QtGui.QFont("Microsoft YaHei")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        font = QtGui.QFont("Microsoft YaHei")
        font.setItalic(False)
        font.setPointSize(14)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 240, 250, 20))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.centralwidget.setStyleSheet('''
                    QLabel#label_6{
                        color:red;
                    }
                    #pushButton{background-color:#2c7adf;color:#fff;border:none;border-radius:4px;}
                    #pushButton:hover{background-color:#2c8adf;}
                ''')
        self.pushButton.clicked.connect(lambda: self.btn_clicked(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python学生管理系统-管理员登录"))
        self.label.setText(_translate("MainWindow", "Python学生管理系统"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入用户名"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密码："))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.pushButton.setText(_translate("MainWindow", "登录"))

    # 管理员登录
    def btn_clicked(self, MainWindow):
        self.label_6.setText("正在登录...")
        self.pushButton.setDisabled(True)
        QApplication.processEvents()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        result = sql_execute(login(username, password))
        if len(result) == 0:
            self.label_6.setText("登录失败：用户名或密码错误")
            self.pushButton.setDisabled(False)
            print(username + "登录失败！")
        else:
            print(username + "登录成功！")
            self.label_6.setText("登录成功！")
            print(result[0])
            C.USER = result[0]
            self.main = MainUi()
            self.main.show()
            C.LOGIN_WINDOW = aw
            MainWindow.hide()
            self.main.setWindowTitle('Python学生管理系统')


if __name__ == "__main__":
    App = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    aw = Ui_MainWindow()  # 创建主窗体对象，实例化Ui_MainWindow
    w = QMainWindow()  # 实例化QMainWindow类
    aw.setupUi(w)  # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
    w.show()  # 显示主窗体
    w.setWindowTitle('Python学生管理系统-管理员登录')
    sys.exit(App.exec_())  # 循环中等待退出程序
