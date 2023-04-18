import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog, QFormLayout, QPushButton, QLineEdit)


class DemoInputDialog(QWidget):
    def __init__(self, parent=None):
        super(DemoInputDialog, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('实战PyQt5: QInputDialog Demo!')
        # 设置窗口大小
        self.resize(320, 240)
        self.initUi()

    def initUi(self):
        # 创建一个表单布局
        mainLayout = QFormLayout(self)

        # 设置内部控件之间的间隔
        mainLayout.setSpacing(16)
        min_width = 120

        btnGetSel = QPushButton('列表选择输入对话框', self)
        btnGetSel.setMinimumWidth(min_width)
        btnGetSel.clicked.connect(self.onGetSelItem)
        self.infoSel = QLineEdit(self)
        self.infoSel.setReadOnly(True)
        mainLayout.addRow(btnGetSel, self.infoSel)

        btnGetTxt = QPushButton('字符串输入对话框', self)
        btnGetTxt.setMinimumWidth(min_width)
        btnGetTxt.clicked.connect(self.onGetText)
        self.infoTxt = QLineEdit(self)
        self.infoTxt.setReadOnly(True)
        mainLayout.addRow(btnGetTxt, self.infoTxt)

        btnGetInt = QPushButton('整数输入对话框')
        btnGetInt.setMinimumWidth(min_width)
        btnGetInt.clicked.connect(self.onGetInt)
        self.infoInt = QLineEdit(self)
        self.infoInt.setReadOnly(True)
        mainLayout.addRow(btnGetInt, self.infoInt)

        btnGetDbl = QPushButton('浮点数输入对话框')
        btnGetDbl.setMinimumWidth(min_width)
        btnGetDbl.clicked.connect(self.onGetDouble)
        self.infoDbl = QLineEdit(self)
        self.infoDbl.setReadOnly(True)
        mainLayout.addRow(btnGetDbl, self.infoDbl)

        self.setLayout(mainLayout)

    def onGetSelItem(self):
        # 创建元组并并定义初始值
        items = ('C', 'C++', 'C#', 'Java', 'Java Script', 'Go', 'Python')
        # 获取item输入的值，以及ok键的点击与否(True 或False)
        item, ok = QInputDialog.getItem(self, "选择输入对话框", '语言列表', items, 0, False)
        if ok and item:
            # 满足条件时，设置单行文本框的文本
            self.infoSel.setText(item)

    def onGetText(self):
        text, ok = QInputDialog.getText(self, '文本输入对话框', '输入姓名：')
        if ok:
            self.infoTxt.setText(str(text))

    def onGetInt(self):
        num, ok = QInputDialog.getInt(self, '整数输入对话框', '输入整数')
        if ok:
            self.infoInt.setText(str(num))

    def onGetDouble(self):
        value, ok = QInputDialog.getDouble(self, '浮点数输入对话框', '输入浮点数')
        if ok:
            self.infoDbl.setText(str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoInputDialog()
    window.show()
    sys.exit(app.exec())
