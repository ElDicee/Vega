import sys

from PySide6.QtCore import QMetaObject, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QApplication

import App.Desktop.Win.Code.integrations.VegaAPI as api
from PySide6 import QtCore, QtGui, QtWidgets

from App.Desktop.Win.Code.integrations.VegaAPI import Event

CALCULATE_EVENT = Event("Calculate Event", "Math", outputs={"Result": float})


def addition(*args):
    return sum(args)


def subtraction(*args):
    return sum(map(lambda x: x * -1, args))


def multiplication(a: int or float, b: int or float):
    return a * b


def test_event():
    pass


def division(a, b):
    if b == 0:
        b += 1 * (10 ** -10)
    return a / b if b != 0 else None


def runServer(addr: str):
    return "hello"


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(395, 238)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        conn = api.VegaConnection()

        self.verticalLayout.addWidget(self.textEdit)

        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.clicked.connect(lambda: conn.emit(CALCULATE_EVENT, self.textEdit.toPlainText()))

        self.verticalLayout.addWidget(self.send)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"Send", None))


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Math")
    vega.add_method(api.Method(addition, api.OPERATOR, outputs={"result": float}))
    vega.add_event(CALCULATE_EVENT)
    vega.add_method(api.Method(subtraction, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(multiplication, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(division, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(runServer, api.EXECUTION, outputs={"result": str}, formal_name="Run Server"))
    vega.add_display_screen(QtWidgets.QPushButton("CLICK ME!"))
    return vega


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ui_MainWindow()
    w.show()
    sys.exit(app.exec())