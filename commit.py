#!/usr/bin/env python
from PyQt4 import QtCore, QtGui
import sys
import os
from mainwindow import MainWindow

def main():
    root=os.path.abspath('.')
    if len(sys.argv)>1:
        root=os.path.abspath(sys.argv[1])
    app=QtGui.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("MLGSoft")
    QtCore.QCoreApplication.setOrganizationDomain("mlgsoft.com")
    QtCore.QCoreApplication.setApplicationName("commit")
    w=MainWindow(root)
    w.show()
    app.exec_()


if __name__=='__main__':
    main()

