import sys
from PyQt5.QtWidgets import *
from interface.notebook_widgets import *


class Notebook(QMainWindow):
    def __init__(self, parent=None):
        super(Notebook, self).__init__(parent)
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        newAction = QAction('New', self)
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)

        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Notebook')
        self.show()

    def newFile(self):
        # name, ok = QInputDialog.getText(self, 'New Notebook', 'Notebook Name:')
        # if ok:
        #     description, ok = QInputDialog.getText(self, 'New Notebook', 'Description:')
        #     if ok:
        #         time, ok = QInputDialog.getText(self, 'New Notebook', 'Time:')
        #         if ok:
        #             location, ok = QInputDialog.getText(self, 'New Notebook', 'Location:')
        #             if ok:
        #                 # Code to create a new file with the given information goes here
        #                 pass

        # 创建一个表单布局
        widget = CreateNewNotebookWindow()
        widget.exec()

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if fileName:
            # Code to open the selected file goes here
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notebook = Notebook()
    sys.exit(app.exec_())
