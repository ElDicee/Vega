import random

from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QHBoxLayout, QScrollArea, QWidget, QVBoxLayout, QStackedWidget, QGroupBox, QPushButton, \
    QFrame, QLabel

import integrations.VegaAPI as api
import matplotlib

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


# https://www.pythonguis.com/tutorials/plotting-matplotlib/


class PlotGraph(FigureCanvasQTAgg):
    def __init__(self, x, y, parent=None):
        plt.ion()
        self.fig = Figure(figsize=(7, 5), dpi=100)
        self.axes = self.fig.add_subplot(111)
        super(PlotGraph, self).__init__(self.fig)


class Dataset:
    def __init__(self):
        self.x = []
        self.y = []


class DisplayPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.datasets = {}
        self.plot = PlotGraph(self.x, self.y)
        toolbar = NavigationToolbar(self.plot, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.plot)

        self.setLayout(layout)

    def update_graph(self):
        self.plot.axes.cla()
        for dat in self.datasets:
            self.plot.axes.plot(dat.x, dat.y)
        self.plot.draw()


class BaseWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.plots = {}
        self.vars = {}  # name:val
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 624)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PlotScrollArea = QScrollArea(self.groupBox)
        self.PlotScrollArea.setObjectName(u"PlotScrollArea")
        self.PlotScrollArea.setMaximumSize(QSize(16777215, 100))
        self.PlotScrollArea.setStyleSheet(u"border-radius: 10px;\n"
                                          "\n"
                                          "QPushButton{\n"
                                          "border: 2px solid rgb(0, 170, 255);\n"
                                          "}")
        self.PlotScrollArea.setFrameShape(QFrame.NoFrame)
        self.PlotScrollArea.setFrameShadow(QFrame.Plain)
        self.PlotScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PlotScrollArea.setWidgetResizable(True)
        self.PlotScrollAreaContent = QWidget()
        self.PlotScrollAreaContent.setObjectName(u"PlotScrollAreaContent")
        self.PlotScrollAreaContent.setGeometry(QRect(0, 0, 718, 77))
        self.horizontalLayout_3 = QHBoxLayout(self.PlotScrollAreaContent)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.PlotScrollArea.setWidget(self.PlotScrollAreaContent)

        self.horizontalLayout_2.addWidget(self.PlotScrollArea)

        self.verticalLayout.addWidget(self.groupBox)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(100, 0))
        self.groupBox_2.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.groupBox_2.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.VariableScrollArea = QScrollArea(self.groupBox_2)
        self.VariableScrollArea.setObjectName(u"VariableScrollArea")
        self.VariableScrollArea.setMaximumSize(QSize(9999, 16777215))
        self.VariableScrollArea.setFrameShape(QFrame.NoFrame)
        self.VariableScrollArea.setFrameShadow(QFrame.Plain)
        self.VariableScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.VariableScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 501))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.VariableScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.VariableScrollArea)

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.PlotStackedWidget = QStackedWidget(self.widget)
        self.PlotStackedWidget.setObjectName(u"PlotStackedWidget")

        self.horizontalLayout.addWidget(self.PlotStackedWidget)

        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Gr\u00e0fics", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Panell de Dades", None))

    def update_plot(self, plot_name):
        self.plots.get(plot_name).update_graph()

    def create_plot(self, name):
        self.plots.update({name: DisplayPlot()})
        self.PlotStackedWidget.addWidget(self.plots.get(name))
        self.PlotStackedWidget.setCurrentWidget(self.plots.get(name))
        b = QPushButton(name)
        b.setStyleSheet("""
        border: 2px solid rgb(20, 140, 200);
        color: rgb(255,255,255);
        background-color: rgb(74,74,74);
        """)
        b.setFont(QFont("Yu Gothic UI", 12))
        b.clicked.connect(lambda: self.PlotStackedWidget.setCurrentWidget(self.plots.get(name)))
        b.setMaximumSize(100, 9999)
        self.horizontalLayout_3.addWidget(b)

    def add_data(self, plot_name, dataset_name, x_val, y_val):
        self.plots.get(plot_name).datasets.get(dataset_name).x.append(x_val)
        self.plots.get(plot_name).datasets.get(dataset_name).y.append(y_val)

    def add_dataset(self, plot_name, dataset_name, x_vals, y_vals):
        d = Dataset()
        d.x = x_vals if isinstance(x_vals, list) else list(x_vals)
        d.y = y_vals if isinstance(y_vals, list) else list(y_vals)
        self.plots.get(plot_name).datasets.update({dataset_name: d})

    def get_plots_name(self):
        return [name for name in self.plots.keys()]

    def get_plot_datasets_name(self, plot):
        return [name for name in self.plots.get(plot).datasets.keys()]

    def add_variable(self, name):
        self.vars.update({name: 0})
        g = QGroupBox(title=name)
        vlay = QVBoxLayout(g)
        g.setLayout(g)
        lab = QLabel()
        vlay.addWidget(lab)

    def update_variable(self, name, val):
        self.vars.update({name: val})
        for g in self.scrollAreaWidgetContents_2.layout().children():
            if g.title == name:
                g.children()[0].setText(str(val))
                break


def vega_main():
    wid = BaseWidget()
    vega = api.Vega_Portal()
    vega.set_name("MatPlotLib")
    vega.add_display_screen(wid)
    vega.add_method(api.Method(wid.create_plot, api.EXECUTION, formal_name="Create Plot"))
    vega.add_method(api.Method(wid.update_plot, api.EXECUTION, formal_name="Update Plot"))
    vega.add_method(api.Method(wid.add_data, api.EXECUTION, formal_name="Add Plot Dataset Value"))
    vega.add_method(api.Method(wid.add_dataset, api.EXECUTION, formal_name="Add Line to Plot"))
    vega.add_method(api.Method(wid.get_plots_name, api.OPERATOR, outputs={"List": None}, formal_name="Get Plots Name"))
    vega.add_method(api.Method(wid.update_variable, api.EXECUTION, formal_name="Update Variable Value"))
    vega.add_method(api.Method(wid.add_variable, api.EXECUTION, formal_name="Add Variable"))
    vega.add_method(api.Method(wid.get_plot_datasets_name, api.OPERATOR, outputs={"List": None},
                               formal_name="Get Plot Datasets Name"))
    return vega
