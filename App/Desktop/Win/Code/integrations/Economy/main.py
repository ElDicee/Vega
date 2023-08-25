import App.Desktop.Win.Code.integrations.VegaAPI as api
from PySide6 import QtCore, QtGui, QtWidgets


def vega_main():
    vega = api.Vega_Portal()
    vega.add_display_screen(QtWidgets.QPushButton("HI"))
    return vega