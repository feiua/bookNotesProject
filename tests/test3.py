from PyQt5.QtWidgets import QApplication, QDesktopWidget

app = QApplication([])
screen = QDesktopWidget().screenGeometry()
width, height = screen.width(), screen.height()

print(f"Screen size: {width}x{height}")