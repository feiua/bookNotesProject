from PyQt5.QtWidgets import *


class CreateNewNotebookWindow(QDialog):
    def __init__(self, parent=None):
        super(CreateNewNotebookWindow, self).__init__(parent)

        # information
        self.notebook_name = str()
        self.notebook_desc = str()
        self.notebook_time = str()
        self.notebook_loca = str()


        # 设置输入框组健
        self.time_line = QLineEdit(self)
        self.desc_line = QLineEdit(self)
        self.name_line = QLineEdit(self)
        self.loca_line = QLineEdit(self)

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
        self.name_line.setReadOnly(True)
        mainLayout.addRow(note_name_btn, self.name_line)

        description_btn = QPushButton('Description:', self)
        description_btn.setMinimumWidth(min_width)
        description_btn.clicked.connect(self.onGetDesc)
        self.desc_line.setReadOnly(True)
        mainLayout.addRow(description_btn, self.desc_line)

        time_btn = QPushButton('Description:', self)
        time_btn.setMinimumWidth(min_width)
        time_btn.clicked.connect(self.onGetTime)
        self.time_line.setReadOnly(True)
        mainLayout.addRow(time_btn, self.time_line)

        loaca_btn = QPushButton('Description:', self)
        loaca_btn.setMinimumWidth(min_width)
        loaca_btn.clicked.connect(self.onGetLoca)
        self.loca_line.setReadOnly(True)
        mainLayout.addRow(loaca_btn, self.loca_line)

        save_btn = QPushButton('Save', self)
        save_btn.setMinimumWidth(min_width)
        save_btn.clicked.connect(self.close())

        cancel_btn = QPushButton('Cancel', self)
        cancel_btn.setMinimumWidth(min_width)
        cancel_btn.clicked.connect(self.close())

        mainLayout.addRow(save_btn, cancel_btn)

        self.setLayout(mainLayout)

    def onGetName(self):
        self.notebook_name, ok = QInputDialog.getText(self, '名称输入对话框', '输入名称：')
        if ok:
            self.name_line.setText(str(self.notebook_name))

    def onGetDesc(self):
        self.notebook_desc, ok = QInputDialog.getText(self, '描述输入对话框', '输入描述：')
        if ok:
            self.desc_line.setText(str(self.notebook_desc))

    def onGetTime(self):
        self.notebook_time, ok = QInputDialog.getText(self, '时间输入对话框', '输入时间：')
        if ok:
            self.time_line.setText(str(self.notebook_time))

    def onGetLoca(self):
        self.notebook_loca, ok = QInputDialog.getText(self, '地址输入对话框', '输入地址：')
        if ok:
            self.loca_line.setText(str(self.notebook_loca))
