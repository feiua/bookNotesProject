import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
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
        # Code to create a new file goes here
        pass

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
