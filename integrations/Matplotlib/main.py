import random

from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PySide6.QtWidgets import QHBoxLayout, QScrollArea, QWidget, QVBoxLayout, QStackedWidget

import integrations.VegaAPI as api
import sys
import matplotlib

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


# https://www.geeksforgeeks.org/dynamically-updating-plot-in-matplotlib/


class PlotGraph(FigureCanvasQTAgg):
    def __init__(self, x, y, parent=None):
        plt.ion()
        self.fig = Figure(figsize=(7, 5), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.axes.plot(x, y)[0]
        super(PlotGraph, self).__init__(self.fig)

    def update(self):
        self.fig = Figure(figsize=(7, 5), dpi=100, facecolor="g")
        self.axes.plot(self.x, self.y)
        plt.xlim(self.x[0], self.x[-1])


class DisplayPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.x = [1, 2, 4]
        self.y = [1, 2, 3]
        self.plot = PlotGraph(self.x, self.y)
        toolbar = NavigationToolbar(self.plot, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.plot)

        self.setLayout(layout)

    def update_graph(self):
        self.update_Val()
        self.plot = PlotGraph(self.x, self.y)
        self.update()

    def update_Val(self):
        self.y.append(random.randint(1, 10))
        self.x.append(self.x[-1] + 1)


class DisplayWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.plots = {}
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(919, 716)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(200, 16777215))
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
                                      "border-top-right-radius:  8px;\n"
                                      "border-bottom-right-radius:  8px;\n"
                                      "}")
        self.scrollArea.setWidgetResizable(True)
        self.plots_container = QWidget()
        self.plots_container.setObjectName(u"plots_container")
        self.plots_container.setGeometry(QRect(0, 0, 200, 716))
        self.verticalLayout = QVBoxLayout(self.plots_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.plots_container)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ToolBar_Widget = QWidget(self.widget)
        self.ToolBar_Widget.setObjectName(u"ToolBar_Widget")
        self.ToolBar_Widget.setMaximumSize(QSize(16777215, 100))
        self.ToolBar_Widget.setMinimumSize(QSize(0, 100))
        self.ToolBar_Widget.setStyleSheet(u"QWidget#ToolBar_Widget{\n"
                                          "	background-color: rgb(42, 45, 54);\n"
                                          "border-bottom-left-radius: 20px;\n"
                                          "border-bottom-right-radius: 20px;\n"
                                          "}")

        self.verticalLayout_2.addWidget(self.ToolBar_Widget)

        self.plot = DisplayPlot()

        self.PlotWidget = QStackedWidget(self.widget)
        self.PlotWidget.setObjectName(u"PlotWidget")
        self.PlotWidget.addWidget(self.plot)

        self.verticalLayout_2.addWidget(self.PlotWidget)

        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

    def add_plot(self, name):
        pass

    def remove_plot(self, name):
        self.plots.pop(name)

    def update_plot(self):
        self.plot.update_graph()

    def add_x(self, d):
        self.plot.x.append(d)


def vega_main():
    wid = DisplayWidget()
    vega = api.Vega_Portal()
    vega.set_name("MatPlotLib")
    vega.add_display_screen(wid)
    vega.add_method(api.Method(wid.update_plot, api.EXECUTION, formal_name="Update Plot Test"))
    vega.add_method(api.Method(wid.add_x, api.EXECUTION, formal_name="Add X"))
    return vega
