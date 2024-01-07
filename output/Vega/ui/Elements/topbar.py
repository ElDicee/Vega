# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'topbar.ui'
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
                           QPalette, QPixmap, QRadialGradient, QTransform, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QWidget)


class Topbar_Widget(QWidget):

    def __init__(self, father):
        super(Topbar_Widget, self).__init__()
        self.dragging = False
        self.moving_offset = QPoint()
        self.father = father
        self.setupUi()

    def setupUi(self):
        self.setObjectName(u"Topbar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(947, 43))
        self.setMaximumSize(QSize(16777215, 43))
        self.setStyleSheet(u"QWidget#Topbar{\n"
                           "background-color: rgb(34, 37, 44);\n"
                           "border-radius: 10px;\n"
                           "}")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.ToggleSlideMenuBtn = QPushButton(self.widget)
        self.ToggleSlideMenuBtn.setObjectName(u"ToggleSlideMenuBtn")
        self.ToggleSlideMenuBtn.setMinimumSize(QSize(25, 25))
        self.ToggleSlideMenuBtn.setMaximumSize(QSize(25, 25))
        self.ToggleSlideMenuBtn.setStyleSheet(u"QPushButton#ToggleSlideMenuBtn{\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(34, 37, 44);\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "QPushButton#ToggleSlideMenuBtn:hover{\n"
                                              "	\n"
                                              "	background-color: rgb(102, 111, 132);\n"
                                              "}")
        icon = QIcon()
        icon.addFile(u"./res/icons/Feather_white/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToggleSlideMenuBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.ToggleSlideMenuBtn)

        self.user_person_img = QLabel(self.widget)
        self.user_person_img.setObjectName(u"user_person_img")

        self.horizontalLayout_3.addWidget(self.user_person_img)

        self.user_name = QLabel(self.widget)
        self.user_name.setObjectName(u"user_name")
        font = QFont()
        font.setBold(True)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet(u"color: rgb(0, 170, 255);")

        self.horizontalLayout_3.addWidget(self.user_name)

        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.expandBtn = QPushButton(self.widget_2)
        self.expandBtn.setObjectName(u"expandBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.expandBtn.sizePolicy().hasHeightForWidth())
        self.expandBtn.setSizePolicy(sizePolicy2)
        self.expandBtn.setMaximumSize(QSize(18, 18))
        self.expandBtn.setStyleSheet(u"QPushButton#expandBtn{\n"
                                     "background-color: rgb(38, 225, 54);\n"
                                     "border-radius: 8px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#expandBtn:hover{\n"
                                     "background-color: rgb(137, 225, 121);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#expandBtn:pressed{\n"
                                     "background-color: rgb(61, 148, 225);\n"
                                     "}")

        self.horizontalLayout_2.addWidget(self.expandBtn)

        self.minBtn = QPushButton(self.widget_2)
        self.minBtn.setObjectName(u"minBtn")
        sizePolicy2.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy2)
        self.minBtn.setMaximumSize(QSize(18, 18))
        self.minBtn.setStyleSheet(u"QPushButton#minBtn{\n"
                                  "background-color: rgb(255, 157, 44);\n"
                                  "border-radius: 8px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#minBtn:hover{\n"
                                  "background-color: rgb(255, 180, 89);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#minBtn:pressed{\n"
                                  "background-color: rgb(61, 148, 225);\n"
                                  "}")

        self.horizontalLayout_2.addWidget(self.minBtn)

        self.closeBtn = QPushButton(self.widget_2)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy2.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy2)
        self.closeBtn.setMaximumSize(QSize(18, 18))
        self.closeBtn.setStyleSheet(u"QPushButton#closeBtn{\n"
                                    "background-color: rgb(255, 53, 53);\n"
                                    "border-radius: 8px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#closeBtn:hover{\n"
                                    "background-color: rgb(255, 105, 105);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#closeBtn:pressed{\n"
                                    "background-color: rgb(61, 148, 225);\n"
                                    "}")

        self.horizontalLayout_2.addWidget(self.closeBtn)

        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignRight)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

        self.closeBtn.clicked.connect(self.father.exitApp)
        self.expandBtn.clicked.connect(self.maximization)
        self.minBtn.clicked.connect(self.father.showMinimized)
        self.ToggleSlideMenuBtn.clicked.connect(self.toggleSlideMenu)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Topbar", u"Form", None))
        self.ToggleSlideMenuBtn.setText("")
        self.user_person_img.setText("")
        self.user_name.setText(QCoreApplication.translate("Topbar", u"PERSON NAME", None))
        self.expandBtn.setText("")
        self.minBtn.setText("")
        self.closeBtn.setText("")

    # retranslateUi

    def maximization(self):
        if self.father.isMaximized():
            self.father.showNormal()
        else:
            self.father.showMaximized()

    def toggleSlideMenu(self):
        if self.father.slideWidg.maximumWidth() > 0:
            self.father.slideWidg.setMaximumWidth(0)
        else:
            self.father.slideWidg.setMaximumWidth(240)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.moving_offset = event.pos().toPointF().toPoint()
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:  #
            self.father.move(self.father.pos().x().real + (event.pos().x().real - self.moving_offset.x().real),
                             self.father.pos().y().real + (event.pos().y().real - self.moving_offset.y().real))
            event.accept()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.maximization()
