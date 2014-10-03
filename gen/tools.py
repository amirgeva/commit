# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/tools.ui'
#
# Created: Fri Oct  3 16:38:34 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_toolsDialog(object):
    def setupUi(self, toolsDialog):
        toolsDialog.setObjectName(_fromUtf8("toolsDialog"))
        toolsDialog.resize(640, 129)
        toolsDialog.selectAllButton = QtGui.QPushButton(toolsDialog)
        toolsDialog.selectAllButton.setGeometry(QtCore.QRect(10, 20, 119, 32))
        toolsDialog.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
        toolsDialog.selectNoneButton = QtGui.QPushButton(toolsDialog)
        toolsDialog.selectNoneButton.setGeometry(QtCore.QRect(140, 20, 119, 32))
        toolsDialog.selectNoneButton.setObjectName(_fromUtf8("selectNoneButton"))
        toolsDialog.groupCommentButton = QtGui.QPushButton(toolsDialog)
        toolsDialog.groupCommentButton.setGeometry(QtCore.QRect(270, 20, 171, 32))
        toolsDialog.groupCommentButton.setObjectName(_fromUtf8("groupCommentButton"))
        toolsDialog.autoCommitCB = QtGui.QCheckBox(toolsDialog)
        toolsDialog.autoCommitCB.setGeometry(QtCore.QRect(10, 70, 271, 27))
        toolsDialog.autoCommitCB.setObjectName(_fromUtf8("autoCommitCB"))
        toolsDialog.commitButton = QtGui.QPushButton(toolsDialog)
        toolsDialog.commitButton.setGeometry(QtCore.QRect(390, 70, 119, 32))
        toolsDialog.commitButton.setObjectName(_fromUtf8("commitButton"))

        self.retranslateUi(toolsDialog)
        QtCore.QMetaObject.connectSlotsByName(toolsDialog)

    def retranslateUi(self, toolsDialog):
        toolsDialog.setWindowTitle(_translate("toolsDialog", "Tools", None))
        toolsDialog.selectAllButton.setText(_translate("toolsDialog", "Select All", None))
        toolsDialog.selectNoneButton.setText(_translate("toolsDialog", "Select None", None))
        toolsDialog.groupCommentButton.setText(_translate("toolsDialog", "Group Comment", None))
        toolsDialog.autoCommitCB.setText(_translate("toolsDialog", "Auto commit on comment", None))
        toolsDialog.commitButton.setText(_translate("toolsDialog", "Commit", None))

