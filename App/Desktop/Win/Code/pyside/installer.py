# -*- coding: utf-8 -*-
from PySide6 import QtGui, QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Installer(QMainWindow):

    def __init__(self):
        super(Installer, self).__init__()
        self.dragging = False
        self.moving_offset = QPoint(0,0)
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(545, 578)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet(u"QMainWindow{\n"
                                 "	border-image: url(:/img/images/aurora.jpg);\n"
                                 "border-radius: 20px;\n"
                                 "border: 2px solid rgb(0, 170, 255);\n"
                                 "}")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
                                         "background-color: rgba(22, 60, 84, 50);\n"
                                         "}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.langContainer = QWidget(self.centralwidget)
        self.langContainer.setObjectName(u"langContainer")
        sizePolicy1.setHeightForWidth(self.langContainer.sizePolicy().hasHeightForWidth())
        self.langContainer.setSizePolicy(sizePolicy1)
        self.langContainer.setMaximumSize(QSize(16777215, 16777215))
        self.langContainer.setStyleSheet(u"QWidget#langContainer{\n"
                                         "	background-color: rgba(61, 61, 61, 0);\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.langContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.langContainer)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(512, 512))
        self.widget_4.setStyleSheet(u"QWidget#widget_4{\n"
                                    "background-color: rgba(61, 61, 61, 100);\n"
                                    "	border-radius: 10px;	}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(48)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                 "color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.widget_6, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy3)
        self.widget_8.setStyleSheet(u"QWidget#widget_8{\n"
                                    "background-color: rgba(61, 61, 61, 100);\n"
                                    "	border-radius: 10px;	\n"
                                    "}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
                                   "color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_3)

        self.comboBox = QComboBox(self.widget_8)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(420, 0))
        self.comboBox.setStyleSheet(u"QWidget{\n"
                                    "    background-color: rgba(194, 212, 229, 90);\n"
                                    "    border: 2px solid rgb(0, 117, 171);\n"
                                    "    border-radius: 8px;\n"
                                    "    padding: 10px;\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "	font-size: 16px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox {\n"
                                    "    background-color: rgba(194, 212, 229, 90);\n"
                                    "    border: 2px solid rgb(0, 117, 171);\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 10px;\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "	font-size: 13\n"
                                    "}\n"
                                    "\n"
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
                                    ""
                                    "	image: url(:/icons_w/res/feather (1)/arrow-down-circle.svg);\n"
                                    "}\n"
                                    "QComboBox::hover {\n"
                                    "    background-color: rgba(194, 212, 229, 130);\n"
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

        self.verticalLayout_5.addWidget(self.comboBox)

        self.verticalLayout_3.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.pushButton = QPushButton(self.widget_7)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(188, 217, 230, 180)\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u":/icons_w/res/feather (1)/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout_3.addWidget(self.widget_7)

        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.langContainer)

        self.pathcontainer = QWidget(self.centralwidget)
        self.pathcontainer.setObjectName(u"pathcontainer")
        sizePolicy1.setHeightForWidth(self.pathcontainer.sizePolicy().hasHeightForWidth())
        self.pathcontainer.setSizePolicy(sizePolicy1)
        self.pathcontainer.setMinimumSize(QSize(0, 0))
        self.pathcontainer.setMaximumSize(QSize(0, 16777215))
        self.pathcontainer.setStyleSheet(u"QWidget#pathcontainer{\n"
                                         "	background-color: rgba(61, 61, 61, 80);\n"
                                         "	border-radius: 10px;\n"
                                         "}")
        self.verticalLayout_2 = QVBoxLayout(self.pathcontainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.pathcontainer)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setPointSize(14)
        self.label_6.setFont(font4)
        self.label_6.setAcceptDrops(False)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_6)

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.pathcontainer)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy4.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy4)
        self.widget_9.setMinimumSize(QSize(30, 50))
        self.widget_9.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
                                    "border-radius: 10px;")

        self.horizontalLayout_4.addWidget(self.widget_9)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.pathcontainer)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QPushButton{\n"
                                    "	background-color: transparent;\n"
                                    "	border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgba(188, 217, 230, 180)\n"
                                    "}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons_w/res/feather (1)/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButton_2, 0, Qt.AlignLeft)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButton_3, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.pathcontainer)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMaximumSize(QSize(0, 16777215))

        self.horizontalLayout.addWidget(self.widget_5)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(lambda: self.switchWindow(self.langContainer, self.pathcontainer))

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to Vega", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Please, select your language!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Catal\u00e0", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))

        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose your language", None))
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"Can you now understand me? Well, let's jump right in!", None))
        self.pushButton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Where should we install Vega?", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"Please, select a valid path to the folder you want us to install Vega",
                                                        None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragging = True
            self.moving_offset = event.pos().toPointF().toPoint()
            event.accept()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragging = False
            event.accept()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if self.dragging:  #
            self.move(self.pos().x().real + (event.pos().x().real - self.moving_offset.x().real),
                      self.pos().y().real + (event.pos().y().real - self.moving_offset.y().real))
            event.accept()

    @classmethod
    def switchWindow(cls, current:QWidget, new:QWidget):
        current.setMaximumWidth(0)
        new.setMaximumWidth(16777215)