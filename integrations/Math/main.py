import math

import integrations.VegaAPI as api


def suma(num1: float, num2: float):
    return num1 + num2


def resta(num1: float, num2: float):
    return num1 - num2


def multi(num1: float, num2: float):
    return num1 * num2


def divis(num1: float, num2: float):
    return num1 / num2 if num2 != 0 else None


def sine(value: float):
    return math.sin(value)


def cosine(value: float):
    return math.cos(value)


def tangent(value: float):
    return math.tan(value)


def arcsin(value: float):
    return math.asin(value)


def arccos(value: float):
    return math.acos(value)


def arctan(value: float):
    return math.atan(value)


def factorial(num: int):
    return math.factorial(num)


def e_num():
    return math.e


def pi_num():
    return math.pi


def elev(base: float, exponent: float):
    return base ** exponent


def modul(num1: float, num2: float):
    return num1 % num2 if num2 != 0 else None


def square_root(num: float):
    return math.sqrt(num)


def loga_10(num: float):
    return math.log10(num)


def loga(num: float, base: float):
    return math.log(num, base)


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Maths")
    vega.add_method(api.Method(suma, api.OPERATOR, outputs={"Result": float}, formal_name="Number Addition"))
    vega.add_method(api.Method(resta, api.OPERATOR, outputs={"Result": float}, formal_name="Number Subtraction"))
    vega.add_method(api.Method(multi, api.OPERATOR, outputs={"Result": float}, formal_name="Number Multiplication"))
    vega.add_method(api.Method(divis, api.OPERATOR, outputs={"Result": None}, formal_name="Number Division"))
    vega.add_method(api.Method(sine, api.OPERATOR, outputs={"Result": float}, formal_name="Sine"))
    vega.add_method(api.Method(cosine, api.OPERATOR, outputs={"Result": float}, formal_name="Cosine"))
    vega.add_method(api.Method(tangent, api.OPERATOR, outputs={"Result": float}, formal_name="Tangent"))
    vega.add_method(api.Method(arcsin, api.OPERATOR, outputs={"Result": float}, formal_name="Arcsine"))
    vega.add_method(api.Method(arccos, api.OPERATOR, outputs={"Result": float}, formal_name="Arcosine"))
    vega.add_method(api.Method(arctan, api.OPERATOR, outputs={"Result": float}, formal_name="Arctangent"))
    vega.add_method(api.Method(factorial, api.OPERATOR, outputs={"Result": int}, formal_name="Factorial"))
    vega.add_method(api.Method(e_num, api.OPERATOR, outputs={"Result": float}, formal_name="Number e"))
    vega.add_method(api.Method(pi_num, api.OPERATOR, outputs={"Result": float}, formal_name="Number pi"))
    vega.add_method(api.Method(elev, api.OPERATOR, outputs={"Result": float}, formal_name="Power"))
    return vega
