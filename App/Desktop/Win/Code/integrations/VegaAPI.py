from inspect import signature

EXECUTION = "exec"
OPERATOR = "oper"


class Method:
    def __init__(self, func, type=EXECUTION, outputs=None, event=False, **kwargs):
        if outputs is None:
            outputs = {"Output": object}
        self.name = func.__name__
        self.func = func
        self.inputs = get_func_params(self.func)
        self.node_type = type
        self.custom_area = None
        self.output_types = outputs
        self.formal_name = self.name
        self.event = False
        if kwargs.get("formal_name"):
            self.formal_name = kwargs.get("formal_name")

    def setCustomArea(self, w):
        self.custom_area = w


class Vega_Portal:
    def __init__(self):
        self.methods = []
        self.display = None

    def add_method(self, m):
        self.methods.append(m)

    def add_display_screen(self, w):
        self.display = w


def get_func_params(func):
    sign = signature(func)
    return [str(x) for x in sign.parameters.values()]