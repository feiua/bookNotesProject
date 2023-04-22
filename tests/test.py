import sys
from PyQt5.QtWidgets import *
from interface.notebook_widgets import *
from db import data_control as dataCon


class Notebook(QMainWindow):
    def __init__(self, parent=None):
        super(Notebook, self).__init__(parent)
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        newAction = QAction('New', self)
        newAction.triggered.connect(self.newNotebook)
        fileMenu.addAction(newAction)

        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openNotebook)
        fileMenu.addAction(openAction)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Notebook')
        self.show()

    def newNotebook(self):
        # pump up a dialog window for inserting information of a new notebook
        book_dialog = CreateNewNotebookWindow()
        book_dialog.exec_()

        # insert information of a new notebook into database
        name = book_dialog.notebook_name
        description = book_dialog.notebook_desc
        time = book_dialog.notebook_time
        location = book_dialog.notebook_loca

        if book_dialog.SUCCESSFULLY_ESTABLISHED:
            dataCon.create_notebook(name, description, time, location)



    def openNotebook(self):
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
