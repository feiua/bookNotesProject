import sys
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap, QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, \
    QDialog, QLineEdit, QGridLayout, QFormLayout, QTextEdit, QRadioButton, QCheckBox, QSlider, QSpinBox

'''
对话框 QDialog 的案例
QT中的对话框
QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog
窗口
QMainWindow
QWidget
QDialog
'''


class QDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置定位和左上角坐标
        self.setGeometry(300, 300, 400, 250)
        # 设置窗口标题
        self.setWindowTitle('对话框 QDialog 的演示')
        # 设置窗口图标
        # self.setWindowIcon(QIcon('../web.ico'))

        # 创建控件
        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle('对话框')
        # 设置模式为模态框
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置应用图标
    app.setWindowIcon(QIcon('../web.ico'))
    w = QDialogDemo()
    w.show()
    sys.exit(app.exec_())