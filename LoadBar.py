# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
                               QVBoxLayout, QWidget, QDialog)


class LoadBar(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(740, 208)
        self.setStyleSheet(u"background-color: rgb(232, 236, 247);\n"
                           "border-radius: 20px;")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Super Mario 256"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(
            u"color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(0, 0, 0, 184), stop:1 rgba(255, 255, 255, 0));")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
                                       "                border: 2px solid grey;\n"
                                       "                border-radius: 8px;\n"
                                       "                background: rgba(56, 60, 72, 20);\n"
                                       "            }\n"
                                       "\n"
                                       "            QProgressBar::chunk {\n"
                                       "                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 "
                                       "rgb(0, 200, 255), stop:1 rgb(140, 0, 255));\n"
                                       "                border-radius: 6px;\n"
                                       "            }")
        self.progressBar.setValue(50)

        self.verticalLayout.addWidget(self.progressBar)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(9)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"The integrations are loading!", None))
        self.progressBar.setFormat("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Please, wait until the process is finished.", None))
    # retranslateUi
