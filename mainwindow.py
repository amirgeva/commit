from PyQt4 import QtCore, QtGui
import scanner


class MainWindow(QtGui.QMainWindow):
    def __init__(self,root,parent=None):
        super(MainWindow,self).__init__(parent)
        self.root=root
        self.setMinimumSize(QtCore.QSize(800,600))
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        #self.timer.start(2000)
        self.fileTable=QtGui.QTableWidget(self)
        self.fileTable.setColumnCount(3)
        self.fileTable.horizontalHeader().setResizeMode(2,QtGui.QHeaderView.Stretch)
        self.fileTable.setHorizontalHeaderLabels(['File','Status','Comment'])
        self.dataDict={}
        self.update()
        self.setCentralWidget(self.fileTable)
        self.dock=QtGui.QDockWidget("Tools",self)
        self.dock.setAllowedAreas(QtCore.Qt.TopDockWidgetArea|QtCore.Qt.BottomDockWidgetArea)
        import tools
        self.dock.setWidget(tools.ToolsDialog(self,self.fileTable))
        self.dock.setMinimumHeight(150)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea,self.dock)
        self.dock.widget().show()
        #self.createToolbar()
        
    def createToolbar(self):
        tb=self.addToolBar('Actions')
        tb.addAction('All').triggered.connect(self.selectAll)
        tb.addAction('None').triggered.connect(self.selectNone)
        tb.addAction('Commit').triggered.connect(self.commit)
        return tb
        
    def editEnded(self,row,col):
        if not self.updating:
            print "Item changed: {},{}".format(row,col)
        
    def resizeEvent(self,event):
        s=event.size()
        newSize=self.fileTable.size()
        newSize.setWidth(s.width())
        self.fileTable.resize(newSize)
        
    def update(self):
        self.updating=True
        newRows=scanner.scan(self.root,self.dataDict)
        modified=False
        if len(newRows)<self.dataDict:
            modified=True
        else:
            for row in newRows:
                if row[0] in self.dataDict:
                    if row!=self.dataDict.get(row[0]):
                        modified=True
                        break
                else:
                    modified=True
                    break
                
        if modified:
            self.dataDict={}
            self.fileTable.setRowCount(len(newRows))
            flags=[QtCore.Qt.ItemIsUserCheckable,0,QtCore.Qt.ItemIsEditable]
            for j in xrange(0,3):
                flags[j]=flags[j]|QtCore.Qt.ItemIsEnabled
            for i in xrange(0,len(newRows)):
                row=newRows[i]
                for j in xrange(0,3):
                    item=QtGui.QTableWidgetItem(row[j])
                    item.setFlags(flags[j])
                    if j==0:
                        item.setCheckState(QtCore.Qt.Unchecked)
                    self.fileTable.setItem(i,j,item)
                self.dataDict[row[0]]=row
            self.fileTable.resizeColumnToContents(0)
            self.fileTable.resizeColumnToContents(1)
        self.updating=False
        
    def selectAll(self):
        n=self.fileTable.rowCount()
        for i in xrange(0,n):
            self.fileTable.item(i,0).setCheckState(QtCore.Qt.Checked)
            
    def selectNone(self):
        n=self.fileTable.rowCount()
        for i in xrange(0,n):
            self.fileTable.item(i,0).setCheckState(QtCore.Qt.Unchecked)
            
    def commit(self):
        pass