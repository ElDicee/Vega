# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileExplorerTree.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 800)
        Form.setStyleSheet(u"QWidget{\n"
"border-radius: 8px;\n"
"background-color: rgba(255, 255, 255, 130);\n"
"padding: 2px;\n"
"}\n"
"QWidget#Form{\n"
"background-color: rgb(56, 60, 72);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setStyleSheet(u"QWidget{\n"
"border-top: 2px solid rgb(19, 148, 207);\n"
"border-bottom: 2px solid rgb(19, 148, 207);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-top: none;\n"
"border-bottom: none;\n"
"border-right: 2px solid rgb(85, 170, 255);\n"
"border-left: 2px solid rgb(85, 170, 255);\n"
"background-color: rgba(233, 247, 255, 180);\n"
"padding: 0px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cancelBtn = QPushButton(self.widget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy1)
        self.cancelBtn.setMinimumSize(QSize(45, 35))

        self.horizontalLayout_2.addWidget(self.cancelBtn, 0, Qt.AlignLeft)

        self.desktopBtn = QPushButton(self.widget)
        self.desktopBtn.setObjectName(u"desktopBtn")
        self.desktopBtn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.desktopBtn)

        self.selectBtn = QPushButton(self.widget)
        self.selectBtn.setObjectName(u"selectBtn")
        sizePolicy1.setHeightForWidth(self.selectBtn.sizePolicy().hasHeightForWidth())
        self.selectBtn.setSizePolicy(sizePolicy1)
        self.selectBtn.setMinimumSize(QSize(45, 35))

        self.horizontalLayout_2.addWidget(self.selectBtn, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setStyleSheet(u"QWidget#widget_2{\n"
"background: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeView = QTreeView(self.widget_2)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"border: 2px solid rgb(19, 148, 207);")

        self.horizontalLayout.addWidget(self.treeView)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cancelBtn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.desktopBtn.setText(QCoreApplication.translate("Form", u"Move To Desktop", None))
        self.selectBtn.setText(QCoreApplication.translate("Form", u"Select", None))
    # retranslateUi

