# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 624)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PlotScrollArea = QScrollArea(self.groupBox)
        self.PlotScrollArea.setObjectName(u"PlotScrollArea")
        self.PlotScrollArea.setMaximumSize(QSize(16777215, 100))
        self.PlotScrollArea.setStyleSheet(u"border-radius: 10px;\n"
"\n"
"QPushButton{\n"
"border: 2px solid rgb(0, 170, 255);\n"
"}")
        self.PlotScrollArea.setFrameShape(QFrame.NoFrame)
        self.PlotScrollArea.setFrameShadow(QFrame.Plain)
        self.PlotScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PlotScrollArea.setWidgetResizable(True)
        self.PlotScrollAreaContent = QWidget()
        self.PlotScrollAreaContent.setObjectName(u"PlotScrollAreaContent")
        self.PlotScrollAreaContent.setGeometry(QRect(0, 0, 718, 77))
        self.horizontalLayout_3 = QHBoxLayout(self.PlotScrollAreaContent)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.PlotScrollAreaContent)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.PlotScrollArea.setWidget(self.PlotScrollAreaContent)

        self.horizontalLayout_2.addWidget(self.PlotScrollArea)


        self.verticalLayout.addWidget(self.groupBox)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(100, 0))
        self.groupBox_2.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.groupBox_2.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.VariableScrollArea = QScrollArea(self.groupBox_2)
        self.VariableScrollArea.setObjectName(u"VariableScrollArea")
        self.VariableScrollArea.setMaximumSize(QSize(9999, 16777215))
        self.VariableScrollArea.setFrameShape(QFrame.NoFrame)
        self.VariableScrollArea.setFrameShadow(QFrame.Plain)
        self.VariableScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.VariableScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 501))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.VariableScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.VariableScrollArea)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.PlotStackedWidget = QStackedWidget(self.widget)
        self.PlotStackedWidget.setObjectName(u"PlotStackedWidget")
        self.PlotStackedWidgetPage1 = QWidget()
        self.PlotStackedWidgetPage1.setObjectName(u"PlotStackedWidgetPage1")
        self.PlotStackedWidget.addWidget(self.PlotStackedWidgetPage1)

        self.horizontalLayout.addWidget(self.PlotStackedWidget)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Gr\u00e0fics", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Panell de Dades", None))
    # retranslateUi

