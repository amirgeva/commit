from PyQt5 import QtCore, QtGui, QtWidgets
import uis
import utils


def commitFile(root, filename, status, comment):
    cmd = 'add'
    if status.find('Deleted') >= 0:
        cmd = 'rm'
    utils.call(root, 'git', cmd, filename)
    utils.call(root, 'git', 'commit', '-m', comment)


class ToolsDialog(QtWidgets.QDialog):
    """
    Dialog placed in a docking bar to provide means to perform actions on the
    list of files in the central list widget
    """

    def __init__(self, mainwin, table, parent=None):
        super(ToolsDialog, self).__init__(parent)
        uis.loadDialog('tools', self)
        self.mainWindow = mainwin
        self.root = mainwin.root
        self.table = table
        self.autoCommitCB.stateChanged.connect(self.toggledAutoCommit)
        s = QtCore.QSettings()
        state = s.value('auto_commit', QtCore.Qt.Unchecked)
        self.autoCommitCB.setCheckState(state > 0)
        self.selectAllButton.clicked.connect(self.selectAllClicked)
        self.selectNoneButton.clicked.connect(self.selectNoneClicked)
        self.groupCommentButton.clicked.connect(self.groupCommentClicked)
        self.groupCommentButton.setDisabled(True)
        self.commitButton.clicked.connect(self.commitClicked)
        self.commitButton.setDisabled(True)
        self.pushButton.clicked.connect(self.pushClicked)
        self.table.cellChanged.connect(self.tableCellChanged)
        self.updating = False

    def toggledAutoCommit(self, state):
        s = QtCore.QSettings()
        s.setValue('auto_commit', state)
        s.sync()

    def selectAllClicked(self):
        self.updating = True
        n = self.table.rowCount()
        for i in range(0, n):
            self.table.item(i, 0).setCheckState(QtCore.Qt.Checked)
        self.updating = False
        self.tableCellChanged()

    def selectNoneClicked(self):
        self.updating = True
        n = self.table.rowCount()
        for i in range(0, n):
            self.table.item(i, 0).setCheckState(QtCore.Qt.Unchecked)
        self.updating = False
        self.tableCellChanged()

    def groupCommentClicked(self):
        (text, ok) = QtWidgets.QInputDialog.getText(self, "Group Comment", "Comment")
        if ok:
            self.updating = True
            n = self.table.rowCount()
            for i in range(0, n):
                if self.table.item(i, 0).checkState() == QtCore.Qt.Checked:
                    self.table.item(i, 2).setText(text)
                    self.table.item(i, 0).setCheckState(QtCore.Qt.Unchecked)
            self.updating = False
            self.tableCellChanged()

    def commitClicked(self):
        n = self.table.rowCount()
        for i in range(0, n):
            comment = str(self.table.item(i, 2).text())
            if len(comment) > 0:
                filename = str(self.table.item(i, 0).text())
                status = str(self.table.item(i, 1).text())
                commitFile(self.root, filename, status, comment)
        self.updating = True
        self.mainWindow.update()
        self.updating = False
        self.tableCellChanged()

    def pushClicked(self):
        (out, err) = utils.call(self.root, 'git', 'push')
        QtWidgets.QMessageBox.information(self, "Push", out + err)

    def tableCellChanged(self, row=0, col=0):
        if self.updating:
            return
        n = self.table.rowCount()
        checks = 0
        comments = 0
        for i in range(0, n):
            fileText = self.table.item(i, 0)
            if fileText and fileText.checkState() == QtCore.Qt.Checked:
                checks = checks + 1
            commentText = self.table.item(i, 2)
            if commentText and len(commentText.text()) > 0:
                comments = comments + 1
        self.groupCommentButton.setEnabled(checks > 0)
        self.commitButton.setEnabled(comments > 0)
        if comments > 0 and self.autoCommitCB.checkState() == QtCore.Qt.Checked:
            self.commitClicked()


class GeneralSettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(GeneralSettingsDialog, self).__init__(parent)
        uis.loadDialog('general_settings', self)
        s = QtCore.QSettings()
        self.diffCmd.setText(s.value('diff').toString())
        xterm = QtCore.Qt.Checked if s.value('xterm').toString() == 'True' else QtCore.Qt.Unchecked
        self.runInXTerm.setCheckState(xterm)

    def accept(self):
        s = QtCore.QSettings()
        diff = self.diffCmd.text()
        s.setValue('diff', diff)
        xterm = 'True' if self.runInXTerm.checkState() == QtCore.Qt.Checked else 'False'
        s.setValue('xterm', xterm)
        s.sync()
        super(GeneralSettingsDialog, self).accept()
