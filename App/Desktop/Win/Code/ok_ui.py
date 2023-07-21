# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ok_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget)
import sys
import topbar


class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
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

        self.canvas = QWidget(self.contentWidg)
        self.canvas.setObjectName(u"canvas")
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setMinimumSize(QSize(300, 300))
        self.canvas.setStyleSheet(u"background-color: rgb(232, 236, 247);\n"
                                  "border-radius: 10px;")

        self.horizontalLayout.addWidget(self.canvas)

        self.verticalLayout.addWidget(self.contentWidg)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

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

    def changeCanvasView(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = MainFrame()
    Form.show()
    sys.exit(app.exec())
