import App.Desktop.Win.Code.integrations.VegaAPI as api


def not_sent(boolean: bool):
    return not boolean


# STRING-------------------------------------STRING-------------------------------------STRING-------------------------------------STRING-------------------------------------

def to_str(element):
    return str(element)


def _split(string: str, char: str):
    return string.split(char)


# MATH--------------------------------------MATH--------------------------------------MATH--------------------------------------MATH--------------------------------------

def to_int(element):
    return int(element)


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


def maximum(a: int, b: int):
    return max(a, b)


def if_pol(f, condition: bool):
    return f("TRUE") if condition else f("FALSE")


def elseif_pol(f, condition1: bool, condition2: bool):
    if condition1:
        f("OPT1")
    elif condition2:
        f("OPT2")
    else:
        f("ELSE")


def for_each_pol(f, list):
    for e in list:
        f("ELEMENT", {"Element": e})
    f("FINISHED")


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Basics")
    vega.add_method(api.Method(not_sent, api.OPERATOR, outputs={"result": bool}, formal_name="NOT"))
    vega.add_method(api.Method(addition, api.OPERATOR, outputs={"result": int}, formal_name="Addition"))
    vega.add_method(api.Method(subtraction, api.OPERATOR, outputs={"result": int}, formal_name="Subtraction"))
    vega.add_method(api.Method(multiplication, api.OPERATOR, outputs={"result": int}, formal_name="Product"))
    vega.add_method(api.Method(division, api.OPERATOR, outputs={"result": float}, formal_name="Quotient"))
    vega.add_method(api.Method(to_str, api.OPERATOR, outputs={"String": str}, formal_name="To String"))
    vega.add_method(api.Method(to_int, api.OPERATOR, outputs={"Integer": int}, formal_name="To Integer"))
    vega.add_method(api.Method(maximum, api.OPERATOR, outputs={"Maximum": int}, formal_name="Max"))
    vega.add_method(api.Method(_split, api.OPERATOR, outputs={"Elements": None}, formal_name="Split"))

    if_sp = api.SpecialMethod(None, api.EXECUTION, formal_name="If Else")
    if_sp.add_execution_output("TRUE")
    if_sp.add_execution_output("FALSE")
    if_sp.set_execution_policy(if_pol)
    vega.add_method(if_sp)

    elif_sp = api.SpecialMethod(None, api.EXECUTION, formal_name="Elif Else")
    elif_sp.add_execution_output("OP1")
    elif_sp.add_execution_output("OPT2")
    elif_sp.add_execution_output("ELSE")
    elif_sp.set_execution_policy(elseif_pol)
    vega.add_method(elif_sp)

    foreach_sp = api.SpecialMethod(None, api.EXECUTION, outputs={"Element": None}, formal_name="For Each Loop")
    foreach_sp.add_execution_output("ELEMENT")
    foreach_sp.add_execution_output("FINISHED")
    foreach_sp.set_execution_policy(for_each_pol)
    vega.add_method(foreach_sp)

    return vega
