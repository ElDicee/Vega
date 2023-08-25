# -*- coding: utf-8 -*-

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QEnterEvent, QDragMoveEvent, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget, QGraphicsItem, QGraphicsProxyWidget)
from App.Desktop.Win.Code.ui.Elements.NodePin import Pin, PinType
import enum

class NodeItem(QGraphicsItem):
    def __init__(self, w):
        super().__init__()
        self.proxy_widget = QGraphicsProxyWidget(self)
        self.proxy_widget.setWidget(w)

    def boundingRect(self):
        return self.proxy_widget.boundingRect()

    def paint(self, painter, option, widget):
        pass

    def mousePressEvent(self, event):
        self.node_widget.mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.node_widget.mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        self.node_widget.mouseMoveEvent(event)