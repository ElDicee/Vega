# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slidemenu_button.ui'
##
## Created by: Qt ui Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)
import res_rc

class Ui_Button(object):
    def setupUi(self, Button):
        if not Button.objectName():
            Button.setObjectName(u"Button")
        Button.resize(240, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Button.sizePolicy().hasHeightForWidth())
        Button.setSizePolicy(sizePolicy)
        Button.setMinimumSize(QSize(240, 50))
        Button.setMaximumSize(QSize(240, 50))
        Button.setStyleSheet(u"QWidget{\n"
"background-color: rgb(56, 60, 72);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QWidget:hover{\n"
"	background-color: rgb(144, 155, 186);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Button)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.itgstatusindicator = QWidget(Button)
        self.itgstatusindicator.setObjectName(u"itgstatusindicator")
        sizePolicy.setHeightForWidth(self.itgstatusindicator.sizePolicy().hasHeightForWidth())
        self.itgstatusindicator.setSizePolicy(sizePolicy)
        self.itgstatusindicator.setMinimumSize(QSize(15, 15))
        self.itgstatusindicator.setMaximumSize(QSize(15, 15))
        self.itgstatusindicator.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(38, 225, 54);")

        self.horizontalLayout.addWidget(self.itgstatusindicator)

        self.label = QLabel(Button)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(Button)

        QMetaObject.connectSlotsByName(Button)
    # setupUi

    def retranslateUi(self, Button):
        Button.setWindowTitle(QCoreApplication.translate("Button", u"Form", None))
        self.label.setText(QCoreApplication.translate("Button", u"ITG NAME", None))
    # retranslateUi

