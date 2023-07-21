# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QEnterEvent)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QWidget)

from enum import Enum


class PinType(Enum):
    INPUT_PIN = "in"
    OUTPUT_PIN = "out"
    EXEC_FLOW_PIN = "exec"


class Pin(QWidget):

    def __init__(self, type: PinType = PinType.INPUT_PIN, valuename: str = "Value", **kwargs):
        super(Pin, self).__init__(**kwargs)
        self.valuename = valuename
        self.type = type
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(400, 30)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 30))
        self.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.contactPin = QPushButton(self)
        self.contactPin.setObjectName(u"contactPin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contactPin.sizePolicy().hasHeightForWidth())
        self.contactPin.setSizePolicy(sizePolicy1)
        self.contactPin.setMinimumSize(QSize(20, 20))
        self.contactPin.setMaximumSize(QSize(20, 20))
        self.contactPin.setStyleSheet(u"QPushButton{\n"
                                      "	background-color: rgb(56, 60, 72);\n"
                                      "	border-radius: 8px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "	background-color: rgb(0, 170, 255);\n"
                                      "	border-radius: 10px;\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u"./res/icons/Feather_white/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.contactPin.setIcon(icon)

        if not self.type == PinType.EXEC_FLOW_PIN:
            self.pinlabel = QLabel(self)
            self.pinlabel.setObjectName(u"pinlabel")
            sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            sizePolicy2.setHorizontalStretch(0)
            sizePolicy2.setVerticalStretch(0)
            sizePolicy2.setHeightForWidth(self.pinlabel.sizePolicy().hasHeightForWidth())
            self.pinlabel.setSizePolicy(sizePolicy2)
            font = QFont()
            font.setPointSize(10)
            font.setBold(True)
            self.pinlabel.setFont(font)
            self.pinlabel.setScaledContents(True)
            self.pinlabel.setWordWrap(False)
            self.pinlabel.setIndent(-1)

            if self.type == PinType.OUTPUT_PIN:
                self.horizontalLayout.addWidget(self.pinlabel, 0, Qt.AlignRight)
                self.horizontalLayout.addWidget(self.contactPin)
            elif self.type == PinType.INPUT_PIN:
                self.horizontalLayout.addWidget(self.contactPin)
                self.horizontalLayout.addWidget(self.pinlabel)
        else:
            self.horizontalLayout.addWidget(self.contactPin)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.contactPin.setText("")
        if not self.type == PinType.EXEC_FLOW_PIN:
            self.pinlabel.setText(QCoreApplication.translate("Form", self.valuename, None))

    # retranslateUi

    def enterEvent(self, event: QEnterEvent):
        print("entering")

    def leaveEvent(self, event: QEvent):
        print("leaving")
