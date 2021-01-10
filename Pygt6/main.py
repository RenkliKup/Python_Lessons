import sys
from PyQt5.QtWidgets import QApplication,QMainWindow


def window():
    app=QApplication(sys.argv)
    win=QMainWindow()

    win.show()
    sys.exit(app.exec())

window()