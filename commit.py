#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
import sys
import os
from mainwindow import MainWindow


def main():
    root = os.path.abspath('.')
    if len(sys.argv) > 1:
        root = os.path.abspath(sys.argv[1])
    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("MLGSoft")
    QtCore.QCoreApplication.setOrganizationDomain("mlgsoft.com")
    QtCore.QCoreApplication.setApplicationName("commit")
    w = MainWindow(root)
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
