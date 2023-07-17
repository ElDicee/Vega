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
                           QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
                               QSizePolicy, QTreeView, QVBoxLayout, QWidget, QDialog, QFileSystemModel, QMainWindow)


class TreeViewMenu(QMainWindow):
    def __init__(self, parent, init_path=""):
        super(TreeViewMenu, self).__init__()
        self.init_path = init_path
        self.par = parent
        central = QWidget()
        central.setStyleSheet("background-color: rgba(255,0,0);")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(central.sizePolicy().hasHeightForWidth())
        central.setSizePolicy(sizePolicy)
        self.setupUi(central)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.resize(700, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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

        self.topButton = QPushButton(self.widget)
        self.topButton.setObjectName(u"topButton")
        self.topButton.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.topButton)

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

        self.model = QFileSystemModel()
        self.model.setRootPath("")

        self.treeView = QTreeView(self.widget_2)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"QTreeView{border: 2px solid rgb(19, 148, 207);}")
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(self.init_path))
        self.treeView.setColumnWidth(0, 250)

        self.horizontalLayout.addWidget(self.treeView)

        self.verticalLayout.addWidget(self.widget_2)

        self.setCentralWidget(Form)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.cancelBtn.clicked.connect(self.close)
        self.topButton.clicked.connect(lambda: self.changePath(""))
        self.selectBtn.clicked.connect(self.select)
    # setupUi

    def changePath(self, path):
        self.treeView.setRootIndex(self.model.index(path))

    def select(self):
        if self.treeView.selectedIndexes().__len__() > 0:
            self.par.inputpath.setText(self.model.filePath(self.treeView.selectionModel().selectedIndexes()[0]))
            self.close()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Select a path", None))
        self.cancelBtn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.topButton.setText(QCoreApplication.translate("Form", u"Move to Disks", None))
        self.selectBtn.setText(QCoreApplication.translate("Form", u"Select", None))
    # retranslateUi