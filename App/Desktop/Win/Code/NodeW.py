# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Node.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Node(object):
    def setupUi(self, Node):
        if not Node.objectName():
            Node.setObjectName(u"Node")
        Node.resize(313, 384)
        Node.setStyleSheet(u"QWidget#Node{\n"
"border-radius: 20px;\n"
"background-color: rgb(232, 236, 247);\n"
"	border-color: rgb(0, 170, 255);\n"
"border-width: 3px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Node)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlecont = QWidget(Node)
        self.titlecont.setObjectName(u"titlecont")
        self.titlecont.setMinimumSize(QSize(0, 30))
        self.titlecont.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.titlecont)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlecont2 = QWidget(self.titlecont)
        self.titlecont2.setObjectName(u"titlecont2")
        self.titlecont2.setStyleSheet(u"QWidget#titlecont2{\n"
"	background-color: rgb(216, 220, 230);\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.titlecont2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.titlecont2)
        self.title.setObjectName(u"title")
        font = QFont()
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title)


        self.horizontalLayout.addWidget(self.titlecont2)


        self.verticalLayout.addWidget(self.titlecont)

        self.exec_spacepin = QWidget(Node)
        self.exec_spacepin.setObjectName(u"exec_spacepin")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exec_spacepin.sizePolicy().hasHeightForWidth())
        self.exec_spacepin.setSizePolicy(sizePolicy)
        self.exec_spacepin.setMinimumSize(QSize(0, 40))
        self.exec_spacepin.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.exec_spacepin)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.exec_spacepin)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(self.exec_spacepin)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.exec_spacepin)

        self.customzone = QWidget(Node)
        self.customzone.setObjectName(u"customzone")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.customzone.sizePolicy().hasHeightForWidth())
        self.customzone.setSizePolicy(sizePolicy1)
        self.customzone.setMaximumSize(QSize(16777215, 0))

        self.verticalLayout.addWidget(self.customzone)

        self.signalpincontent = QWidget(Node)
        self.signalpincontent.setObjectName(u"signalpincontent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.signalpincontent.sizePolicy().hasHeightForWidth())
        self.signalpincontent.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.signalpincontent)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.widget_4 = QWidget(self.signalpincontent)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout_3.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.signalpincontent)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.signalpincontent)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_3.addWidget(self.widget_7)


        self.horizontalLayout_3.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.signalpincontent)


        self.retranslateUi(Node)

        QMetaObject.connectSlotsByName(Node)
    # setupUi

    def retranslateUi(self, Node):
        Node.setWindowTitle(QCoreApplication.translate("Node", u"Form", None))
        self.title.setText(QCoreApplication.translate("Node", u"Title", None))
        self.pushButton.setText(QCoreApplication.translate("Node", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Node", u"PushButton", None))
    # retranslateUi

