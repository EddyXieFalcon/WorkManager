# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 660)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.btnAddSetting = QtWidgets.QPushButton(self.centralWidget)
        self.btnAddSetting.setObjectName("btnAddSetting")
        self.gridLayout.addWidget(self.btnAddSetting, 0, 1, 1, 1)
        self.btnDelSetting = QtWidgets.QPushButton(self.centralWidget)
        self.btnDelSetting.setObjectName("btnDelSetting")
        self.gridLayout.addWidget(self.btnDelSetting, 0, 2, 1, 1)
        self.btnEditSetting = QtWidgets.QPushButton(self.centralWidget)
        self.btnEditSetting.setObjectName("btnEditSetting")
        self.gridLayout.addWidget(self.btnEditSetting, 0, 3, 1, 1)
        self.tableWidgetSetting = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidgetSetting.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetSetting.setObjectName("tableWidgetSetting")
        self.tableWidgetSetting.setColumnCount(1)
        self.tableWidgetSetting.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSetting.setHorizontalHeaderItem(0, item)
        self.tableWidgetSetting.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSetting.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidgetSetting, 1, 0, 1, 4)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.btnAddUnit = QtWidgets.QPushButton(self.centralWidget)
        self.btnAddUnit.setObjectName("btnAddUnit")
        self.gridLayout_2.addWidget(self.btnAddUnit, 0, 1, 1, 1)
        self.btnDelUnit = QtWidgets.QPushButton(self.centralWidget)
        self.btnDelUnit.setObjectName("btnDelUnit")
        self.gridLayout_2.addWidget(self.btnDelUnit, 0, 2, 1, 1)
        self.btnEditUnit = QtWidgets.QPushButton(self.centralWidget)
        self.btnEditUnit.setObjectName("btnEditUnit")
        self.gridLayout_2.addWidget(self.btnEditUnit, 0, 3, 1, 1)
        self.tableWidgetUnit = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidgetUnit.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetUnit.setObjectName("tableWidgetUnit")
        self.tableWidgetUnit.setColumnCount(1)
        self.tableWidgetUnit.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetUnit.setHorizontalHeaderItem(0, item)
        self.tableWidgetUnit.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetUnit.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableWidgetUnit, 1, 0, 1, 4)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.chbEnableClose = QtWidgets.QCheckBox(self.centralWidget)
        self.chbEnableClose.setObjectName("chbEnableClose")
        self.horizontalLayout_2.addWidget(self.chbEnableClose)
        self.btnDo = QtWidgets.QPushButton(self.centralWidget)
        self.btnDo.setObjectName("btnDo")
        self.horizontalLayout_2.addWidget(self.btnDo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 806, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "工作启动管理"))
        self.btnAddSetting.setText(_translate("MainWindow", "+"))
        self.btnDelSetting.setText(_translate("MainWindow", "—"))
        self.btnEditSetting.setText(_translate("MainWindow", "/"))
        item = self.tableWidgetSetting.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "设置表"))
        self.btnAddUnit.setText(_translate("MainWindow", "+"))
        self.btnDelUnit.setText(_translate("MainWindow", "—"))
        self.btnEditUnit.setText(_translate("MainWindow", "/"))
        item = self.tableWidgetUnit.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "配置项"))
        self.chbEnableClose.setText(_translate("MainWindow", "完成后关闭"))
        self.btnDo.setText(_translate("MainWindow", "执行"))

