# -------------------------------------------------------------------------------
# Name:        PIDTuneAboutWindow
# Purpose:
#
# Author:      ElBar
#
# Created:     17/04/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------
#!/usr/bin/env python

# from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_about import Ui_About

_VERSION = "0.3.4"
_URL = "<a href = ""http://sourceforge.net/projects/pypidtune"">Sourceforge Project Home Page</a>"

# -------------------------------------------------------------------------------


class PIDTuneAboutWindow(QDialog):
    """ Class wrapper for about window ui """

    def __init__(self):
        super(PIDTuneAboutWindow, self).__init__()
        self.setupUI()

    def setupUI(self):
        # create window from ui
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.ui.lblVersion.setText("pyPIDTune v{0}".format(_VERSION))
        self.ui.lblURL.setText(_URL)
# -------------------------------------------------------------------------------
