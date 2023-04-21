from PyQt5.QtWidgets import *


class CreateNewNotebookWindow(QDialog):
    def __init__(self, parent=None):
        super(CreateNewNotebookWindow, self).__init__(parent)

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

        loaca_btn = QPushButton('Description:', self)
        loaca_btn.setMinimumWidth(min_width)
        loaca_btn.clicked.connect(self.onGetLoca)
        self.loca_line = QLineEdit(self)
        self.loca_line.setReadOnly(True)
        mainLayout.addRow(loaca_btn, self.loca_line)

        self.setLayout(mainLayout)

    def onGetLoca(self):
        time_desc, ok = QInputDialog.getText(self, '描述输入对话框', '输入地址：')
        if ok:
            self.loca_line.setText(str(time_desc))
