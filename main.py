from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
import sys
from sqlite3 import Error


class MyWindow(QtWidgets.QMainWindow):
    ui_path = 'UI/'

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('Robot_ui.ui', self)


if __name__ == '__main__':
    qss_file = open('Remover.qss').read()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qss_file)
    window = MyWindow()
    window.resize(1280, 720)
    window.show()
    sys.exit(app.exec_())
