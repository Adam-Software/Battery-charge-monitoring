# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenXOZdTu.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(480, 680)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(0, 0, 480, 480))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(30, 30, 420, 420))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 210px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(30, 30, 420, 420))
        
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 210px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(50, 50, 380, 380))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 190px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 363, 291))

        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.widget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(78)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)

        self.labelLoadingInfo = QLabel(self.widget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 15))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(16)
        self.labelLoadingInfo.setFont(font2)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(93, 93, 154);\n"
"	color: #FFFFFF;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)

        self.labelCredits = QLabel(self.widget)
        self.labelCredits.setObjectName(u"labelCredits")
        self.labelCredits.setFont(font2)
        self.labelCredits.setStyleSheet(u"background-color: none;\n"
"color: rgb(155, 155, 255);")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#aaaaff;\">ADAM</span><span style=\" font-size:18pt;\"> BATTERY LEVEL</span></p></body></html>", None))
        self.labelPercentage.setText(QCoreApplication.translate("SplashScreen", u"<p><span style=\" font-size:72pt;\">0</span><span style=\" font-size:72pt; vertical-align:super;\">%</span></p>", None))
        self.labelLoadingInfo.setText(QCoreApplication.translate("SplashScreen", u"MAIN", None))
        self.labelCredits.setText(QCoreApplication.translate("SplashScreen", u"by: Robot LLC, 2023", None))
    # retranslateUi

