# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# class Ui_MainWindow(QtGui.QMainWindow):
class Ui_MainWindow(QtWidgets.QMainWindow):
# class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Songs Recognizer")
        MainWindow.resize(1061, 716)
        MainWindow.setBaseSize(QtCore.QSize(723, 361))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.File1_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.File1_Browse.setMaximumSize(QtCore.QSize(200, 30))
        self.File1_Browse.setObjectName("File1_Browse")
        self.gridLayout.addWidget(self.File1_Browse, 2, 1, 1, 1)

        self.File2_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.File2_Browse.setMaximumSize(QtCore.QSize(200, 30))
        #self.File2_Browse.setIconSize(QtCore.QSize(10, 16))
        self.File2_Browse.setObjectName("File2_Browse")
        self.gridLayout.addWidget(self.File2_Browse, 3, 1, 1, 1)

        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setMaximumSize(QtCore.QSize(200, 30))
        self.Search.setObjectName("Search")
        self.gridLayout.addWidget(self.Search, 4,1,1,1)        

        spacerItem = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 10, 0, 1, 3)
        self.mixlabel = QtWidgets.QLabel(self.centralwidget)
        self.mixlabel.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.mixlabel.setFont(font)
        self.mixlabel.setObjectName("mixlabel")
        self.gridLayout.addWidget(self.mixlabel, 8, 0, 1, 1)
        self.song1vssong2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.song1vssong2.setFont(font)
        self.song1vssong2.setObjectName("song1vssong2")
        self.gridLayout.addWidget(self.song1vssong2, 5, 0, 1, 1)
        self.mixer = QtWidgets.QSlider(self.centralwidget)
        self.mixer.setOrientation(QtCore.Qt.Horizontal)
        self.mixer.setObjectName("mixer")
        self.gridLayout.addWidget(self.mixer, 5, 1, 1, 2)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.name_song1 = QtWidgets.QLabel(self.centralwidget)
        font.setWeight(75)
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.name_song1.setObjectName("name_song1")
        self.gridLayout.addWidget(self.name_song1, 2, 2, 1, 1)
        #spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem, 6, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.name_song2 = QtWidgets.QLabel(self.centralwidget)
        self.name_song2.setObjectName("name_song2")
        self.gridLayout.addWidget(self.name_song2, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.File1_Browse.setText(_translate("MainWindow", "Aud 1"))
        self.File2_Browse.setText(_translate("MainWindow", "Aud 2"))
        self.tableWidget.setColumnWidth(0, 600)
        self.tableWidget.setColumnWidth(1, 200)
        self.Search.setText(_translate("MainWindow", "Find Similarity"))
        item = self.tableWidget.horizontalHeaderItem(0) #table row 1
        item.setText(_translate("MainWindow", "Aud Name"))
        item = self.tableWidget.horizontalHeaderItem(1) #table row 2
        item.setText(_translate("MainWindow", "Similarity Index")) 
        #item = self.tableWidget.horizontalHeaderItem(2) #table row 3
        #item.setText(_translate("MainWindow", "artist")) 
        self.label_1.setText(_translate("MainWindow", "Select Aud 1 "))
        self.name_song1.setText(_translate("MainWindow", "Aud1 Name"))
        self.label_2.setText(_translate("MainWindow", "Select Aud 2"))
        self.name_song2.setText(_translate("MainWindow", "Aud2 Name"))
        self.mixlabel.setText(_translate("MainWindow", "Aud Matching"))
        self.song1vssong2.setText(_translate("MainWindow", "Aud 1 : Aud 2"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

