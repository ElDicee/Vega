# -*- coding: utf-8 -*-
import random

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, QStackedWidget, QDialog, QGroupBox,
                               QLineEdit, QGraphicsBlurEffect)
import sys
import topbar
import socket
from random import randint


class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.connection_portal = ConnectionPortal(6969)
        self.canvaspanels = {}
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(1112, 836)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
                                         "border-radius:10px;\n"
                                         "background-color: rgba(255, 255, 255, 90);\n"
                                         "}")
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(10)
        self.setGraphicsEffect(blur_effect)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar = topbar.Topbar_Widget(self)  # TOPBAR
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topbar.sizePolicy().hasHeightForWidth())
        self.topbar.setSizePolicy(sizePolicy1)
        """self.topbar.setMinimumSize(QSize(947, 43))
        self.topbar.setMaximumSize(QSize(16777215, 43))"""

        self.verticalLayout.addWidget(self.topbar)

        self.contentWidg = QWidget(self.centralwidget)
        self.contentWidg.setObjectName(u"contentWidg")
        sizePolicy.setHeightForWidth(self.contentWidg.sizePolicy().hasHeightForWidth())
        self.contentWidg.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.contentWidg)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.slideWidg = QWidget(self.contentWidg)
        self.slideWidg.setObjectName(u"slideWidg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slideWidg.sizePolicy().hasHeightForWidth())
        self.slideWidg.setSizePolicy(sizePolicy2)
        self.slideWidg.setMinimumSize(QSize(0, 0))
        self.slideWidg.setMaximumSize(QSize(240, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.slideWidg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.slideWidg)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.widget_5.setMinimumSize(QSize(0, 120))
        self.widget_5.setMaximumSize(QSize(240, 120))
        self.widget_5.setStyleSheet(u"background-color: rgb(34, 37, 44);\n"
                                    "border-top-left-radius: 10px;\n"
                                    "border-top-right-radius: 10px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.VegaImg = QLabel(self.widget_4)
        self.VegaImg.setObjectName(u"VegaImg")
        font = QFont()
        font.setPointSize(28)
        font.setBold(False)
        self.VegaImg.setFont(font)
        self.VegaImg.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "")
        self.VegaImg.setScaledContents(True)
        self.VegaImg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.VegaImg)

        self.verticalLayout_3.addWidget(self.widget_4)

        self.name_container = QWidget(self.widget_5)
        self.name_container.setObjectName(u"name_container")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.name_container.sizePolicy().hasHeightForWidth())
        self.name_container.setSizePolicy(sizePolicy4)
        self.name_container.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.name_container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.widget = QWidget(self.name_container)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setMinimumSize(QSize(25, 25))
        self.label.setMaximumSize(QSize(25, 25))
        self.label.setStyleSheet(u"image: url(./res/icons/Feather_white/user.svg);")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.UI_usernameLabel = QLabel(self.widget)
        self.UI_usernameLabel.setObjectName(u"UI_usernameLabel")
        sizePolicy5.setHeightForWidth(self.UI_usernameLabel.sizePolicy().hasHeightForWidth())
        self.UI_usernameLabel.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.UI_usernameLabel.setFont(font1)
        self.UI_usernameLabel.setStyleSheet(u"color: rgb(0, 170, 255);")

        self.horizontalLayout_4.addWidget(self.UI_usernameLabel)

        self.horizontalLayout_3.addWidget(self.widget, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.name_container, 0, Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.widget_5)

        self.scrollArea = QScrollArea(self.slideWidg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
                                      "    background-color: rgb(56, 60, 72);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:vertical {\n"
                                      "    width: 12px;\n"
                                      "	background-color: rgb(56, 60, 72);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "    background: #AAAAAA;\n"
                                      "	background-color: rgb(230, 230, 230);\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line:vertical,\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "    height: 12px;\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-page:vertical,\n"
                                      "QScrollBar::sub-page:vertical {\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 207, 543))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(56, 60, 72);")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.widget_7 = QWidget(self.slideWidg)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
        self.widget_7.setMinimumSize(QSize(0, 120))
        self.widget_7.setMaximumSize(QSize(240, 120))
        self.widget_7.setStyleSheet(u"background-color: rgb(34, 37, 44);\n"
                                    "border-bottom-left-radius: 10px;\n"
                                    "border-bottom-right-radius: 10px;\n"
                                    "")
        self.verticalLayout_5 = QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_7)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "border-radius: 12px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "	background-color: rgb(126, 135, 162);\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u"./res/icons/Feather_white/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "border-radius: 12px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: rgb(126, 135, 162);\n"
                                        "}")
        icon1 = QIcon()
        icon1.addFile(u"./res/icons/Feather_white/gitlab.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setMaximumSize(QSize(50, 50))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "border-radius: 12px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: rgb(126, 135, 162);\n"
                                        "}")
        icon2 = QIcon()
        icon2.addFile(u"./res/icons/Feather_white/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.verticalLayout_5.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget_7)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 30))
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setStyleSheet(u"color: rgb(87, 95, 113);")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.widget_2)

        self.verticalLayout_2.addWidget(self.widget_7)

        self.horizontalLayout.addWidget(self.slideWidg)

        self.canvas = QStackedWidget(self.contentWidg)
        self.canvas.setObjectName(u"canvas")
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setMinimumSize(QSize(300, 300))
        self.canvas.setStyleSheet(u"background-color: rgb(232, 236, 247);\n"
                                  "border-radius: 10px;")
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.canvas.addWidget(self.HomePage)
        self.Blueprint = QWidget()
        self.Blueprint.setObjectName(u"Blueprint")
        self.horizontalLayout_7 = QHBoxLayout(self.Blueprint)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = BlueprintView()
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_7.addWidget(self.graphicsView)

        self.canvas.addWidget(self.Blueprint)

        self.horizontalLayout.addWidget(self.canvas)

        self.verticalLayout.addWidget(self.contentWidg)

        self.setCentralWidget(self.centralwidget)

        self.addCanvasPanel("BP", BlueprintView())

        self.retranslateUi()

        self.pushButton_2.clicked.connect(lambda: self.canvas.setCurrentWidget(self.canvaspanels["BP"]))

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.VegaImg.setText(QCoreApplication.translate("MainWindow", u"VEGA", None))
        self.label.setText("")
        self.UI_usernameLabel.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GitHub: https://github.com/ElDicee", None))

    # retranslateUi

    def changeCanvasView(self, w):
        self.canvas.setCurrentWidget()

    def addCanvasPanel(self, name, widget):
        self.canvas.addWidget(widget)
        self.canvaspanels.update({name: widget})

    def exitApp(self):
        self.connection_portal.close_connection()
        self.close()


class BlueprintView(QGraphicsView):
    def __init__(self, **kwargs):
        self.scene = QGraphicsScene()
        super(BlueprintView, self).__init__()
        self.setStyleSheet("background-image: url(./res/icons/images/")
        self.filter = Filter(parent=self)
        self.filter.hide()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if self.filter.isHidden():
            self.filter.move(event.pos())
            self.filter.show()
        else:
            self.filter.move(event.pos())
        event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        if not self.filter.isHidden():
            self.filter.hide()


class Filter(QWidget):

    def __init__(self, **kwargs):
        super(Filter, self).__init__(**kwargs)
        self.elements = []
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(341, 412)
        self.setStyleSheet(u"QWidget{\n"
                           "background-color: rgba(232, 236, 247, 100);\n"
                           "border-radius: 10px;\n"
                           "}\n"
                           "")
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(10)
        self.setGraphicsEffect(blur_effect)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self)
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

        # ADD ALL MODULES

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi()
        self.add_section("TEST")
        self.add_element("title", section="TEST")



        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Filter", None))

    def add_section(self, name):
        section = FilterSection(self.scrollAreaWidgetContents, name)
        self.verticalLayout_2.addWidget(section.groupBox)
        self.elements.append(section)

    def add_element(self, element, section=None):
        if section:
            sec = self.get_section(section)
            sec.add_item(element)
        else:
            label = QLabel(self.scrollAreaWidgetContents)
            label.setText(element)
            self.verticalLayout_2.addWidget(label)
            self.elements.append(label)

    def get_section(self, name):
        sec = None
        for x in self.elements:
            if isinstance(x, FilterSection) and x.groupBox.title() == name:
                sec = x
                break
        return sec


class FilterSection:
    def __init__(self, parent, name):
        self.groupBox = QGroupBox(parent)
        self.groupBox.setObjectName(u"{}".format(name))
        self.groupBox.setTitle(name)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(-1, 25, -1, -1)
        self.items = []
    def __str__(self):
        return self.groupBox.title().title()

    def add_item(self, name):
        label = QLabel(self.groupBox)
        label.setText(name)
        self.verticalLayout.addWidget(label, 0, Qt.AlignTop)
        self.items.append(label)


class ConnectionPortal:
    def __init__(self, port):
        print("creating socket")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        try:
            print("starting connection")
            self.start_connection()
        except OSError:
            self.port = randint(49152, 65535)
            self.start_connection()
        self.buffer = 1024
        self.command_query = []

    def go_listen(self):
        self.socket.listen(1)

    def start_connection(self):
        self.socket.bind(("127.0.0.1", self.port))

    def receive_data(self):
        client, addr = self.socket.accept()
        return client.recv(self.buffer)

    def close_connection(self):
        self.socket.close()

    def change_data_buffer(self, buf: int):
        self.buffer = buf


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = MainFrame()
    Form.show()
    sys.exit(app.exec())
