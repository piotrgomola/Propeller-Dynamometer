# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Zrzuty/PP_logo_jasne.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(150, 180))
        self.tabWidget.setMaximumSize(QtCore.QSize(150, 180))
        self.tabWidget.setObjectName("tabWidget")
        self.uart = QtWidgets.QWidget()
        self.uart.setObjectName("uart")
        self.label_2 = QtWidgets.QLabel(self.uart)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.label_2.setObjectName("label_2")
        self.uartPortList = QtWidgets.QComboBox(self.uart)
        self.uartPortList.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.uartPortList.setObjectName("uartPortList")
        self.label_3 = QtWidgets.QLabel(self.uart)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_3.setObjectName("label_3")
        self.uartBaudRateList = QtWidgets.QComboBox(self.uart)
        self.uartBaudRateList.setGeometry(QtCore.QRect(10, 110, 111, 22))
        self.uartBaudRateList.setObjectName("uartBaudRateList")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.uartBaudRateList.addItem("")
        self.tabWidget.addTab(self.uart, "")
        self.usb_hid = QtWidgets.QWidget()
        self.usb_hid.setObjectName("usb_hid")
        self.label_4 = QtWidgets.QLabel(self.usb_hid)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.vendorID = QtWidgets.QLineEdit(self.usb_hid)
        self.vendorID.setGeometry(QtCore.QRect(10, 30, 113, 22))
        self.vendorID.setObjectName("vendorID")
        self.label_5 = QtWidgets.QLabel(self.usb_hid)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_5.setObjectName("label_5")
        self.productID = QtWidgets.QLineEdit(self.usb_hid)
        self.productID.setGeometry(QtCore.QRect(10, 110, 113, 22))
        self.productID.setObjectName("productID")
        self.tabWidget.addTab(self.usb_hid, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.connectButton.setObjectName("connectButton")
        self.verticalLayout_3.addWidget(self.connectButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(40, 20, 151, 16))
        self.label_14.setObjectName("label_14")
        self.speedMeterN1 = QtWidgets.QLabel(self.groupBox_4)
        self.speedMeterN1.setGeometry(QtCore.QRect(40, 40, 55, 16))
        self.speedMeterN1.setObjectName("speedMeterN1")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(490, 20, 81, 16))
        self.label_15.setObjectName("label_15")
        self.voltageMeter = QtWidgets.QLabel(self.groupBox_4)
        self.voltageMeter.setGeometry(QtCore.QRect(490, 40, 55, 16))
        self.voltageMeter.setObjectName("voltageMeter")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(340, 20, 71, 16))
        self.label_16.setObjectName("label_16")
        self.currentMeterI1 = QtWidgets.QLabel(self.groupBox_4)
        self.currentMeterI1.setGeometry(QtCore.QRect(340, 40, 55, 16))
        self.currentMeterI1.setObjectName("currentMeterI1")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(570, 20, 71, 16))
        self.label_17.setObjectName("label_17")
        self.pressureMeter = QtWidgets.QLabel(self.groupBox_4)
        self.pressureMeter.setGeometry(QtCore.QRect(570, 40, 55, 16))
        self.pressureMeter.setObjectName("pressureMeter")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(410, 20, 71, 16))
        self.label_18.setObjectName("label_18")
        self.currentMeterI2 = QtWidgets.QLabel(self.groupBox_4)
        self.currentMeterI2.setGeometry(QtCore.QRect(410, 40, 55, 16))
        self.currentMeterI2.setObjectName("currentMeterI2")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(190, 20, 151, 16))
        self.label_19.setObjectName("label_19")
        self.speedMeterN2 = QtWidgets.QLabel(self.groupBox_4)
        self.speedMeterN2.setGeometry(QtCore.QRect(190, 40, 55, 16))
        self.speedMeterN2.setObjectName("speedMeterN2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(0, 20, 55, 16))
        self.label_20.setObjectName("label_20")
        self.PWMMeter = QtWidgets.QLabel(self.groupBox_4)
        self.PWMMeter.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.PWMMeter.setObjectName("PWMMeter")
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 141, 16))
        self.label_6.setObjectName("label_6")
        self.calibrateTens = QtWidgets.QPushButton(self.groupBox_2)
        self.calibrateTens.setGeometry(QtCore.QRect(10, 120, 93, 28))
        self.calibrateTens.setObjectName("calibrateTens")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_13.setObjectName("label_13")
        self.poleNumber = QtWidgets.QSpinBox(self.groupBox_2)
        self.poleNumber.setGeometry(QtCore.QRect(10, 50, 81, 22))
        self.poleNumber.setMaximum(127)
        self.poleNumber.setObjectName("poleNumber")
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(100, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.label_11.setObjectName("label_11")
        self.minPWM = QtWidgets.QSpinBox(self.groupBox_3)
        self.minPWM.setGeometry(QtCore.QRect(40, 50, 51, 22))
        self.minPWM.setMaximum(100)
        self.minPWM.setObjectName("minPWM")
        self.maxPWM = QtWidgets.QSpinBox(self.groupBox_3)
        self.maxPWM.setGeometry(QtCore.QRect(120, 50, 51, 22))
        self.maxPWM.setMaximum(100)
        self.maxPWM.setObjectName("maxPWM")
        self.jumpPWM = QtWidgets.QSpinBox(self.groupBox_3)
        self.jumpPWM.setGeometry(QtCore.QRect(10, 100, 51, 22))
        self.jumpPWM.setMaximum(100)
        self.jumpPWM.setObjectName("jumpPWM")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 130, 291, 16))
        self.label_12.setObjectName("label_12")
        self.pwmTime = QtWidgets.QSpinBox(self.groupBox_3)
        self.pwmTime.setGeometry(QtCore.QRect(10, 150, 51, 22))
        self.pwmTime.setMaximum(127)
        self.pwmTime.setObjectName("pwmTime")
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.saveToFile = QtWidgets.QCheckBox(self.centralwidget)
        self.saveToFile.setChecked(True)
        self.saveToFile.setObjectName("saveToFile")
        self.verticalLayout_4.addWidget(self.saveToFile)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(150, 180))
        self.groupBox.setMaximumSize(QtCore.QSize(150, 180))
        self.groupBox.setObjectName("groupBox")
        self.saveSpeed = QtWidgets.QCheckBox(self.groupBox)
        self.saveSpeed.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.saveSpeed.setChecked(True)
        self.saveSpeed.setObjectName("saveSpeed")
        self.saveVoltage = QtWidgets.QCheckBox(self.groupBox)
        self.saveVoltage.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.saveVoltage.setChecked(True)
        self.saveVoltage.setObjectName("saveVoltage")
        self.saveCurrent = QtWidgets.QCheckBox(self.groupBox)
        self.saveCurrent.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.saveCurrent.setChecked(True)
        self.saveCurrent.setObjectName("saveCurrent")
        self.savePressure = QtWidgets.QCheckBox(self.groupBox)
        self.savePressure.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.savePressure.setChecked(True)
        self.savePressure.setObjectName("savePressure")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_8.setObjectName("label_8")
        self.fileName = QtWidgets.QLineEdit(self.groupBox)
        self.fileName.setGeometry(QtCore.QRect(10, 130, 131, 22))
        self.fileName.setObjectName("fileName")
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QtCore.QSize(150, 50))
        self.stopButton.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_3.addWidget(self.stopButton)
        self.startTest = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTest.sizePolicy().hasHeightForWidth())
        self.startTest.setSizePolicy(sizePolicy)
        self.startTest.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.startTest.setFont(font)
        self.startTest.setObjectName("startTest")
        self.horizontalLayout_3.addWidget(self.startTest)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        self.menuPomoc = QtWidgets.QMenu(self.menubar)
        self.menuPomoc.setObjectName("menuPomoc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Terminal = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Terminal.sizePolicy().hasHeightForWidth())
        self.Terminal.setSizePolicy(sizePolicy)
        self.Terminal.setMinimumSize(QtCore.QSize(109, 200))
        self.Terminal.setMaximumSize(QtCore.QSize(1000, 350))
        self.Terminal.setObjectName("Terminal")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.terminal = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal.sizePolicy().hasHeightForWidth())
        self.terminal.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.terminal.setPalette(palette)
        self.terminal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.terminal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.terminal.setReadOnly(True)
        self.terminal.setObjectName("terminal")
        self.verticalLayout.addWidget(self.terminal)
        self.Terminal.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.Terminal)
        self.actionZamknij = QtWidgets.QAction(MainWindow)
        self.actionZamknij.setObjectName("actionZamknij")
        self.actionAutorzy = QtWidgets.QAction(MainWindow)
        self.actionAutorzy.setObjectName("actionAutorzy")
        self.actionPomoc = QtWidgets.QAction(MainWindow)
        self.actionPomoc.setObjectName("actionPomoc")
        self.menuPlik.addAction(self.actionZamknij)
        self.menuPomoc.addAction(self.actionPomoc)
        self.menuPomoc.addAction(self.actionAutorzy)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.uartBaudRateList.setCurrentIndex(11)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DynoSoft"))
        self.label.setText(_translate("MainWindow", "Wybrany sposób komunikacji:"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "BaudRate:"))
        self.uartBaudRateList.setCurrentText(_translate("MainWindow", "115200"))
        self.uartBaudRateList.setItemText(0, _translate("MainWindow", "600"))
        self.uartBaudRateList.setItemText(1, _translate("MainWindow", "1200"))
        self.uartBaudRateList.setItemText(2, _translate("MainWindow", "2400"))
        self.uartBaudRateList.setItemText(3, _translate("MainWindow", "4800"))
        self.uartBaudRateList.setItemText(4, _translate("MainWindow", "9600"))
        self.uartBaudRateList.setItemText(5, _translate("MainWindow", "14400"))
        self.uartBaudRateList.setItemText(6, _translate("MainWindow", "19200"))
        self.uartBaudRateList.setItemText(7, _translate("MainWindow", "28800"))
        self.uartBaudRateList.setItemText(8, _translate("MainWindow", "38400"))
        self.uartBaudRateList.setItemText(9, _translate("MainWindow", "56000"))
        self.uartBaudRateList.setItemText(10, _translate("MainWindow", "57600"))
        self.uartBaudRateList.setItemText(11, _translate("MainWindow", "115200"))
        self.uartBaudRateList.setItemText(12, _translate("MainWindow", "128000"))
        self.uartBaudRateList.setItemText(13, _translate("MainWindow", "256000"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uart), _translate("MainWindow", "UART"))
        self.label_4.setText(_translate("MainWindow", "VendroID:"))
        self.label_5.setText(_translate("MainWindow", "ProductID:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usb_hid), _translate("MainWindow", "USB HID"))
        self.connectButton.setText(_translate("MainWindow", "Połącz"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Wskazania:"))
        self.label_14.setText(_translate("MainWindow", "Pręd.obrot. n1[obr/min]:"))
        self.speedMeterN1.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "Napięcie [V]:"))
        self.voltageMeter.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Prąd I1 [A]:"))
        self.currentMeterI1.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Nacisk [g]:"))
        self.pressureMeter.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Prąd I2 [A]:"))
        self.currentMeterI2.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Pręd.obrot. n2[obr/min]:"))
        self.speedMeterN2.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "PWM:"))
        self.PWMMeter.setText(_translate("MainWindow", "0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parametry hamowni:"))
        self.label_6.setText(_translate("MainWindow", "Liczba par biegunów:"))
        self.calibrateTens.setText(_translate("MainWindow", "Kalibracja"))
        self.label_13.setText(_translate("MainWindow", "Tensometr:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Ustawienia testów:"))
        self.label_7.setText(_translate("MainWindow", "Zakres wypełnienia [%]:"))
        self.label_9.setText(_translate("MainWindow", "Od"))
        self.label_10.setText(_translate("MainWindow", "do"))
        self.label_11.setText(_translate("MainWindow", "Skok wypełnienia[%]:"))
        self.label_12.setText(_translate("MainWindow", "Okres poszczególnego skoku wypełnienia [s]:"))
        self.saveToFile.setText(_translate("MainWindow", "Zapisuj do pliku"))
        self.groupBox.setTitle(_translate("MainWindow", "Opcje zapisu"))
        self.saveSpeed.setText(_translate("MainWindow", "Prędkość obrotowa"))
        self.saveVoltage.setText(_translate("MainWindow", "Napięcie"))
        self.saveCurrent.setText(_translate("MainWindow", "Prąd"))
        self.savePressure.setText(_translate("MainWindow", "Nacisk"))
        self.label_8.setText(_translate("MainWindow", "Nazwa pliku:"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))
        self.startTest.setText(_translate("MainWindow", "Start"))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik"))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc"))
        self.Terminal.setWindowTitle(_translate("MainWindow", "Terminal"))
        self.actionZamknij.setText(_translate("MainWindow", "Zamknij"))
        self.actionAutorzy.setText(_translate("MainWindow", "Autorzy"))
        self.actionPomoc.setText(_translate("MainWindow", "Pomoc"))