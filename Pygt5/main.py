import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, qApp


def window():
    app= QApplication(sys.argv)
    win= QMainWindow()

    win.show()
    sys.exit(app.exec())

window()