import App.Desktop.Win.Code.integrations.VegaAPI as api


def not_sent(boolean: bool):
    return not boolean


def addition(a: int, b: int):
    return a + b


def subtraction(a: int, b: int):
    return a - b


def multiplication(a: int, b: int):
    return a * b


def division(a, b):
    if b == 0:
        b += 1 * (10 ** -10)
    return a / b if b != 0 else None


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Basics")
    vega.add_method(api.Method(not_sent, api.OPERATOR, outputs={"result": bool}, formal_name="NOT"))
    vega.add_method(api.Method(addition, api.OPERATOR, outputs={"result": int}, formal_name="Addition"))
    vega.add_method(api.Method(subtraction, api.OPERATOR, outputs={"result": int}, formal_name="Subtraction"))
    vega.add_method(api.Method(multiplication, api.OPERATOR, outputs={"result": int}, formal_name="Product"))
    vega.add_method(api.Method(division, api.OPERATOR, outputs={"result": float}, formal_name="Quotient"))
    return vega
