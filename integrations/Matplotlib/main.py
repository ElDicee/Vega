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


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class PlotGraph(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(7, 5), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        super(PlotGraph, self).__init__(self.fig)


class DisplayPlot(QWidget):
    def __init__(self):
        super().__init__()

        self.plot = PlotGraph()
        toolbar = NavigationToolbar(self.plot, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.plot)

        self.setLayout(layout)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


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
        pass
        # self.plot.plot.axes.plot([random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50)],
        #                          [random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50)])
        # self.plot.plot.draw()
        # self.plot.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()


def vega_main():
    wid = DisplayWidget()
    vega = api.Vega_Portal()
    vega.set_name("MatPlotLib")
    vega.add_display_screen(wid)
    vega.add_method(api.Method(wid.update_plot, api.EXECUTION, formal_name="Update Plot Test"))
    return vega
