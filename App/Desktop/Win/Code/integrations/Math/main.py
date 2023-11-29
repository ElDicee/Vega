import sys

from PySide6.QtCore import QMetaObject, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QApplication

import App.Desktop.Win.Code.integrations.VegaAPI as api
from PySide6 import QtCore, QtGui, QtWidgets
import datetime

from App.Desktop.Win.Code.integrations.VegaAPI import Event

CHAT_EVENT = Event("Chat Event", "Math", outputs={"Text": str})


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


def writeLogs(text: str):
    with open("logs.txt", "r+") as file:
        file.read()
        file.write(f"[{datetime.datetime.now()}] {text}\n")
        file.close()


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
        try:
            self.conn = api.VegaConnection(False)
        except:
            self.conn = None

        self.verticalLayout.addWidget(self.textEdit)

        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.clicked.connect(lambda: self.send_data(CHAT_EVENT, self.textEdit.toPlainText()))

        self.verticalLayout.addWidget(self.send)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"Send", None))

    def send_data(self, event, data):
        if self.conn:
            if self.conn.is_closing:
                try:
                    self.conn = api.VegaConnection(False)
                except:
                    print("Could not connect to Vega Portal.")
            else:
                self.conn.emit(event, {"Text": data})
        else:
            try:
                self.conn = api.VegaConnection(False)
            except:
                print("Could not connect to Vega Portal.")


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Math")
    vega.add_method(api.Method(addition, api.OPERATOR, outputs={"result": float}))
    vega.add_event(CHAT_EVENT)
    vega.add_method(api.Method(subtraction, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(multiplication, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(division, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(writeLogs, api.EXECUTION, formal_name="Write Log"))
    vega.add_display_screen(QtWidgets.QPushButton("CLICK ME!"))
    return vega


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ui_MainWindow()
    w.show()
    sys.exit(app.exec())
