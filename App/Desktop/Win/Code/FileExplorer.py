# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileExplorer.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
                               QTextEdit, QWidget)
import FileExplorerTree as Tree


class FileExplorerWidget(QWidget):

    def __init__(self, path):
        super(FileExplorerWidget, self).__init__()
        self.path = path
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(791, 68)
        self.setStyleSheet(u"QWidget#Form{\n"
                           "	background-color: rgba(56, 60, 72, 90);\n"
                           "	border-radius: 10px;\n"
                           "}")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputpath = QTextEdit(self)
        self.inputpath.setObjectName(u"inputpath")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputpath.sizePolicy().hasHeightForWidth())
        self.inputpath.setSizePolicy(sizePolicy)
        self.inputpath.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.inputpath.setFont(font)
        self.inputpath.setStyleSheet(u"QTextEdit{\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid rgb(0, 85, 127);\n"
                                     "background-color: rgba(255, 255, 255, 150);\n"
                                     "color: rgb(56, 60, 72);\n"
                                     "padding: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QTextEdit:focus{\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid rgb(19, 148, 207);\n"
                                     "background-color: rgba(255, 255, 255, 190);\n"
                                     "padding: 2px;\n"
                                     "}")
        self.inputpath.setText(self.path)
        self.horizontalLayout.addWidget(self.inputpath)

        self.browsebtn = QPushButton(self)
        self.browsebtn.setObjectName(u"browsebtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.browsebtn.sizePolicy().hasHeightForWidth())
        self.browsebtn.setSizePolicy(sizePolicy1)
        self.browsebtn.setMinimumSize(QSize(60, 40))
        self.browsebtn.setFont(font)
        self.browsebtn.setStyleSheet(u"QPushButton#browsebtn{\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid rgb(0, 85, 127);\n"
                                     "background-color: rgba(255, 255, 255, 150);\n"
                                     "color: rgb(0, 170, 255);\n"
                                     "padding: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#browsebtn:hover{\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid rgb(19, 148, 207);\n"
                                     "background-color: rgba(255, 255, 255, 190);\n"
                                     "color: rgb(38, 197, 255);\n"
                                     "padding: 2px;\n"
                                     "}")
        icon = QIcon()
        icon.addFile(u"./res/icons/Feather_white/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browsebtn.setIcon(icon)
        self.browsebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.browsebtn)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        self.browsebtn.clicked.connect(self.openBrowsing)
    # setupUi

    def openBrowsing(self):
        tree = Tree.TreeViewMenu(self, init_path=self.path)
        tree.show()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.browsebtn.setText(QCoreApplication.translate("Form", u"Buscar", None))
    # retranslateUi
