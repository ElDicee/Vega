from PySide6.QtMultimedia import QSoundEffect

import integrations.VegaAPI as api

from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect,QSize, QUrl, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QDialog, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget)


class Dialog(QDialog):

    def __init__(self, title, text):
        super().__init__()
        self.title = title
        self.text = text
        self.setupUi(self)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(511, 522)
        Dialog.setStyleSheet(u"background-color: rgb(48, 49, 71);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Star Cartoon"])
        font.setPointSize(28)
        self.widget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_label = QLabel(self.widget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        self.title_label.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Spicy Shrimp"])
        font1.setPointSize(22)
        font1.setBold(False)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"QLabel{\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "}")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_label)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(138, 139, 186);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 473, 359))
        self.scrollAreaWidgetContents.setStyleSheet(u"border-radius: 12px;\n"
                                                    "background-color: rgb(34, 34, 50);")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.text_label = QLabel(self.scrollAreaWidgetContents)
        self.text_label.setObjectName(u"text_label")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.text_label.setFont(font2)
        self.text_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.text_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.text_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line_2 = QFrame(self.widget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(138, 139, 186);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout_4.addWidget(self.widget_4)

        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", self.title, None))
        self.text_label.setText(QCoreApplication.translate("Dialog", self.text, None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"PushButton", None))


class disp(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.e = QSoundEffect()
        self.e.setSource(QUrl.fromLocalFile("pling.wav"))
        self.e.setLoopCount(5)
        self.e.setVolume(20)

    def show_dialog(self, title, text):
        self.e.play()
        self.n = Dialog(title, text)
        self.n.show()
        self.n.setFocus()


# PLING SOUND EFFECT: https://youtu.be/GVAF07-2Xic?si=6SvsMRh9HQEW3XUv


def vega_main():
    w = disp()
    vega = api.Vega_Portal()
    vega.set_name("Notifier")
    vega.add_method(api.Method(w.show_dialog, api.EXECUTION, formal_name="Show Notification"))
    vega.add_display_screen(w)
    return vega
