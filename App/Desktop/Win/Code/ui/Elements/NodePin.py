# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QEnterEvent)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QWidget, QCheckBox, QComboBox, QLineEdit, QSpinBox, QDoubleSpinBox)

from enum import Enum


class PinType(Enum):
    INPUT_PIN = "in"
    OUTPUT_PIN = "out"
    EXEC_FLOW_PIN = "exec"


class ContactPin(QPushButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setObjectName(u"contactPin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy1)
        self.setMinimumSize(QSize(20, 20))
        self.setMaximumSize(QSize(20, 20))
        self.setStyleSheet(u"QPushButton{\n"
                           "	background-color: rgb(56, 60, 72);\n"
                           "	border-radius: 8px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "	background-color: rgb(0, 170, 255);\n"
                           "	border-radius: 10px;\n"
                           "}")
        icon = QIcon()
        icon.addFile(u":../../res/icons/Feather_white/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon)

    def change_icon(self, icon):
        self.setIcon(icon)

    def enterEvent(self, event: QEnterEvent):
        pass

    def leaveEvent(self, event: QEvent):
        pass


class Pin(QWidget):

    def __init__(self, type: PinType = PinType.INPUT_PIN, valuename: str = "Value", datatype=object, **kwargs):
        super(Pin, self).__init__(**kwargs)
        self.contactPin = None
        self.valuename = valuename
        self.data_type = datatype
        self.type = type
        if kwargs.get("extend"):
            pass
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
        self.contactPin = ContactPin(parent=self)

        if self.type is not PinType.EXEC_FLOW_PIN:
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

            align = Qt.AlignmentFlag.AlignLeft
            if self.type == PinType.OUTPUT_PIN:
                align = Qt.AlignmentFlag.AlignRight

            if self.type == PinType.INPUT_PIN:
                self.horizontalLayout.addWidget(self.contactPin, 0, align)
                self.horizontalLayout.addWidget(self.pinlabel, 0, align)
            else:
                self.horizontalLayout.addWidget(self.pinlabel, 0, align)
                self.horizontalLayout.addWidget(self.contactPin, 0, align)

            if self.data_type == str:
                self.add_string()
            elif self.data_type == bool:
                self.add_boolean()
            elif self.data_type == int:
                self.add_int()
            elif self.data_type == float:
                self.add_float()

            self.retranslateUi()
        else:
            if self.valuename.lower() == "in":
                self.horizontalLayout.addWidget(self.contactPin, 0, Qt.AlignmentFlag.AlignLeft)
            else:
                self.horizontalLayout.addWidget(self.contactPin, 0, Qt.AlignmentFlag.AlignRight)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.contactPin.setText("")
        if not self.type == PinType.EXEC_FLOW_PIN:
            self.pinlabel.setText(QCoreApplication.translate("Form", self.valuename, None))

    def add_int(self):
        self.param_int = QSpinBox(self)
        self.param_int.setObjectName(u"param_int")
        self.param_int.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
                                     "border-radius: 4px;\n"
                                     "\n"
                                     "QWidget{\n"
                                     "}")

        self.horizontalLayout.addWidget(self.param_int, 0, Qt.AlignLeft)

    def add_float(self):
        self.param_float = QDoubleSpinBox(self)
        self.param_float.setObjectName(u"param_float")
        self.param_float.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
                                       "border-radius: 4px;\n"
                                       "")

        self.horizontalLayout.addWidget(self.param_float, 0, Qt.AlignLeft)

    def add_string(self):
        self.param_string = QLineEdit(self)
        self.param_string.setObjectName(u"param_string")
        self.param_string.setStyleSheet(u"QLineEdit{\n"
                                        "border: 2px solid rgb(0, 85, 255);\n"
                                        "border-radius: 8px;\n"
                                        "background-color: qradialgradient(spread:pad, cx:1, cy:0.5, radius:1.2, fx:1, fy:0.5, stop:0 rgba(56, 60, 72, 50), stop:1 rgba(255, 255, 255, 0));\n"
                                        "}\n"
                                        "QLineEdit::hover{\n"
                                        "border: 3px solid rgb(255, 85, 127);\n"
                                        "}\n"
                                        "QLineEdit::focus{\n"
                                        "border: 2.5px solid rgb(170, 0, 127);\n"
                                        "}")

        self.horizontalLayout.addWidget(self.param_string, 0, Qt.AlignLeft | Qt.AlignVCenter)

    def add_combo_box(self):
        self.param_options = QComboBox(self)
        self.param_options.addItem("")
        self.param_options.addItem("")
        self.param_options.setObjectName(u"param_options")
        self.param_options.setStyleSheet(u"QWidget{\n"
                                         "    background-color: rgba(194, 212, 229, 90);\n"
                                         "    border: 2px solid rgb(0, 117, 171);\n"
                                         "    border-radius: 8px;\n"
                                         "	color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "QComboBox {\n"
                                         "    background-color: rgba(194, 212, 229, 90);\n"
                                         "    border: 2px solid rgb(0, 85, 255);\n"
                                         "    border-radius: 10px;\n"
                                         "	color: rgb(0, 170, 255);\n"
                                         "}\n"
                                         "QComboBox::drop-down {\n"
                                         "    subcontrol-origin: padding;\n"
                                         "    subcontrol-position: top right;\n"
                                         "    width: 28px;\n"
                                         "	background-color: rgba(255, 255, 255, 30);\n"
                                         "    border-left-width: 1px;\n"
                                         "    border-left-color: rgba(255, 255, 255, 40);\n"
                                         "    border-left-style: solid; /* just a single line */\n"
                                         "    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
                                         "    border-bottom-right-radius: 10px;\n"
                                         "}\n"
                                         "QComboBox::down-arrow {\n"
                                         "	border: none;\n"
                                         "	padding: 5px;\n"
                                         "	border-bottom-right-radius: 10px;\n"
                                         "	border-top-right-radius: 10px;\n"
                                         "	image: url(:/icons_w/res/feather (1)/arrow-down-circle.svg);\n"
                                         "}\n"
                                         "QComboBox::hover {\n"
                                         "   "
                                         " background-color: rgba(194, 212, 229, 130);\n"
                                         "	border: 2px solid rgb(40, 133, 195);\n"
                                         "}\n"
                                         "QComboBox::on {\n"
                                         "    background-color: rgba(255, 255, 255, 190)\n"
                                         "}\n"
                                         "QScrollBar{\n"
                                         "	border-radius: 8px;\n"
                                         "	border: 1px solid rgb(0, 85, 127);\n"
                                         "	background-color: rgba(255, 255, 255,30);\n"
                                         "}\n"
                                         "QScrollBar::handle{\n"
                                         "	background-color: rgb(0, 170, 255);\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QScrollBar::sub-line{\n"
                                         "	image: url(:/icons_w/res/feather (1)/arrow-up.svg);\n"
                                         "}\n"
                                         "QScrollBar::add-line{\n"
                                         "	image: url(:/icons_w/res/feather (1)/arrow-down.svg);\n"
                                         "}")

        self.horizontalLayout.addWidget(self.param_options, 0, Qt.AlignLeft)

    def add_boolean(self):
        self.param_boolean = QCheckBox(self)
        self.param_boolean.setObjectName(u"param_boolean")
        self.param_boolean.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.param_boolean, 0, Qt.AlignLeft)
