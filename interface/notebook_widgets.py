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

        note_name_btn = QPushButton('Notebook Name:', self)
        note_name_btn.setMinimumWidth(min_width)
        note_name_btn.clicked.connect(self.onGetName)
        self.name_line = QLineEdit(self)
        self.name_line.setReadOnly(True)
        mainLayout.addRow(note_name_btn, self.name_line)

        description_btn = QPushButton('Description:', self)
        description_btn.setMinimumWidth(min_width)
        description_btn.clicked.connect(self.onGetDesc)
        self.desc_line = QLineEdit(self)
        self.desc_line.setReadOnly(True)
        mainLayout.addRow(description_btn, self.desc_line)

        description_btn = QPushButton('Description:', self)
        description_btn.setMinimumWidth(min_width)
        description_btn.clicked.connect(self.onGetDesc)
        self.desc_line = QLineEdit(self)
        self.desc_line.setReadOnly(True)
        mainLayout.addRow(description_btn, self.desc_line)

        self.setLayout(mainLayout)

    def onGetName(self):
        notebook_name, ok = QInputDialog.getText(self, '名称输入对话框', '输入名称：')
        if ok:
            self.name_line.setText(str(notebook_name))

    def onGetDesc(self):
        notebook_desc, ok = QInputDialog.getText(self, '描述输入对话框', '输入描述：')
        if ok:
            self.name_line.setText(str(notebook_desc))