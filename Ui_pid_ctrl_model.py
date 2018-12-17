# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pid_ctrl_model.ui'
#
# Created: Tue Nov 19 09:33:43 2013
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


class Ui_PIDCtrlModel(object):
    def setupUi(self, PIDCtrlModel):
        PIDCtrlModel.setObjectName(_fromUtf8("PIDCtrlModel"))
        PIDCtrlModel.setWindowModality(Qt.NonModal)
        PIDCtrlModel.resize(290, 320)
        PIDCtrlModel.setMinimumSize(QSize(290, 320))
        PIDCtrlModel.setMaximumSize(QSize(290, 320))
        PIDCtrlModel.setModal(True)
        self.gridLayoutWidget = QWidget(PIDCtrlModel)
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 271, 152))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        # self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblPIDType = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPIDType.setFont(font)
        self.lblPIDType.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblPIDType.setObjectName(_fromUtf8("lblPIDType"))
        self.gridLayout.addWidget(self.lblPIDType, 0, 0, 1, 1)
        self.cmbPIDType = QComboBox(self.gridLayoutWidget)
        self.cmbPIDType.setObjectName(_fromUtf8("cmbPIDType"))
        self.cmbPIDType.addItem(_fromUtf8(""))
        self.cmbPIDType.addItem(_fromUtf8(""))
        self.cmbPIDType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbPIDType, 0, 1, 1, 1)
        self.lblKc = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblKc.setFont(font)
        self.lblKc.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblKc.setObjectName(_fromUtf8("lblKc"))
        self.gridLayout.addWidget(self.lblKc, 2, 0, 1, 1)
        self.leKc = QLineEdit(self.gridLayoutWidget)
        self.leKc.setObjectName(_fromUtf8("leKc"))
        self.gridLayout.addWidget(self.leKc, 2, 1, 1, 1)
        self.chbTi = QCheckBox(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chbTi.setFont(font)
        self.chbTi.setLayoutDirection(Qt.LeftToRight)
        self.chbTi.setObjectName(_fromUtf8("chbTi"))
        self.gridLayout.addWidget(self.chbTi, 3, 0, 1, 1)
        self.leTi = QLineEdit(self.gridLayoutWidget)
        self.leTi.setObjectName(_fromUtf8("leTi"))
        self.gridLayout.addWidget(self.leTi, 3, 1, 1, 1)
        self.chbTd = QCheckBox(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chbTd.setFont(font)
        self.chbTd.setObjectName(_fromUtf8("chbTd"))
        self.gridLayout.addWidget(self.chbTd, 4, 0, 1, 1)
        self.leTd = QLineEdit(self.gridLayoutWidget)
        self.leTd.setObjectName(_fromUtf8("leTd"))
        self.gridLayout.addWidget(self.leTd, 4, 1, 1, 1)
        spacerItem = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.lblTuneMethod = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTuneMethod.setFont(font)
        self.lblTuneMethod.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblTuneMethod.setObjectName(_fromUtf8("lblTuneMethod"))
        self.gridLayout.addWidget(self.lblTuneMethod, 1, 0, 1, 1)
        self.cmbTuneMethod = QComboBox(self.gridLayoutWidget)
        self.cmbTuneMethod.setObjectName(_fromUtf8("cmbTuneMethod"))
        self.gridLayout.addWidget(self.cmbTuneMethod, 1, 1, 1, 1)
        self.cmbPIDConfig = QComboBox(self.gridLayoutWidget)
        self.cmbPIDConfig.setObjectName(_fromUtf8("cmbPIDConfig"))
        self.gridLayout.addWidget(self.cmbPIDConfig, 1, 2, 1, 1)
        self.lblTf = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTf.setFont(font)
        self.lblTf.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblTf.setObjectName(_fromUtf8("lblTf"))
        self.gridLayout.addWidget(self.lblTf, 5, 0, 1, 1)
        self.leTf = QLineEdit(self.gridLayoutWidget)
        self.leTf.setObjectName(_fromUtf8("leTf"))
        self.gridLayout.addWidget(self.leTf, 5, 1, 1, 1)
        self.verticalLayoutWidget = QWidget(PIDCtrlModel)
        self.verticalLayoutWidget.setGeometry(QRect(10, 180, 271, 128))
        self.verticalLayoutWidget.setObjectName(
            _fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        # self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblTF = QLabel(self.verticalLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTF.setFont(font)
        self.lblTF.setFrameShape(QFrame.Box)
        self.lblTF.setFrameShadow(QFrame.Sunken)
        self.lblTF.setText(_fromUtf8(""))
        self.lblTF.setAlignment(Qt.AlignCenter)
        self.lblTF.setObjectName(_fromUtf8("lblTF"))
        self.verticalLayout.addWidget(self.lblTF)
        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Apply | QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PIDCtrlModel)
        self.cmbPIDType.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(PIDCtrlModel)

    def retranslateUi(self, PIDCtrlModel):
        PIDCtrlModel.setWindowTitle(QApplication.translate(
            "PIDCtrlModel", "PID Model"))
        self.lblPIDType.setText(QApplication.translate(
            "PIDCtrlModel", "PID Type"))
        self.cmbPIDType.setItemText(0, QApplication.translate(
            "PIDCtrlModel", "Standard PID"))
        self.cmbPIDType.setItemText(1, QApplication.translate(
            "PIDCtrlModel", "Parallel PID"))
        self.cmbPIDType.setItemText(2, QApplication.translate(
            "PIDCtrlModel", "Predefined PIDs"))
        self.lblKc.setText(QApplication.translate(
            "PIDCtrlModel", "Kc"))
        self.chbTi.setText(QApplication.translate(
            "PIDCtrlModel", "Ti"))
        self.chbTd.setText(QApplication.translate(
            "PIDCtrlModel", "Td"))
        self.lblTuneMethod.setText(QApplication.translate(
            "PIDCtrlModel", "Tune Method"))
        self.lblTf.setText(QApplication.translate(
            "PIDCtrlModel", "Tf"))
