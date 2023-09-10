import json
from inspect import signature
import socket
import os
import threading

from PySide6.QtCore import QObject, Signal

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
    def __init__(self, name, itg_name, outputs=None):
        self.name = name
        self.itg_name = itg_name
        self.outputs = outputs


class ConnSignals(QObject):
    received_data_from_vega = Signal(dict)


class VegaConnection(socket.socket):

    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer_size = 1024
        self.try_connection()
        self.is_closing = False
        self.signals = ConnSignals()

    def try_connection(self):
        try:
            with open(os.path.join(os.getenv("APPDATA"), ".vega", "ports.veg"), "r") as file:
                for line in file.readlines():
                    if "Port:" in line:
                        self.connect(("127.0.0.1", int(line.split("Port:")[1].rstrip().lstrip())))
                        self.receive()
        except:
            self.close()
            raise "VegaConnectionException"

    def emit(self, e: Event, d):
        self.sendall(json.dumps({"event": e.name, "itg": e.itg_name, "data": d}).encode())

    def finishConnection(self):
        self.is_closing = True

    def receive(self):
        threading.Thread(target=self.handleReceivedData).start()  # https://realpython.com/intro-to-python-threading/

    def handleReceivedData(self):
        while True:
            data = self.recv(self.buffer_size).decode()
            if data == "close_socket" or self.is_closing:
                self.close()
                break
            else:
                self.signals.emit(json.loads(data))


class Vega_Portal:
    def __init__(self):
        self.methods = []
        self.display = None
        self.name = None
        self.vega_main_software_class = None
        self.events = []
        self.socket = None

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
