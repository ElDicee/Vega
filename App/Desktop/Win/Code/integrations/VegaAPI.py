from inspect import signature


class Vega_Portal():
    def __init__(self):
        self.methods = []

    def add_method(self, func):
        self.methods.append((func.__name__, func, get_func_params(func)))

def get_func_params(func):
    args_presence = False
    kwargs_presence = False
    sign = signature(func)
    return [str(x) for x in sign.parameters.values()]