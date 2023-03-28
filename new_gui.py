# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, \
    QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.btn_add.setObjectName("btn_add")

        self.line_blender = QtWidgets.QLineEdit(self.centralwidget)
        self.line_blender.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.line_blender.setObjectName("line_blender")

        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.btn_browse.setObjectName("btn_browse")

        self.line_threads = QtWidgets.QLineEdit(self.centralwidget)
        self.line_threads.setGeometry(QtCore.QRect(300, 60, 113, 20))
        self.line_threads.setObjectName("line_threads")

        #self.line_11 = QtWidgets.QLineEdit(self.centralwidget)
        #self.line_11.setGeometry(QtCore.QRect(20, 130, 113, 20))
        #self.line_11.setObjectName("line_11")
        #self.line_12 = QtWidgets.QLineEdit(self.centralwidget)
        #self.line_12.setGeometry(QtCore.QRect(250, 130, 113, 20))
        #self.line_12.setObjectName("line_12")
        #self.btn_browse11 = QtWidgets.QPushButton(self.centralwidget)
        #self.btn_browse11.setGeometry(QtCore.QRect(140, 130, 75, 23))
        #self.btn_browse11.setObjectName("btn_browse11")
        #self.btn_browse12 = QtWidgets.QPushButton(self.centralwidget)
        #self.btn_browse12.setGeometry(QtCore.QRect(370, 130, 75, 23))
        #self.btn_browse12.setObjectName("btn_browse12")
        #self.line_13 = QtWidgets.QLineEdit(self.centralwidget)
        #self.line_13.setGeometry(QtCore.QRect(460, 130, 31, 20))
        #self.line_13.setObjectName("line_13")
        #self.line_14 = QtWidgets.QLineEdit(self.centralwidget)
        #self.line_14.setGeometry(QtCore.QRect(510, 130, 31, 20))
        #self.line_14.setObjectName("line_14")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add.setText(_translate("MainWindow", "Add File"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        #self.btn_browse11.setText(_translate("MainWindow", "Browse"))
        #self.btn_browse12.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setText(_translate("MainWindow", "Render"))


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("my window")
        self.setGeometry(560, 240, 800, 600)
        self.setMinimumSize(600, 400)
        self.files = 0

        btn_add = QPushButton("Add File", self)
        #btn_add.move(20, 20)
        btn_add.setGeometry(QtCore.QRect(20, 20, 75, 20))
        btn_add.clicked.connect(self.addFile)

        line_blender = QLineEdit(self)
        #line_blender.move(20, 60)
        line_blender.setGeometry(QtCore.QRect(20, 60, 113, 20))

        btn_browse = QPushButton("Browse", self)
        #btn_browse.move(140, 60)
        btn_browse.setGeometry(QtCore.QRect(140, 60, 75, 20))

        line_threads = QLineEdit(self)
        #line_threads.move(300, 60)
        line_threads.setGeometry(QtCore.QRect(300, 60, 113, 20))

        btn_render = QPushButton("Render", self)
        # btn_browse.move(140, 60)
        btn_render.setGeometry(QtCore.QRect(20, 400, 75, 20))

        #self.layout = QGridLayout(self)
        #self.layout_add = QHBoxLayout(self)
        #self.layout_blender = QHBoxLayout(self)
        #self.layout_files = QGridLayout(self)
        #self.layout_files.setRowStretch(0, 3)
        #self.layout_files.setGeometry(QtCore.QRect(20, 100, 100, 20))

        #self.layout.addLayout(self.layout_add)
        #self.layout.addLayout(self.layout_blender)
        #self.layout.addLayout(self.layout_files)

        #self.layout_add.addWidget(btn_add)
        #self.layout_blender.addWidget(line_blender)
        #self.layout_blender.addWidget(btn_browse)
        #self.layout_blender.addWidget(line_threads)

    def addFile(self):
        print('Line {} will be created'.format(self.files+1))
        btn_browse1 = QPushButton('Browse', self)
        btn_browse2 = QPushButton('Browse', self)
        line_1 = QLineEdit(self)
        line_2 = QLineEdit(self)
        btn_browse1.setObjectName('Browse_{}1'.format(self.files + 1))
        btn_browse2.setObjectName('Browse_{}2'.format(self.files + 1))
        line_1.setObjectName('Line_{}1'.format(self.files+1))
        line_2.setObjectName('Line_{}2'.format(self.files + 1))
        #btn_new.clicked.connect(lambda: print(btn_new.text()))

        line_1.setGeometry(QtCore.QRect(20, 60 + 40 * (self.files + 1), 120, 20))
        btn_browse1.setGeometry(QtCore.QRect(150, 60 + 40 * (self.files + 1), 80, 20))
        line_2.setGeometry(QtCore.QRect(240, 60 + 40 * (self.files + 1), 120, 20))
        btn_browse2.setGeometry(QtCore.QRect(370, 60 + 40 * (self.files + 1), 80, 20))

        line_1.show()
        btn_browse1.show()
        line_2.show()
        btn_browse2.show()

        #self.layout_files.addWidget(line_1, self.files, 0)
        #self.layout_files.addWidget(btn_browse1, self.files, 0)
        #self.layout_files.addWidget(line_2, self.files, 0)
        #self.layout_files.addWidget(btn_browse2, self.files, 0)
        self.files += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())