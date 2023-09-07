import App.Desktop.Win.Code.integrations.VegaAPI as api


def addition(a: int, b: int):
    return a+b


def subtraction(a: int, b: int):
    return a-b


def multiplication(a: int, b: int):
    return a * b


def division(a, b):
    if b == 0:
        b += 1 * (10 ** -10)
    return a / b if b != 0 else None


def runServer(addr: str):
    return "hello"


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Basics")
    vega.add_method(api.Method(addition, api.OPERATOR, outputs={"result": int}))
    vega.add_method(api.Method(subtraction, api.OPERATOR, outputs={"result": int}))
    vega.add_method(api.Method(multiplication, api.OPERATOR, outputs={"result": int}))
    vega.add_method(api.Method(division, api.OPERATOR, outputs={"result": float}))
    vega.add_method(api.Method(runServer, api.EXECUTION, outputs={"result": str}, formal_name="Run Server"))
    return vega
