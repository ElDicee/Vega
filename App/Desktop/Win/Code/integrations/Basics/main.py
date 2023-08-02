import App.Desktop.Win.Code.integrations.VegaAPI as api


def addition(a, *args):
    return sum(args)


def subtraction(*args):
    return sum(map(lambda x: x * -1, args))


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b if b != 0 else None


def vega_main():
    vega = api.Vega_Portal()
    vega.add_method(addition)
    vega.add_method(subtraction)
    vega.add_method(multiplication)
    vega.add_method(division)
    return vega
