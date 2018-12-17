# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proccess_model.ui'
#
# Created: Thu Nov 14 12:30:01 2013
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


class Ui_ProccessModel(object):
    def setupUi(self, ProccessModel):
        ProccessModel.setObjectName(_fromUtf8("ProccessModel"))
        ProccessModel.setWindowModality(Qt.NonModal)
        ProccessModel.resize(290, 320)
        ProccessModel.setMinimumSize(QSize(290, 320))
        ProccessModel.setMaximumSize(QSize(290, 320))
        self.gridLayoutWidget = QWidget(ProccessModel)
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 270, 158))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        # self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblVar2 = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblVar2.setFont(font)
        self.lblVar2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblVar2.setObjectName(_fromUtf8("lblVar2"))
        self.gridLayout.addWidget(self.lblVar2, 3, 0, 1, 1)
        self.cmbTFForm = QComboBox(self.gridLayoutWidget)
        self.cmbTFForm.setObjectName(_fromUtf8("cmbTFForm"))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbTFForm, 0, 1, 1, 1)
        self.lblTFForm = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTFForm.setFont(font)
        self.lblTFForm.setObjectName(_fromUtf8("lblTFForm"))
        self.gridLayout.addWidget(self.lblTFForm, 0, 0, 1, 1)
        self.leVar1 = QLineEdit(self.gridLayoutWidget)
        self.leVar1.setObjectName(_fromUtf8("leVar1"))
        self.gridLayout.addWidget(self.leVar1, 2, 1, 1, 1)
        self.leGain = QLineEdit(self.gridLayoutWidget)
        self.leGain.setObjectName(_fromUtf8("leGain"))
        self.gridLayout.addWidget(self.leGain, 1, 1, 1, 1)
        self.lblVar1 = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblVar1.setFont(font)
        self.lblVar1.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblVar1.setObjectName(_fromUtf8("lblVar1"))
        self.gridLayout.addWidget(self.lblVar1, 2, 0, 1, 1)
        self.lblGain = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblGain.setFont(font)
        self.lblGain.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblGain.setObjectName(_fromUtf8("lblGain"))
        self.gridLayout.addWidget(self.lblGain, 1, 0, 1, 1)
        self.leVar2 = QLineEdit(self.gridLayoutWidget)
        self.leVar2.setObjectName(_fromUtf8("leVar2"))
        self.gridLayout.addWidget(self.leVar2, 3, 1, 1, 1)
        self.lblDelay = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDelay.setFont(font)
        self.lblDelay.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblDelay.setObjectName(_fromUtf8("lblDelay"))
        self.gridLayout.addWidget(self.lblDelay, 4, 0, 1, 1)
        self.lblPadeOrder = QLabel(self.gridLayoutWidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPadeOrder.setFont(font)
        self.lblPadeOrder.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblPadeOrder.setObjectName(_fromUtf8("lblPadeOrder"))
        self.gridLayout.addWidget(self.lblPadeOrder, 5, 0, 1, 1)
        self.leDelay = QLineEdit(self.gridLayoutWidget)
        self.leDelay.setObjectName(_fromUtf8("leDelay"))
        self.gridLayout.addWidget(self.leDelay, 4, 1, 1, 1)
        self.sbPadeOrder = QSpinBox(self.gridLayoutWidget)
        self.sbPadeOrder.setMinimum(1)
        self.sbPadeOrder.setMaximum(10)
        self.sbPadeOrder.setProperty("value", 1)
        self.sbPadeOrder.setObjectName(_fromUtf8("sbPadeOrder"))
        self.gridLayout.addWidget(self.sbPadeOrder, 5, 1, 1, 1)
        self.verticalLayoutWidget = QWidget(ProccessModel)
        self.verticalLayoutWidget.setGeometry(QRect(10, 180, 271, 127))
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

        self.retranslateUi(ProccessModel)
        QMetaObject.connectSlotsByName(ProccessModel)

    def retranslateUi(self, ProccessModel):
        ProccessModel.setWindowTitle(QApplication.translate(
            "ProccessModel", "Proccess Model"))
        self.lblVar2.setText(QApplication.translate(
            "ProccessModel", "lblVar2"))
        self.cmbTFForm.setItemText(0, QApplication.translate(
            "ProccessModel", "Num / Den"))
        self.cmbTFForm.setItemText(1, QApplication.translate(
            "ProccessModel", "Zero / Poles"))
        self.cmbTFForm.setItemText(2, QApplication.translate(
            "ProccessModel", "Time Constants"))
        self.cmbTFForm.setItemText(3, QApplication.translate(
            "ProccessModel", "First Order with Delay"))
        self.lblTFForm.setText(QApplication.translate(
            "ProccessModel", "Transfer Function Form"))
        self.lblVar1.setText(QApplication.translate(
            "ProccessModel", "lblVar1"))
        self.lblGain.setText(QApplication.translate(
            "ProccessModel", "K"))
        self.lblDelay.setText(QApplication.translate(
            "ProccessModel", "Delay"))
        self.lblPadeOrder.setText(QApplication.translate(
            "ProccessModel", "Pade aprox. for delay"))
