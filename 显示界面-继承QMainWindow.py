# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_de.ui'
# Created by: PyQt5 UI code generator 5.11.3
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treewidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treewidget.setGeometry(QtCore.QRect(10, 200, 221, 341))
        self.treewidget.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.treewidget.setFont(font)
        self.treewidget.setStyleSheet("#treewidget::item\n"
            "{\n"
            "height:32px;\n"
            "background-color:\n"
            "qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, "
                "stop:0 rgba(255, 235, 235, 206), "
                "stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), "
                "stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), "
                "stop:1 rgba(255, 255, 255, 0));\n"
                "color:rgb(0, 0, 255);\n"
            "}")
        self.treewidget.setFrameShape(QtWidgets.QFrame.Box)
        self.treewidget.setAutoScrollMargin(16)
        self.treewidget.setAutoExpandDelay(2)
        self.treewidget.setIndentation(20)
        self.treewidget.setHeaderHidden(True)
        self.treewidget.setColumnCount(1)
        self.treewidget.setObjectName("treewidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treewidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treewidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treewidget)
        self.label_right = QtWidgets.QLabel(self.centralwidget)
        self.label_right.setGeometry(QtCore.QRect(230, 200, 651, 341))
        self.label_right.setObjectName("label_right")
        self.label_top = QtWidgets.QLabel(self.centralwidget)
        self.label_top.setGeometry(QtCore.QRect(10, 10, 871, 191))
        self.label_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_top.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_top.setObjectName("label_top")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treewidget.headerItem().setText(0, _translate("MainWindow", "质量检验"))
        __sortingEnabled = self.treewidget.isSortingEnabled()
        self.treewidget.setSortingEnabled(False)
        self.treewidget.topLevelItem(0).setText(0, _translate("MainWindow", "质量检验"))
        self.treewidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "上传质检结果"))
        self.treewidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "质检标准"))
        self.treewidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "质检任务"))
        self.treewidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "质检工单"))
        self.treewidget.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "统计分析"))
        self.treewidget.topLevelItem(0).child(4).child(0).setText(0, _translate("MainWindow", "不良品统计"))
        self.treewidget.topLevelItem(0).child(4).child(1).setText(0, _translate("MainWindow", "产品合格率"))
        self.treewidget.topLevelItem(1).setText(0, _translate("MainWindow", "质量追溯"))
        self.treewidget.topLevelItem(2).setText(0, _translate("MainWindow", "生产管理"))
        self.treewidget.setSortingEnabled(__sortingEnabled)
        self.label_right.setText(_translate("MainWindow", "右边背景"))
        self.label_top.setText(_translate("MainWindow", "上部背景"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    _mainwindow = QtWidgets.QMainWindow()
    mainui = Ui_MainWindow()
    mainui.setupUi(_mainwindow)
    mainui.show()
    sys.exit(app.exec_())
