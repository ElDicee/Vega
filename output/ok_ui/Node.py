# -*- coding: utf-8 -*-

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QEnterEvent)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget)
from NodePin import Pin, PinType
import enum


class NodeType(enum.Enum):
    EXECUTION = "exec"
    OPERATOR = "oper"


class Node(QWidget):

    def __init__(self, name:str, node_type:NodeType):
        super(Node, self).__init__()
        self.input_pins = {}
        self.output_pins = {}
        self.function = None
        self.name = name
        self.node_type = node_type
        self.border_color = [232, 236, 247]

        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Node")
        self.resize(313, 384)
        self.setStyleSheet(u"QWidget#Node{\n"
                           "border-radius: 20px;\n"
                           f"background-color: rgb({self.border_color[0]},{self.border_color[1]},{self.border_color[2]});\n"
                           "border - color: rgb(0, 170, 255);\n"
                           "border-width: 3px;\n"
                           "}")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 2, 4, 2)
        self.titlecont = QWidget(self)
        self.titlecont.setObjectName(u"titlecont")
        self.titlecont.setMinimumSize(QSize(0, 30))
        self.titlecont.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.titlecont)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlecont2 = QWidget(self.titlecont)
        self.titlecont2.setObjectName(u"titlecont2")
        self.horizontalLayout_2 = QHBoxLayout(self.titlecont2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.titlecont2)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Star Cartoon"])
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalLayout.addWidget(self.titlecont2)

        self.verticalLayout.addWidget(self.titlecont)

        if self.node_type == NodeType.EXECUTION:
            self.exec_spacepin = QWidget(self)
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
            self.exec_in_pin = Pin(type=PinType.EXEC_FLOW_PIN, valuename="exec_in", parent=self.exec_spacepin)
            self.exec_in_pin.setObjectName(u"exec_in")

            self.horizontalLayout_4.addWidget(self.exec_in_pin, 0, Qt.AlignLeft)

            self.exec_out_pin = Pin(type=PinType.EXEC_FLOW_PIN, valuename="exec_out", parent=self.exec_spacepin)
            self.exec_out_pin.setObjectName(u"exec_out")

            self.horizontalLayout_4.addWidget(self.exec_out_pin, 0, Qt.AlignRight)

            self.verticalLayout.addWidget(self.exec_spacepin)

        self.customzone = QWidget(self)
        self.customzone.setObjectName(u"customzone")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customzone.sizePolicy().hasHeightForWidth())
        self.customzone.setSizePolicy(sizePolicy)
        self.customzone.setMaximumSize(QSize(16777215, 0))

        self.verticalLayout.addWidget(self.customzone)

        self.signalpincontent = QWidget(self)
        self.signalpincontent.setObjectName(u"signalpincontent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.signalpincontent.sizePolicy().hasHeightForWidth())
        self.signalpincontent.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.signalpincontent)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.widget_4 = QWidget(self.signalpincontent)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.signalpincontent)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.signalpincontent)
        self.widget_5.setObjectName(u"widget_5")

        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_5)

        self.verticalLayout.addWidget(self.signalpincontent)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

        if self.node_type == NodeType.EXECUTION:
            pass



    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Node", u"Form", None))
        self.title.setText(QCoreApplication.translate("Node", self.name, None))

    # retranslateUi

    def addInputPin(self, name):
        self.input_pins.update({name: None})
        self.verticalLayout_2.addWidget(Pin(valuename=name, parent=self.widget_4))

    def addOutputPin(self, name):
        self.output_pins.update({name: None})
        self.verticalLayout_3.addWidget(Pin(type=PinType.OUTPUT_PIN, valuename=name, parent=self.widget_5))

    def setFunction(self, func):
        self.function = func

    def run(self):
        self.function(self.input_pins, self.output_pins)


def suma(inp, outp):
    outp.update({"Result": {inp["Num1"] + inp["Num2"]}})

if __name__ == "__main__":
    app = QApplication(sys.argv)
    n = Node("Suma", NodeType.OPERATOR)
    n.addInputPin("Num1")
    n.addInputPin("Num2")
    n.addOutputPin("Result")
    n.setFunction(suma)
    n.show()
    sys.exit(app.exec())
