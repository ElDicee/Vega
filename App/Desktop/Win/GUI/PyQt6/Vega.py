import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class Topbar(QtWidgets.QWidget):
    def __init__(self, mainwin: QtWidgets.QWidget, **kwargs):
        super(Topbar, self).__init__()
        self.dragging = False
        self.moving_offset = None
        self.mainwin = mainwin
        self.setupUi()
        self.username = kwargs.get("username")
        self.slidebar:QtWidgets.QWidget = None

    def setSlidebar(self, slidebar):
        self.slidebar = slidebar

    def setupUi(self):
        self.setObjectName("Topbar")
        self.resize(744, 43)
        self.setMinimumSize(QtCore.QSize(300, 43))
        self.setMaximumSize(QtCore.QSize(16777215, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("QWidget#Topbar{\n"
                           "background-color: rgb(34, 37, 44);\n"
                           "border-radius: 10px;\n"
                           "}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=self)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ToggleSlideMenuBtn = QtWidgets.QPushButton(parent=self.widget)
        self.ToggleSlideMenuBtn.setMinimumSize(QtCore.QSize(25, 25))
        self.ToggleSlideMenuBtn.setMaximumSize(QtCore.QSize(25, 25))
        self.ToggleSlideMenuBtn.setStyleSheet("QPushButton#ToggleSlideMenuBtn{\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(34, 37, 44);\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "QPushButton#ToggleSlideMenuBtn:hover{\n"
                                              "    \n"
                                              "    background-color: rgb(102, 111, 132);\n"
                                              "}")
        self.ToggleSlideMenuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/Feather_white/corner-up-left.svg"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ToggleSlideMenuBtn.setIcon(icon)
        self.ToggleSlideMenuBtn.setObjectName("ToggleSlideMenuBtn")
        self.horizontalLayout_3.addWidget(self.ToggleSlideMenuBtn)
        self.user_person_img = QtWidgets.QLabel(parent=self.widget)
        self.user_person_img.setText("")
        self.user_person_img.setObjectName("user_person_img")
        self.horizontalLayout_3.addWidget(self.user_person_img)
        self.user_name = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("color: rgb(0, 170, 255);")
        self.user_name.setObjectName("user_name")
        self.horizontalLayout_3.addWidget(self.user_name)
        self.horizontalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.widget_2 = QtWidgets.QWidget(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.expandBtn = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expandBtn.sizePolicy().hasHeightForWidth())
        self.expandBtn.setSizePolicy(sizePolicy)
        self.expandBtn.setMaximumSize(QtCore.QSize(18, 18))
        self.expandBtn.setStyleSheet("QPushButton#expandBtn{\n"
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
        self.expandBtn.setText("")
        self.expandBtn.setObjectName("expandBtn")
        self.horizontalLayout_2.addWidget(self.expandBtn)
        self.minBtn = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy)
        self.minBtn.setMaximumSize(QtCore.QSize(18, 18))
        self.minBtn.setStyleSheet("QPushButton#minBtn{\n"
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
        self.minBtn.setText("")
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout_2.addWidget(self.minBtn)
        self.closeBtn = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMaximumSize(QtCore.QSize(18, 18))
        self.closeBtn.setStyleSheet("QPushButton#closeBtn{\n"
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
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn)
        self.horizontalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # SIGNALS-------------------------------------------------------------------
        self.closeBtn.clicked.connect(self.mainwin.exit_app)
        self.expandBtn.clicked.connect(self.maximize)
        self.minBtn.clicked.connect(self.mainwin.showMinimized)
        self.ToggleSlideMenuBtn.clicked.connect(lambda: self.slide_menu())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.user_name.setText(_translate("self", "PERSON NAME"))

    def slide_menu(self):
        icon = QtGui.QIcon()
        if self.slidebar.width() <= 0:
            nw = 240
            icon.addPixmap(QtGui.QPixmap("./res/Feather_white/corner-up-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.ToggleSlideMenuBtn.setIcon(icon)
        else:
            nw = 0
            icon.addPixmap(QtGui.QPixmap("./res/Feather_white/menu.svg"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.ToggleSlideMenuBtn.setIcon(icon)

        self.animation = QtCore.QPropertyAnimation(self.slidebar, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setEndValue(nw)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()
        self.slidebar.setMaximumWidth(0)
        self.slidebar.update()
        print("here4")


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
            self.mainwin.move(self.mainwin.pos().x().real + (event.pos().x().real - self.moving_offset.x().real),
                              self.mainwin.pos().y().real + (event.pos().y().real - self.moving_offset.y().real))
            event.accept()

    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.maximize()
            event.accept()

    def maximize(self):
        if self.mainwin.isMaximized():
            self.mainwin.showNormal()
        else:
            self.mainwin.showMaximized()


class slidemenubtn_UIO(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(240, 50))
        Form.setMaximumSize(QtCore.QSize(240, 50))
        Form.setStyleSheet("QWidget{\n"
                           "background-color: rgb(56, 60, 72);\n"
                           "border-radius: 10px;\n"
                           "}\n"
                           "\n"
                           "QWidget:hover{\n"
                           "    background-color: rgb(144, 155, 186);\n"
                           "}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.itgstatusindicator = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itgstatusindicator.sizePolicy().hasHeightForWidth())
        self.itgstatusindicator.setSizePolicy(sizePolicy)
        self.itgstatusindicator.setMinimumSize(QtCore.QSize(15, 15))
        self.itgstatusindicator.setMaximumSize(QtCore.QSize(15, 15))
        self.itgstatusindicator.setStyleSheet("border-radius: 5px;\n"
                                              "background-color: rgb(38, 225, 54);")
        self.itgstatusindicator.setObjectName("itgstatusindicator")
        self.horizontalLayout.addWidget(self.itgstatusindicator)
        self.button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setMinimumSize(QtCore.QSize(210, 32))
        self.button.setMaximumSize(QtCore.QSize(210, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.button.setFont(font)
        self.button.setStyleSheet("border-radius: 10px;\n"
                                  "background-color: rgba(255, 255, 255, 0);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "text-align: left;")
        self.button.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.button.setCheckable(False)
        self.button.setAutoRepeat(False)
        self.button.setAutoExclusive(False)
        self.button.setObjectName("button")
        self.horizontalLayout.addWidget(self.button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button.setText(_translate("Form", "NAME"))


class Vega_UI(QtWidgets.QMainWindow):

    def __init__(self):
        super(Vega_UI, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1404, 817)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
                                         "border-radius:10px;\n"
                                         "background-color: rgba(255, 255, 255, 140);\n"
                                         "}")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0,92,157, 550))
        self.centralwidget.setGraphicsEffect(self.shadow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topbar = Topbar(mainwin=self, parent=self.centralwidget)
        self.verticalLayout.addWidget(self.topbar)
        self.contentWidg = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentWidg.sizePolicy().hasHeightForWidth())
        self.contentWidg.setSizePolicy(sizePolicy)
        self.contentWidg.setObjectName("contentWidg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.contentWidg)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slideWidg = QtWidgets.QWidget(parent=self.contentWidg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideWidg.sizePolicy().hasHeightForWidth())
        self.slideWidg.setSizePolicy(sizePolicy)
        self.slideWidg.setMinimumSize(QtCore.QSize(240, 0))
        self.slideWidg.setMaximumSize(QtCore.QSize(240, 16777215))
        self.slideWidg.setObjectName("slideWidg")
        self.topbar.setSlidebar(self.slideWidg)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slideWidg)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(parent=self.slideWidg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(240, 120))
        self.widget_5.setMaximumSize(QtCore.QSize(240, 120))
        self.widget_5.setStyleSheet("background-color: rgb(34, 37, 44);\n"
                                    "border-top-left-radius: 10px;\n"
                                    "border-top-right-radius: 10px;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VegaImg = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        self.VegaImg.setFont(font)
        self.VegaImg.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "")
        self.VegaImg.setScaledContents(True)
        self.VegaImg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.VegaImg.setObjectName("VegaImg")
        self.verticalLayout_3.addWidget(self.VegaImg)
        self.name_container = QtWidgets.QWidget(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_container.sizePolicy().hasHeightForWidth())
        self.name_container.setSizePolicy(sizePolicy)
        self.name_container.setMinimumSize(QtCore.QSize(240, 0))
        self.name_container.setObjectName("name_container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.name_container)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(parent=self.name_container)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(25, 25))
        self.label.setMaximumSize(QtCore.QSize(25, 25))
        self.label.setStyleSheet("image: url(./res/Feather_white/user.svg);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.UI_usernameLabel = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UI_usernameLabel.sizePolicy().hasHeightForWidth())
        self.UI_usernameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.UI_usernameLabel.setFont(font)
        self.UI_usernameLabel.setStyleSheet("color: rgb(0, 170, 255);")
        self.UI_usernameLabel.setObjectName("UI_usernameLabel")
        self.horizontalLayout_4.addWidget(self.UI_usernameLabel)
        self.horizontalLayout_3.addWidget(self.widget, 0,
                                          QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.name_container, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.slideWidg)
        self.scrollArea.setStyleSheet("QScrollArea {\n"
                                      "    background-color: rgb(56, 60, 72);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:vertical {\n"
                                      "    width: 12px;\n"
                                      "    background-color: rgb(56, 60, 72);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "    background: #AAAAAA;\n"
                                      "    background-color: rgb(230, 230, 230);\n"
                                      "    border-radius: 5px;\n"
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
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 240, 299))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(56, 60, 72);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.widget_7 = QtWidgets.QWidget(parent=self.slideWidg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QtCore.QSize(240, 120))
        self.widget_7.setMaximumSize(QtCore.QSize(240, 120))
        self.widget_7.setStyleSheet("background-color: rgb(34, 37, 44);\n"
                                    "border-bottom-left-radius: 10px;\n"
                                    "border-bottom-right-radius: 10px;\n"
                                    "")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_7)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border-radius: 12px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(126, 135, 162);\n"
                                      "}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/Feather_white/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border-radius: 12px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(126, 135, 162);\n"
                                        "}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./res/Feather_white/gitlab.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "border-radius: 12px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(126, 135, 162);\n"
                                        "}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./res/Feather_white/tool.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_7)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setStyleSheet("color: rgb(87, 95, 113);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0,
                                          QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.horizontalLayout.addWidget(self.slideWidg)
        self.canvas = QtWidgets.QWidget(parent=self.contentWidg)
        self.canvas.setMinimumSize(QtCore.QSize(300, 300))
        self.canvas.setStyleSheet("background-color: rgb(232, 236, 247);\n"
                                  "border-radius: 10px;")
        self.canvas.setObjectName("canvas")
        self.horizontalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.contentWidg)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.VegaImg.setText(_translate("MainWindow", "VEGA"))
        self.UI_usernameLabel.setText(_translate("MainWindow", "User Name"))
        self.label_2.setText(_translate("MainWindow", "GitHub: https://github.com/ElDicee"))

    # EXIT -------------------------------------------------------------------------------------------------------------------------------------------------------
    def exit_app(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Vega_UI()
    window.show()
    sys.exit(app.exec())
