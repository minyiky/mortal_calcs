# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bow_calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(440, 20, 821, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 381, 161))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 19, 371, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridMaterials = QtWidgets.QGridLayout()
        self.gridMaterials.setObjectName("gridMaterials")
        self.boneTissue = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.boneTissue.setObjectName("boneTissue")
        self.gridMaterials.addWidget(self.boneTissue, 2, 1, 1, 1)
        self.greyWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.greyWood.setObjectName("greyWood")
        self.gridMaterials.addWidget(self.greyWood, 4, 0, 1, 1)
        self.firmWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.firmWood.setObjectName("firmWood")
        self.gridMaterials.addWidget(self.firmWood, 3, 2, 1, 1)
        self.whiteWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.whiteWood.setObjectName("whiteWood")
        self.gridMaterials.addWidget(self.whiteWood, 3, 1, 1, 1)
        self.compactHorn = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.compactHorn.setObjectName("compactHorn")
        self.gridMaterials.addWidget(self.compactHorn, 1, 1, 1, 1)
        self.dappleWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.dappleWood.setObjectName("dappleWood")
        self.gridMaterials.addWidget(self.dappleWood, 4, 1, 1, 1)
        self.spongeWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.spongeWood.setObjectName("spongeWood")
        self.gridMaterials.addWidget(self.spongeWood, 3, 0, 1, 1)
        self.ironWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ironWood.setObjectName("ironWood")
        self.gridMaterials.addWidget(self.ironWood, 5, 1, 1, 1)
        self.brownWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.brownWood.setObjectName("brownWood")
        self.gridMaterials.addWidget(self.brownWood, 4, 2, 1, 1)
        self.horn = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.horn.setObjectName("horn")
        self.gridMaterials.addWidget(self.horn, 1, 2, 1, 1)
        self.blackWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.blackWood.setObjectName("blackWood")
        self.gridMaterials.addWidget(self.blackWood, 5, 0, 1, 1)
        self.ironBone = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ironBone.setObjectName("ironBone")
        self.gridMaterials.addWidget(self.ironBone, 2, 0, 1, 1)
        self.greatHorn = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.greatHorn.setObjectName("greatHorn")
        self.gridMaterials.addWidget(self.greatHorn, 1, 0, 1, 1)
        self.crepite = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.crepite.setObjectName("crepite")
        self.gridMaterials.addWidget(self.crepite, 0, 1, 1, 1)
        self.molarium = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.molarium.setObjectName("molarium")
        self.gridMaterials.addWidget(self.molarium, 0, 2, 1, 1)
        self.denseCrepite = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.denseCrepite.setObjectName("denseCrepite")
        self.gridMaterials.addWidget(self.denseCrepite, 0, 0, 1, 1)
        self.stoneWood = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.stoneWood.setObjectName("stoneWood")
        self.gridMaterials.addWidget(self.stoneWood, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridMaterials)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 190, 381, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 19, 371, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridTypes = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridTypes.setContentsMargins(0, 0, 0, 0)
        self.gridTypes.setObjectName("gridTypes")
        self.long_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.long_2.setObjectName("long_2")
        self.gridTypes.addWidget(self.long_2, 0, 1, 1, 1)
        self.short_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.short_2.setObjectName("short_2")
        self.gridTypes.addWidget(self.short_2, 0, 0, 1, 1)
        self.asym_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.asym_2.setObjectName("asym_2")
        self.gridTypes.addWidget(self.asym_2, 0, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 260, 381, 51))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 371, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridMechanics = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridMechanics.setContentsMargins(0, 0, 0, 0)
        self.gridMechanics.setObjectName("gridMechanics")
        self.recurve = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.recurve.setObjectName("recurve")
        self.gridMechanics.addWidget(self.recurve, 0, 0, 1, 1)
        self.flat = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.flat.setObjectName("flat")
        self.gridMechanics.addWidget(self.flat, 0, 1, 1, 1)
        self.decurve = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.decurve.setObjectName("decurve")
        self.gridMechanics.addWidget(self.decurve, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 350, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 350, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 350, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.spinStrength = QtWidgets.QSpinBox(self.centralwidget)
        self.spinStrength.setGeometry(QtCore.QRect(300, 320, 91, 22))
        self.spinStrength.setMinimum(10)
        self.spinStrength.setMaximum(123)
        self.spinStrength.setProperty("value", 100)
        self.spinStrength.setObjectName("spinStrength")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 320, 101, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
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
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bow Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Bow Mechanic"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Left Material"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Right Material"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Percentage"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Strength"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Range"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Durability"))
        self.groupBox.setTitle(_translate("MainWindow", "Available Materials"))
        self.boneTissue.setText(_translate("MainWindow", "Bone Tissue"))
        self.greyWood.setText(_translate("MainWindow", "Greywood"))
        self.firmWood.setText(_translate("MainWindow", "Firmwood"))
        self.whiteWood.setText(_translate("MainWindow", "Whitewood"))
        self.compactHorn.setText(_translate("MainWindow", "Compact Horn"))
        self.dappleWood.setText(_translate("MainWindow", "Dapplewood"))
        self.spongeWood.setText(_translate("MainWindow", "Spongewood"))
        self.ironWood.setText(_translate("MainWindow", "Ironwood"))
        self.brownWood.setText(_translate("MainWindow", "Brownwood"))
        self.horn.setText(_translate("MainWindow", "Horn"))
        self.blackWood.setText(_translate("MainWindow", "Blackwood"))
        self.ironBone.setText(_translate("MainWindow", "Iron Bone"))
        self.greatHorn.setText(_translate("MainWindow", "Great Horn"))
        self.crepite.setText(_translate("MainWindow", "Crepite"))
        self.molarium.setText(_translate("MainWindow", "Molarium"))
        self.denseCrepite.setText(_translate("MainWindow", "Dense Crepite"))
        self.stoneWood.setText(_translate("MainWindow", "Stonewood"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Bow Types"))
        self.long_2.setText(_translate("MainWindow", "Long Bow"))
        self.short_2.setText(_translate("MainWindow", "Short Bow"))
        self.asym_2.setText(_translate("MainWindow", "Asymetric Bow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Bow Mechanics"))
        self.recurve.setText(_translate("MainWindow", "Recurve Bow"))
        self.flat.setText(_translate("MainWindow", "Flat Bow"))
        self.decurve.setText(_translate("MainWindow", "Decurve Bow"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "Update Data"))
        self.label.setText(_translate("MainWindow", "Character Strength"))
