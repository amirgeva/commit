# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/general_settings.ui'
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

class Ui_GeneralSettingsDialog(object):
    def setupUi(self, GeneralSettingsDialog):
        GeneralSettingsDialog.setObjectName(_fromUtf8("GeneralSettingsDialog"))
        GeneralSettingsDialog.resize(640, 480)
        GeneralSettingsDialog.buttonBox = QtGui.QDialogButtonBox(GeneralSettingsDialog)
        GeneralSettingsDialog.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        GeneralSettingsDialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        GeneralSettingsDialog.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        GeneralSettingsDialog.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        GeneralSettingsDialog.label = QtGui.QLabel(GeneralSettingsDialog)
        GeneralSettingsDialog.label.setGeometry(QtCore.QRect(20, 40, 84, 22))
        GeneralSettingsDialog.label.setObjectName(_fromUtf8("label"))
        GeneralSettingsDialog.diffCmd = QtGui.QLineEdit(GeneralSettingsDialog)
        GeneralSettingsDialog.diffCmd.setGeometry(QtCore.QRect(130, 30, 281, 32))
        GeneralSettingsDialog.diffCmd.setObjectName(_fromUtf8("diffCmd"))
        GeneralSettingsDialog.runInXTerm = QtGui.QCheckBox(GeneralSettingsDialog)
        GeneralSettingsDialog.runInXTerm.setGeometry(QtCore.QRect(440, 30, 161, 27))
        GeneralSettingsDialog.runInXTerm.setObjectName(_fromUtf8("runInXTerm"))

        self.retranslateUi(GeneralSettingsDialog)
        QtCore.QObject.connect(GeneralSettingsDialog.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GeneralSettingsDialog.accept)
        QtCore.QObject.connect(GeneralSettingsDialog.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GeneralSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GeneralSettingsDialog)

    def retranslateUi(self, GeneralSettingsDialog):
        GeneralSettingsDialog.setWindowTitle(_translate("GeneralSettingsDialog", "General Settings", None))
        GeneralSettingsDialog.label.setText(_translate("GeneralSettingsDialog", "Diff", None))
        GeneralSettingsDialog.runInXTerm.setText(_translate("GeneralSettingsDialog", "Run in xterm", None))

