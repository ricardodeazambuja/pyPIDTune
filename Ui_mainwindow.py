# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Nov 13 15:46:11 2013
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# try:
#     _fromUtf8 = QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s): return s


def _fromUtf8(s): return s


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 320)
        MainWindow.setMinimumSize(QSize(500, 320))
        MainWindow.setMaximumSize(QSize(700, 320))
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8(":/img/Bus.png")),
                       QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayoutSettings = QGridLayout()
        self.gridLayoutSettings.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayoutSettings.setObjectName(_fromUtf8("gridLayoutSettings"))
        self.lblPIDModel = QLabel(self.centralWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblPIDModel.sizePolicy().hasHeightForWidth())
        self.lblPIDModel.setSizePolicy(sizePolicy)
        self.lblPIDModel.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPIDModel.setFont(font)
        self.lblPIDModel.setFrameShape(QFrame.Box)
        self.lblPIDModel.setFrameShadow(QFrame.Sunken)
        self.lblPIDModel.setAlignment(Qt.AlignCenter)
        self.lblPIDModel.setObjectName(_fromUtf8("lblPIDModel"))
        self.gridLayoutSettings.addWidget(self.lblPIDModel, 1, 0, 1, 1)
        self.lblProccess = QLabel(self.centralWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblProccess.sizePolicy().hasHeightForWidth())
        self.lblProccess.setSizePolicy(sizePolicy)
        self.lblProccess.setMinimumSize(QSize(0, 90))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProccess.setFont(font)
        self.lblProccess.setFrameShape(QFrame.Box)
        self.lblProccess.setFrameShadow(QFrame.Sunken)
        self.lblProccess.setAlignment(Qt.AlignCenter)
        self.lblProccess.setObjectName(_fromUtf8("lblProccess"))
        self.gridLayoutSettings.addWidget(self.lblProccess, 0, 2, 1, 1)
        self.lblPID = QLabel(self.centralWidget)
        self.lblPID.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPID.setFont(font)
        self.lblPID.setFrameShape(QFrame.Box)
        self.lblPID.setFrameShadow(QFrame.Sunken)
        self.lblPID.setAlignment(Qt.AlignCenter)
        self.lblPID.setObjectName(_fromUtf8("lblPID"))
        self.gridLayoutSettings.addWidget(self.lblPID, 1, 2, 1, 1)
        self.lblProccessModel = QLabel(self.centralWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblProccessModel.sizePolicy().hasHeightForWidth())
        self.lblProccessModel.setSizePolicy(sizePolicy)
        self.lblProccessModel.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProccessModel.setFont(font)
        self.lblProccessModel.setFrameShape(QFrame.Box)
        self.lblProccessModel.setFrameShadow(QFrame.Sunken)
        self.lblProccessModel.setAlignment(Qt.AlignCenter)
        self.lblProccessModel.setObjectName(_fromUtf8("lblProccessModel"))
        self.gridLayoutSettings.addWidget(self.lblProccessModel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayoutSettings)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setGeometry(QRect(0, 0, 500, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuModels = QMenu(self.menuBar)
        self.menuModels.setObjectName(_fromUtf8("menuModels"))
        self.menuPID = QMenu(self.menuBar)
        self.menuPID.setObjectName(_fromUtf8("menuPID"))
        self.menuClosed_Loop = QMenu(self.menuBar)
        self.menuClosed_Loop.setObjectName(_fromUtf8("menuClosed_Loop"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QAction(MainWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8(":/img/close16.png")),
                        QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QAction(MainWindow)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(_fromUtf8(":/img/info16.png")),
                        QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(_fromUtf8(":/img/options-16.png")),
                        QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon3)
        self.actionSettings.setIconVisibleInMenu(True)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionProccessTF = QAction(MainWindow)
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(_fromUtf8(":/img/text_superscript-16.png")), QIcon.Normal, QIcon.On)
        self.actionProccessTF.setIcon(icon4)
        self.actionProccessTF.setObjectName(_fromUtf8("actionProccessTF"))
        self.actionPID_Controller = QAction(MainWindow)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(_fromUtf8(":/img/gcp-16.png")),
                        QIcon.Normal, QIcon.On)
        self.actionPID_Controller.setIcon(icon5)
        self.actionPID_Controller.setObjectName(
            _fromUtf8("actionPID_Controller"))
        self.actionReset_Models = QAction(MainWindow)
        icon6 = QIcon()
        icon6.addPixmap(
            QPixmap(_fromUtf8(":/img/refresh-16.png")), QIcon.Normal, QIcon.On)
        self.actionReset_Models.setIcon(icon6)
        self.actionReset_Models.setObjectName(_fromUtf8("actionReset_Models"))
        self.actionTime_Domain_Graph = QAction(MainWindow)
        icon7 = QIcon()
        icon7.addPixmap(
            QPixmap(_fromUtf8(":/img/chart_curve-16.png")), QIcon.Normal, QIcon.Off)
        self.actionTime_Domain_Graph.setIcon(icon7)
        self.actionTime_Domain_Graph.setObjectName(
            _fromUtf8("actionTime_Domain_Graph"))
        self.actionFreq_Domain_Graph = QAction(MainWindow)
        icon8 = QIcon()
        icon8.addPixmap(
            QPixmap(_fromUtf8(":/img/linechart-16.png")), QIcon.Normal, QIcon.Off)
        self.actionFreq_Domain_Graph.setIcon(icon8)
        self.actionFreq_Domain_Graph.setObjectName(
            _fromUtf8("actionFreq_Domain_Graph"))
        self.actionCLTime_Domain_Graph = QAction(MainWindow)
        icon9 = QIcon()
        icon9.addPixmap(
            QPixmap(_fromUtf8(":/img/diagramm-16.png")), QIcon.Normal, QIcon.Off)
        self.actionCLTime_Domain_Graph.setIcon(icon9)
        self.actionCLTime_Domain_Graph.setObjectName(
            _fromUtf8("actionCLTime_Domain_Graph"))
        self.actionCLFreq_Domain_Graph = QAction(MainWindow)
        icon10 = QIcon()
        icon10.addPixmap(
            QPixmap(_fromUtf8(":/img/vector-16.png")), QIcon.Normal, QIcon.Off)
        self.actionCLFreq_Domain_Graph.setIcon(icon10)
        self.actionCLFreq_Domain_Graph.setObjectName(
            _fromUtf8("actionCLFreq_Domain_Graph"))
        self.actionCLNyquist_Graph = QAction(MainWindow)
        icon11 = QIcon()
        icon11.addPixmap(
            QPixmap(_fromUtf8(":/img/centroid-16.png")), QIcon.Normal, QIcon.Off)
        self.actionCLNyquist_Graph.setIcon(icon11)
        self.actionCLNyquist_Graph.setObjectName(
            _fromUtf8("actionCLNyquist_Graph"))
        self.menuFile.addAction(self.actionReset_Models)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuModels.addAction(self.actionProccessTF)
        self.menuModels.addSeparator()
        self.menuModels.addAction(self.actionTime_Domain_Graph)
        self.menuModels.addAction(self.actionFreq_Domain_Graph)
        self.menuPID.addAction(self.actionPID_Controller)
        self.menuPID.addSeparator()
        self.menuClosed_Loop.addAction(self.actionCLTime_Domain_Graph)
        self.menuClosed_Loop.addAction(self.actionCLFreq_Domain_Graph)
        self.menuClosed_Loop.addAction(self.actionCLNyquist_Graph)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuModels.menuAction())
        self.menuBar.addAction(self.menuPID.menuAction())
        self.menuBar.addAction(self.menuClosed_Loop.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        # QObject.connect(self.actionExit, SIGNAL(
        #     _fromUtf8("triggered()")), MainWindow.close)

        getattr(self.actionExit, "triggered").connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate(
            "MainWindow", "PID Tune"))
        self.lblPIDModel.setText(QApplication.translate(
            "MainWindow", "PID"))
        self.lblProccess.setText(QApplication.translate("MainWindow", "None\n"
                                                        "Delay : 0.0s, Pade : 1"))
        self.lblPID.setText(QApplication.translate(
            "MainWindow", "None"))
        self.lblProccessModel.setText(QApplication.translate(
            "MainWindow", "Proccess"))
        self.menuFile.setTitle(QApplication.translate(
            "MainWindow", "File"))
        self.menuHelp.setTitle(QApplication.translate(
            "MainWindow", "Help"))
        self.menuModels.setTitle(QApplication.translate(
            "MainWindow", "Proccess"))
        self.menuPID.setTitle(QApplication.translate(
            "MainWindow", "PID"))
        self.menuClosed_Loop.setTitle(QApplication.translate(
            "MainWindow", "Closed Loop"))
        self.actionExit.setText(QApplication.translate(
            "MainWindow", "Exit"))
        self.actionAbout.setText(QApplication.translate(
            "MainWindow", "About..."))
        self.actionSettings.setText(QApplication.translate(
            "MainWindow", "Settings..."))
        self.actionProccessTF.setText(QApplication.translate(
            "MainWindow", "Transfer Function"))
        self.actionProccessTF.setIconText(QApplication.translate(
            "MainWindow", "Transfer Function"))
        self.actionProccessTF.setToolTip(QApplication.translate(
            "MainWindow", "Proccess Transfer Function"))
        self.actionPID_Controller.setText(QApplication.translate(
            "MainWindow", "PID Controller"))
        self.actionReset_Models.setText(QApplication.translate(
            "MainWindow", "Reset Models"))
        self.actionTime_Domain_Graph.setText(QApplication.translate(
            "MainWindow", "Time Domain Graphs"))
        self.actionTime_Domain_Graph.setToolTip(QApplication.translate(
            "MainWindow", "Proccess Time Domain Graphs"))
        self.actionFreq_Domain_Graph.setText(QApplication.translate(
            "MainWindow", "Freq Domain Graphs"))
        self.actionFreq_Domain_Graph.setToolTip(QApplication.translate(
            "MainWindow", "Proccess Freq Domain Graphs"))
        self.actionCLTime_Domain_Graph.setText(QApplication.translate(
            "MainWindow", "Time Domain Graphs"))
        self.actionCLTime_Domain_Graph.setToolTip(QApplication.translate(
            "MainWindow", "Closed Loop Time Domain Graphs"))
        self.actionCLFreq_Domain_Graph.setText(QApplication.translate(
            "MainWindow", "Freq Domain Graph"))
        self.actionCLFreq_Domain_Graph.setToolTip(QApplication.translate(
            "MainWindow", "Closed Loop Freq Domain Graph"))
        self.actionCLNyquist_Graph.setText(QApplication.translate(
            "MainWindow", "Nyquist Graph"))


import pyPIDTune_rc
