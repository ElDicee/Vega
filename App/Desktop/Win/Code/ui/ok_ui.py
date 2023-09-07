# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QIcon,
                           QMouseEvent, QPainter)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, QStackedWidget, QGroupBox,
                               QLineEdit, QGraphicsBlurEffect, QDialog, QProgressBar, QGraphicsWidget, QGraphicsItem,
                               QGraphicsProxyWidget)

from App.Desktop.Win.Code.ui.Elements import Node, topbar, Node1
from App.Desktop.Win.Code.ui.NodeEditor.Editor import BlueprintView, EditorWidget


class MainFrame(QMainWindow):
    def __init__(self, vega, **kwargs):
        super(MainFrame, self).__init__()
        self.vega = vega
        self.canvaspanels = {}
        self.setupUi()
        if kwargs.get("show"):
            self.show()

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
        self.canvas.setStyleSheet(u"border-radius: 10px;")
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.canvas.addWidget(self.HomePage)
        self.Blueprint = QWidget()
        self.Blueprint.setObjectName(u"Blueprint")
        self.horizontalLayout_7 = QHBoxLayout(self.Blueprint)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = EditorWidget(self.vega)

        self.horizontalLayout_7.addWidget(self.graphicsView)

        self.canvas.addWidget(self.Blueprint)

        self.horizontalLayout.addWidget(self.canvas)

        self.verticalLayout.addWidget(self.contentWidg)

        self.setCentralWidget(self.centralwidget)

        self.addCanvasPanel("BP", self.Blueprint)

        self.retranslateUi()

        self.pushButton_2.clicked.connect(lambda: self.canvas.setCurrentWidget(self.canvaspanels["BP"]))

        QMetaObject.connectSlotsByName(self)

        for itg in self.vega.integrations.values():
            if itg.display is not None:
                s = SlideButton(itg, parent=self.scrollAreaWidgetContents)
                self.verticalLayout_4.addWidget(s, 0, Qt.AlignmentFlag.AlignTop)

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
        self.close()


class SlideButton(QWidget):

    def __init__(self, integration, **kwargs):
        super(SlideButton, self).__init__(**kwargs)
        self.integration = integration
        self.setupUi()
        self.label.setText(self.integration.name.upper())

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Button")
        self.resize(240, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(240, 50))
        self.setMaximumSize(QSize(240, 50))
        self.setStyleSheet(u"QWidget{\n"
                           "background-color: rgb(56, 60, 72);\n"
                           "border-radius: 10px;\n"
                           "}\n"
                           "\n"
                           "QWidget:hover{\n"
                           "	background-color: rgb(144, 155, 186);\n"
                           "}")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.itgstatusindicator = QWidget(self)
        self.itgstatusindicator.setObjectName(u"itgstatusindicator")
        sizePolicy.setHeightForWidth(self.itgstatusindicator.sizePolicy().hasHeightForWidth())
        self.itgstatusindicator.setSizePolicy(sizePolicy)
        self.itgstatusindicator.setMinimumSize(QSize(15, 15))
        self.itgstatusindicator.setMaximumSize(QSize(15, 15))
        self.itgstatusindicator.setStyleSheet(u"border-radius: 5px;\n"
                                              "background-color: rgb(38, 225, 54);")

        self.horizontalLayout.addWidget(self.itgstatusindicator)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                 "background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.label)

        QMetaObject.connectSlotsByName(self)

    def mousePressEvent(self, event: QMouseEvent):
        print("hello")


def parse_type_from_str(s):
    s = str(s).lstrip().rstrip().lower()
    t = object
    if s == "int":
        t = int
    elif s == "str":
        t = str
    elif s == "float":
        t = float
    elif s == "bool":
        t = bool
    return t


# class BlueprintView(QGraphicsView):
#     def __init__(self, vega, **kwargs):
#         self.vega = vega
#         super(BlueprintView, self).__init__()
#         self.setScene(QGraphicsScene())
#         self.setObjectName("BP_bg")
#         # self.setStyleSheet("QWidget#BP_bg{background-image: url(./res/images/bpbg.jpg)}")
#         self.setRenderHint(QPainter.Antialiasing)
#         self.setWindowTitle("Node in QGraphicsItem")
#         self.filter = Filter(self.vega, self, parent=self)
#         self.filter.do_hide()
#
#     def mouseDoubleClickEvent(self, event: QMouseEvent):
#         if self.filter.isHidden():
#             self.filter.move(event.pos())
#             self.filter.show()
#         else:
#             self.filter.move(event.pos())
#         event.accept()
#
#     def mousePressEvent(self, event: QMouseEvent):
#         if not self.filter.isHidden():
#             self.filter.do_hide()
#
#     def spawn_node(self, method, section):
#         data = self.vega.integrations.get(section)
#         meth = data.methods.get(method)
#         node = Node.Node(method.title(), Node.NodeType.valueOf(meth.get("node")), formal_name=meth.get("formal_name"))
#         print(meth.get("inputs"))
#         for inp_name, datatype in meth.get("inputs").items():
#             node.addInputPin(inp_name, parse_type_from_str(datatype))
#         if meth.get("extend")[0]:  # ARGS
#             pass
#         if meth.get("extend")[1]:  # KW
#             pass
#         for name, type in meth.get("outs").items():
#             node.addOutputPin(name, parse_type_from_str(type))
#         n = QGraphicsProxyWidget()
#         n.setWidget(node)
#         n.setPos(self.filter.pos())
#         n.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
#         n.setFlag(QGraphicsItem.ItemIsSelectable)
#         n.setFlag(QGraphicsItem.ItemIsMovable)
#         n.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
#         n.setFlag(QGraphicsItem.GraphicsItemFlag.ItemAcceptsInputMethod)
#         self.scene().addItem(NodeGraphicsItem(node))
#         self.filter.do_hide()
#
#
# class LoadBar(QDialog):
#
#     def __init__(self):
#         super().__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         if not self.objectName():
#             self.setObjectName(u"Form")
#         self.resize(740, 208)
#         self.setStyleSheet(u"background-color: rgb(232, 236, 247);\n"
#                            "border-radius: 20px;")
#         self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
#         self.verticalLayout = QVBoxLayout(self)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.label = QLabel(self)
#         self.label.setObjectName(u"label")
#         font = QFont()
#         font.setFamilies([u"Super Mario 256"])
#         font.setPointSize(18)
#         font.setBold(True)
#         self.label.setFont(font)
#         self.label.setStyleSheet(
#             u"color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(0, 0, 0, 184), stop:1 rgba(255, 255, 255, 0));")
#
#         self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignVCenter)
#
#         self.progressBar = QProgressBar(self)
#         self.progressBar.setObjectName(u"progressBar")
#         self.progressBar.setMaximumSize(QSize(16777215, 20))
#         self.progressBar.setStyleSheet(u"QProgressBar {\n"
#                                        "                border: 2px solid grey;\n"
#                                        "                border-radius: 8px;\n"
#                                        "                background: rgba(56, 60, 72, 20);\n"
#                                        "            }\n"
#                                        "\n"
#                                        "            QProgressBar::chunk {\n"
#                                        "                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 "
#                                        "rgb(0, 200, 255), stop:1 rgb(140, 0, 255));\n"
#                                        "                border-radius: 6px;\n"
#                                        "            }")
#         self.progressBar.setValue(50)
#
#         self.verticalLayout.addWidget(self.progressBar)
#
#         self.label_2 = QLabel(self)
#         self.label_2.setObjectName(u"label_2")
#         font1 = QFont()
#         font1.setFamilies([u"Yu Gothic UI"])
#         font1.setPointSize(9)
#         self.label_2.setFont(font1)
#
#         self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)
#
#         self.retranslateUi()
#
#         QMetaObject.connectSlotsByName(self)
#
#     # setupUi
#
#     def retranslateUi(self):
#         self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#         self.label.setText(QCoreApplication.translate("Form", u"The integrations are loading!", None))
#         self.progressBar.setFormat("")
#         self.label_2.setText(QCoreApplication.translate("Form", u"Please, wait until the process is finished.", None))
