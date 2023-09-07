from inspect import signature
import socket
import os
import uuid

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
        self.event = event
        if kwargs.get("formal_name"):
            self.formal_name = kwargs.get("formal_name")

    def setCustomArea(self, w):
        self.custom_area = w


class Event:
    def __init__(self, name):
        self.name = name

    def emit(self, d):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            with open(os.path.join(os.getenv("APPDATA"), ".vega", "ports.veg"), "r") as file:
                for line in file.readlines():
                    if "Port:" in line:
                        soc.connect(("127.0.0.1", int(line.split("Port:")[1].rstrip().lstrip())))
                        print("Connected")
                        data = {"": {"event": self.name, "data": d}}
                        soc.send(data)
                        print("Sent")
        except:
            pass
        soc.close()


class Vega_Portal:
    def __init__(self):
        self.methods = []
        self.display = None
        self.name = None
        self.vega_main_software_class = None
        self.events = []

    def add_method(self, m: Method):
        self.methods.append(m)

    def set_name(self, name):
        self.name = name

    def add_display_screen(self, w):
        self.display = w

    def add_event(self, e: Event):
        if not e in self.events:
            self.events.append(e)


def get_func_params(func):
    sign = signature(func)
    return [str(x) for x in sign.parameters.values()]