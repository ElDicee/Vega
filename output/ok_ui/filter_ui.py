# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import reso_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(341, 412)
        Form.setStyleSheet(u"QWidget{\n"
"background-color: rgba(232, 236, 247, 100);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 200))
        self.widget.setStyleSheet(u"background-color: rgba(232, 236, 247, 100);")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border-top-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-bottom: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(140, 0, 255), stop:1 rgb(0, 221, 255));\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    background-color: rgb(56, 60, 72);\n"
"    width: 12px;\n"
"    border: 0.5px solid rgb(56, 60, 72);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(56, 60, 72);\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(255, 0, 221), stop:1 rgb(255, 115, 0));\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    width: 0;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background-color: transparent;\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 319, 381))
        self.scrollAreaWidgetContents.setStyleSheet(u"QGroupBox{\n"
"	color: rgb(56, 60, 72);\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	background-color: rgba(239, 243, 254, 150);\n"
"	border-radius: 10px;\n"
"	box-shadow: 30px 30px 50px rgb(0, 0, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 3px 5px;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.5, y2:0, x3:1, y3:0, stop:0 rgb(255, 8, 169), stop:1 rgb(255, 68, 6), stop:2 rgb(255, 213, 1));\n"
"    font-size: 16px; \n"
"    font-weight: bold; \n"
"	border-radius: 3px;\n"
"	font-family: Microsoft-YaHei;\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"background-color: rgb(239, 243, 254);\n"
"border-radius: 8px;\n"
"}\n"
"QLabel:hover{\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(1, 204, 187, 255));\n"
"	border-width: 5px;\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 85, 255, 0"
                        "));\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 25, -1, -1)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Filter", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Title - ITG", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
    # retranslateUi

