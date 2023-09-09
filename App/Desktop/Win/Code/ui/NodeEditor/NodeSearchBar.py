# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QMimeData)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QMouseEvent, QDrag)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QScrollArea, QSizePolicy, QVBoxLayout,
                               QWidget, QPushButton, QGroupBox)


class NodeSearchBar(QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.elements = []
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"ContentPane")
        self.resize(266, 642)
        self.setStyleSheet(
            u"background-color: rgba(64, 72, 108, 255);\nQWidget#ContentPane{background-color: rgba(64, 72, 108, 255);}")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"filter_content_widget")
        self.widget.setStyleSheet("QWidget#filter_content_widget{background-color: rgba(64, 72, 108, 255);}")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.search_icon = QLabel(self.widget)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setStyleSheet("QLabel#search_icon{background-color: rgba(64, 72, 108, 255);}")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_icon.sizePolicy().hasHeightForWidth())
        self.search_icon.setSizePolicy(sizePolicy1)
        self.search_icon.setMinimumSize(QSize(20, 20))
        self.search_icon.setMaximumSize(QSize(20, 20))
        self.search_icon.setStyleSheet(u"border-image: url(./res/icons/Feather_white/filter.svg);")

        self.horizontalLayout.addWidget(self.search_icon)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 64, 98), stop:1 rgb(56, 60, 72));\n"
            "border-top-left-radius: 8px;\n"
            "border-top-right-radius: 8px;\n"
            "border-bottom: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(140, 0, 255), stop:1 rgb(0, 221, 255));\n"
            "color: rgb(255, 255, 255);")

        self.lineEdit.setPlaceholderText("Filter")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.verticalLayout.addWidget(self.widget)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.setStyleSheet(u"QScrollArea{background-color: rgba(64, 72, 108, 255);}"
                           "QGroupBox{\n"
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
                           "}QLabel#search_icon{background-color: rgba(64, 72, 108, 255);}\n"
                           "QLabel:hover{\n"
                           "	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(1, 204, 187, 255));\n"
                           "	border-width: 5px;\n"
                           "	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 85, 255, 0"
                           "));\n"
                           "}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)

        self.contentLayout = QVBoxLayout(self.scrollArea)

        self.verticalLayout.addWidget(self.scrollArea)
        self.lineEdit.textEdited.connect(self.start_filter)

        QMetaObject.connectSlotsByName(self)

        self.refreshElements()

    def refreshElements(self):
        self.elements.clear()
        for w in self.contentLayout.children():
            self.contentLayout.removeWidget(w)
            del w
        for itg in self.parent().vega.integrations.values():
            self.add_section(itg.name)
            for m in itg.methods.keys():
                self.add_element(m, section=itg.name)
            for e in itg.events.keys():
                self.add_element(e, section=itg.name)

    def add_section(self, name):
        section = FilterSection(self.scrollArea, name)
        self.contentLayout.addWidget(section)
        self.elements.append(section)

    def add_element(self, element, section=None, event=False):
        if section:
            sec = self.get_section(section)
            sec.add_item(element, event=event)
        else:
            label = FilterElement(parent=self.scrollArea, isevent=event)
            label.setText(element)
            self.contentLayout.addWidget(label)
            self.elements.append(label)

    def get_section(self, name):
        sec = None
        for x in self.elements:
            if isinstance(x, FilterSection) and x.title() == name:
                sec = x
                break
        if sec is None: raise "Section not Found"
        return sec

    def start_filter(self, text):
        print(text)
        for element in self.elements:
            if isinstance(element, FilterSection):
                element.showFiltered(text)
            else:
                element.show() if text in element.text() else element.hide()


class FilterElement(QPushButton):
    def __init__(self, section=None, isevent=False, **kwargs):
        super().__init__(**kwargs)
        self.section: FilterSection = section
        self.isevent = isevent

    def mousePressEvent(self, e: QMouseEvent):
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.text())
        mime_data.setData("section", str(self.section.name).encode())
        mime_data.setData("element", self.text().encode())
        mime_data.setData("event", str(self.isevent).encode())
        mime_data.item = self
        drag.setMimeData(mime_data)

        # Drag needs a pixmap or else it'll error due to a null pixmap
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor("darkgray"))
        drag.setPixmap(pixmap)
        drag.exec_()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        pass
    # SPAWN NODE


class FilterSection(QGroupBox):
    def __init__(self, parent, name, **kwargs):
        super().__init__(**kwargs)
        self.parent = parent
        self.name = name
        self.setObjectName(u"{}".format(name))
        self.setTitle(name)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.items = []

    def __str__(self):
        return self.title()

    def add_item(self, name, event):
        label = FilterElement(section=self, parent=self, isevent=event)
        label.setText(name)
        self.verticalLayout.addWidget(label, 0, Qt.AlignmentFlag.AlignLeft)
        self.items.append(label)

    def hide_elements(self):
        for item in self.items:
            item.hide()

    def show_elements(self):
        for item in self.items:
            item.show()

    def showFiltered(self, s):
        b = False
        for item in self.items:
            if s in item.text():
                item.show()
            else:
                if not b: b = True
                item.hide()
        if not b:  # SI NO HI HA CAP ELEMENT DE LA SECCIÓ QUE NO CUMPLEIXI EL FILTRE
            self.show()
        else:
            self.hide()
