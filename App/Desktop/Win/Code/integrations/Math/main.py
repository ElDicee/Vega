import App.Desktop.Win.Code.integrations.VegaAPI as api
from PySide6 import QtCore, QtGui, QtWidgets


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

def vega_main():
    vega = api.Vega_Portal()
    vega.add_method(api.Method(addition, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(subtraction, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(multiplication, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(division, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(runServer, api.EXECUTION, outputs={"result": str}, formal_name="Run Server"))
    vega.add_display_screen(QtWidgets.QPushButton("CLICK ME!"))
    return vega
